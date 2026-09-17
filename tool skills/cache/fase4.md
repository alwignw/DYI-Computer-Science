# Fase 4 — Pola & Arsitektur Cache

Fase terakhir ini menjawab pertanyaan: **"Bagaimana mendesain sistem dengan cache yang benar di skala besar?"**

---

## 13. Cache Patterns — Pola Desain Cache

Ada beberapa pola standar yang dipakai di industri. Masing-masing punya karakteristik berbeda.

---

### Cache-Aside (Lazy Loading)
> Aplikasi yang bertanggung jawab mengelola cache secara manual.

```
Read:
  Aplikasi → cek cache
               ↓ miss
  Aplikasi → query DB
               ↓
  Aplikasi → simpan ke cache
               ↓
  Aplikasi → return data

Write:
  Aplikasi → update DB
  Aplikasi → delete/update cache
```

```python
def get_product(product_id):
    # Aplikasi yang handle semua logika cache
    cached = cache.get(f"product:{product_id}")
    if cached:
        return cached

    product = db.find(product_id)
    cache.set(f"product:{product_id}", product, ttl=3600)
    return product
```

**Karakteristik:**
```
✅ Cache hanya berisi data yang benar-benar diminta
✅ Jika cache down, sistem tetap berjalan (fallback ke DB)
✅ Fleksibel — developer punya full control
❌ Kode lebih verbose (logika cache tersebar di mana-mana)
❌ Cache miss pertama selalu lambat (cold start)
❌ Potensi data stale jika invalidation tidak konsisten
```

**Paling umum dipakai** — cocok untuk general purpose.

---

### Read-Through
> Cache yang **secara otomatis** mengambil data dari DB saat miss.

```
Read:
  Aplikasi → minta data ke Cache
                ↓ miss
             Cache → query DB sendiri
                ↓
             Cache → simpan data
                ↓
  Aplikasi ← return data
```

```python
class ReadThroughCache:
    def __init__(self, db, redis):
        self.db = db
        self.redis = redis

    def get(self, key, loader_fn, ttl=3600):
        cached = self.redis.get(key)
        if cached:
            return json.loads(cached)

        # Cache miss → cache yang fetch sendiri
        data = loader_fn()  # panggil fungsi untuk load dari DB
        self.redis.setex(key, ttl, json.dumps(data))
        return data

# Pemakaian — aplikasi tidak perlu tahu detail cache
cache = ReadThroughCache(db, redis)

product = cache.get(
    key=f"product:{product_id}",
    loader_fn=lambda: db.find("products", product_id)
)
```

**Karakteristik:**
```
✅ Logika cache terpusat, kode aplikasi lebih bersih
✅ Developer tidak perlu ingat "simpan ke cache setelah query"
❌ Cache harus tahu cara load data → coupling lebih tinggi
❌ Miss pertama tetap lambat
```

---

### Write-Through (sebagai pattern, bukan hanya strategy)
> Setiap write ke DB **otomatis** diikuti write ke cache.

```
Write:
  Aplikasi → tulis ke Cache
  Cache    → otomatis tulis ke DB
  Cache    → konfirmasi ke Aplikasi
```

```python
class WriteThroughCache:
    def set(self, key, value, db_writer_fn, ttl=3600):
        # Tulis ke DB dulu
        db_writer_fn(value)

        # Langsung update cache
        self.redis.setex(key, ttl, json.dumps(value))

# Pemakaian:
cache.set(
    key=f"product:{product_id}",
    value=new_product_data,
    db_writer_fn=lambda data: db.update("products", product_id, data)
)
```

**Karakteristik:**
```
✅ Cache selalu konsisten dengan DB
✅ Read setelah write selalu dapat data terbaru
❌ Write lebih lambat (harus tunggu dua operasi selesai)
❌ Cache bisa berisi data yang tidak pernah dibaca (write-heavy, read-light)
```

---

### Perbandingan Pattern:

```
                Cache-Aside   Read-Through   Write-Through
Siapa manage?   Aplikasi      Cache layer    Cache layer
Kode aplikasi   Verbose       Bersih         Bersih
Konsistensi     Manual        Otomatis       Otomatis
Cocok untuk     General       Read-heavy     Read-after-write
```

---

## 14. Distributed Cache — Cache di Sistem Terdistribusi

Saat aplikasi kamu berjalan di banyak server, muncul tantangan baru.

### Masalah tanpa distributed cache:

```
Server A: cache user:123 → {name: "Budi", points: 100}
Server B: cache user:123 → {name: "Budi", points: 150}  ← berbeda!

User update points di Server A
→ Server B masih punya data lama
→ Inconsistency! ❌
```

### Solusi: Centralized Cache

```
Server A ──┐
           ├──→ Redis Cluster (shared) ──→ DB
Server B ──┘

Semua server baca/tulis ke cache yang sama ✅
```

---

### Redis Cluster — Horizontal Scaling

Saat satu Redis node tidak cukup, gunakan **Redis Cluster** — data dibagi ke beberapa node.

```
              Redis Cluster
         ┌────────────────────┐
         │  Node 1            │  → Slot 0–5460
         │  Node 2            │  → Slot 5461–10922
         │  Node 3            │  → Slot 10923–16383
         └────────────────────┘

Key "user:123" → di-hash → masuk ke slot tertentu → ke node yang tepat
```

```python
from redis.cluster import RedisCluster

rc = RedisCluster(
    startup_nodes=[
        {"host": "redis-node-1", "port": 7000},
        {"host": "redis-node-2", "port": 7001},
        {"host": "redis-node-3", "port": 7002},
    ],
    decode_responses=True
)

# Transparant — developer tidak perlu tahu data ada di node mana
rc.set("user:123", json.dumps(user_data))
rc.get("user:123")
```

---

### Consistent Hashing — Teknik Distribusi Key

Masalah distribusi naif:

```python
# Naive: modulo biasa
node_index = hash(key) % jumlah_node

# Masalah: kalau jumlah node berubah (tambah/kurang 1 node)
# → hampir SEMUA key pindah node
# → massive cache miss! ❌
```

**Consistent Hashing** — solusinya:

```
Node dan key sama-sama diletakkan di "ring" (0 – 2^32)

        0
    ┌───┴───┐
    │       │
  NodeA   NodeB
    │       │
    └───┬───┘
       NodeC

Key → di-hash → diletakkan di ring
     → diarahkan ke Node terdekat searah jarum jam

Kalau NodeB dihapus:
→ Hanya key yang tadinya ke NodeB yang pindah ke NodeC
→ Key lain tidak terganggu ✅
```

---

### Replikasi — High Availability

```
Primary Redis ──→ Replica 1
              └──→ Replica 2

Read  → bisa ke Primary atau Replica (load balancing)
Write → hanya ke Primary (lalu sync ke Replica)

Kalau Primary mati:
→ Replica dipromosikan jadi Primary otomatis (Redis Sentinel)
```

```python
# Pisahkan read dan write client
write_client = redis.Redis(host='redis-primary', port=6379)
read_client  = redis.Redis(host='redis-replica', port=6380)

def get_user(user_id):
    return read_client.get(f"user:{user_id}")   # baca dari replica

def update_user(user_id, data):
    write_client.set(f"user:{user_id}", data)   # tulis ke primary
```

---

## 15. Cache Consistency — Menjaga Data Tetap Sinkron

Di sistem terdistribusi, konsistensi adalah tantangan terbesar.

### CAP Theorem dalam konteks cache:

```
        Consistency
            /\
           /  \
          /    \
    Availability ── Partition Tolerance

Kamu hanya bisa pilih 2 dari 3.
Cache biasanya memilih: Availability + Partition Tolerance
→ Artinya: data mungkin tidak selalu konsisten (eventual consistency)
```

---

### Eventual Consistency — Pola Umum di Cache

```
DB diupdate → cache masih stale
                 ↓ (beberapa detik kemudian)
Cache invalidated / TTL expired
                 ↓
Request berikutnya → cache miss → ambil dari DB
                 ↓
Cache terisi data terbaru ✅

"Eventually" konsisten — ada jeda waktu, tapi akhirnya sinkron.
```

---

### Double Delete Pattern — Menghindari Race Condition

```python
# Masalah race condition saat update:

# Thread 1: update user
db.update(user_id, new_data)
cache.delete(f"user:{user_id}")     # hapus cache

# Thread 2: baca user (di antara delete dan re-cache)
data = db.read(user_id)             # baca dari DB (old data?)
cache.set(f"user:{user_id}", data)  # simpan → bisa simpan stale data!
```

**Solusi: Double Delete**
```python
def update_user(user_id, new_data):
    # Hapus cache SEBELUM update
    cache.delete(f"user:{user_id}")

    # Update DB
    db.update("users", user_id, new_data)

    # Hapus cache LAGI setelah update
    # (jaga-jaga ada yang re-cache data lama di antara proses)
    time.sleep(0.5)  # tunggu sebentar
    cache.delete(f"user:{user_id}")
```

---

### Cache Warm-Up — Menghindari Cold Start

Saat server baru restart atau cache kosong, semua request akan miss → DB kena beban besar.

```python
def warm_up_cache():
    """Dijalankan saat aplikasi startup"""
    print("Warming up cache...")

    # Pre-load data yang paling sering diakses
    top_products = db.query("""
        SELECT * FROM products
        ORDER BY view_count DESC
        LIMIT 100
    """)

    for product in top_products:
        cache.set(
            f"product:{product['id']}",
            product,
            ttl=3600
        )

    # Pre-load konfigurasi sistem
    configs = db.query("SELECT * FROM system_configs")
    cache.set("system:configs", configs, ttl=86400)

    print(f"Cache warmed up: {len(top_products)} products loaded")

# Panggil saat startup:
app.on_startup(warm_up_cache)
```

---

## 16. Monitoring Cache — Tahu Kapan Cache Bermasalah

Cache yang tidak dimonitor adalah cache yang tidak bisa diperbaiki.

### Metrik Penting:

```
Hit Rate       → persentase request yang terlayani dari cache
                 Target: > 80% untuk production

Miss Rate      → kebalikan hit rate
                 Tinggi → cache kurang efektif

Eviction Rate  → berapa banyak data dibuang per detik
                 Tinggi → cache terlalu kecil

Memory Usage   → berapa memori yang dipakai
                 > 80% → pertimbangkan scale up

Latency        → berapa lama operasi cache (get/set)
                 Redis seharusnya < 1ms

Key Count      → jumlah key di cache
                 Terlalu banyak → mungkin ada key leak
```

### Monitoring dengan Redis CLI:

```bash
# Info lengkap Redis
redis-cli INFO stats

# Monitor hit/miss rate
redis-cli INFO stats | grep -E "keyspace_hits|keyspace_misses"
# keyspace_hits:8500
# keyspace_misses:1500
# Hit rate = 8500 / (8500+1500) = 85% ✅

# Monitor memory
redis-cli INFO memory | grep used_memory_human
# used_memory_human:256.50M

# Monitor eviction
redis-cli INFO stats | grep evicted_keys
# evicted_keys:1234  ← kalau tinggi, cache perlu diperbesar

# Real-time monitoring
redis-cli MONITOR  # lihat semua operasi secara live (hati-hati di production!)
```

### Monitoring di kode aplikasi:

```python
import time

class MonitoredCache:
    def __init__(self, redis_client):
        self.redis = redis_client
        self.hits = 0
        self.misses = 0

    def get(self, key):
        start = time.time()
        value = self.redis.get(key)
        latency = time.time() - start

        if value:
            self.hits += 1
            metrics.record("cache.hit", 1, tags={"key_prefix": key.split(":")[0]})
        else:
            self.misses += 1
            metrics.record("cache.miss", 1, tags={"key_prefix": key.split(":")[0]})

        metrics.record("cache.latency", latency)
        return value

    @property
    def hit_rate(self):
        total = self.hits + self.misses
        return self.hits / total * 100 if total > 0 else 0
```

---

### Red Flags yang Harus Diperhatikan:

```
🚨 Hit rate tiba-tiba turun drastis
   → Kemungkinan: deployment baru flush cache, TTL terlalu pendek,
     atau traffic pattern berubah

🚨 Eviction rate sangat tinggi
   → Cache terlalu kecil, perlu tambah memori atau scale up

🚨 Latency cache > 10ms
   → Network issue antara app dan Redis, atau Redis overloaded

🚨 Memory usage > 90%
   → Bahaya OOM (Out of Memory), Redis bisa crash

🚨 Key count terus naik tanpa batas
   → Ada key leak — TTL tidak di-set atau invalidation bermasalah
```

---

## ✅ Ringkasan Fase 4

```
Cache Patterns
  Cache-Aside   → aplikasi manage sendiri, paling fleksibel
  Read-Through  → cache yang auto-fetch saat miss
  Write-Through → write ke cache & DB bersamaan, selalu konsisten

Distributed Cache
  Redis Cluster      → data dibagi ke banyak node (horizontal scale)
  Consistent Hashing → distribusi key yang minimal disruption
  Replikasi          → primary untuk write, replica untuk read

Cache Consistency
  Eventual Consistency → cache mungkin stale sesaat, akhirnya sinkron
  Double Delete        → hindari race condition saat update
  Cache Warm-Up        → pre-load data populer saat startup

Monitoring
  Hit Rate       → target > 80%
  Eviction Rate  → tinggi = cache terlalu kecil
  Memory Usage   → jaga di bawah 80%
  Latency        → Redis harus < 1ms
```

---

## 🎓 Recap Keseluruhan — Semua Fase

```
FASE 1 — Fondasi
  Kenapa cache ada    → latency, throughput, redundant computation
  Lokalitas data      → temporal & spatial locality
  Hit vs Miss         → hit rate adalah metrik utama
  Anatomi cache       → key, value, TTL

FASE 2 — Cara Kerja Internal
  Eviction Policy     → LRU (paling umum), LFU, FIFO
  Cache Invalidation  → TTL, event-based, versioning
  Write Strategies    → write-through, write-back, write-around
  Cache Stampede      → locking, early expiry, stale-while-revalidate

FASE 3 — Dunia Nyata
  In-memory / Memoization → @lru_cache, tercepat tapi tidak shared
  Redis               → cache terpusat, shared semua server
  HTTP Cache          → Cache-Control, ETag, CDN
  Database Cache      → query cache, connection pool

FASE 4 — Pola & Arsitektur
  Cache Patterns      → Cache-Aside, Read-Through, Write-Through
  Distributed Cache   → Redis Cluster, Consistent Hashing, Replikasi
  Cache Consistency   → Eventual consistency, Double Delete, Warm-Up
  Monitoring          → Hit rate, Eviction, Memory, Latency
```

---

**Selamat!** 🎉 Kamu sudah menyelesaikan semua fase belajar cache — dari konsep paling dasar sampai arsitektur skala besar.

Langkah selanjutnya yang bisa kamu ambil:
- **Praktik langsung** — install Redis di lokal, coba semua operasi
- **Implementasi** — tambahkan cache ke project yang sedang kamu kerjakan
- **Deep dive** — pilih satu topik yang paling menarik untuk digali lebih dalam

Ada topik dari keempat fase yang mau didalami lebih lanjut? 🚀