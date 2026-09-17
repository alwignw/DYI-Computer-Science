# Fase 2 — Cara Kerja Internal Cache

Fase ini menjawab pertanyaan: **"Apa yang terjadi di dalam cache?"**

---

## 5. Eviction Policy — Siapa yang Dibuang Saat Cache Penuh?

Cache punya ukuran terbatas. Ketika penuh dan ada data baru yang mau disimpan, **harus ada data lama yang dibuang**. Inilah eviction policy.

### Analogi:
Bayangkan meja kerja kamu cuma muat 5 buku. Saat buku ke-6 datang, kamu harus kembalikan salah satu ke rak. **Buku mana yang kamu kembalikan?** Itu keputusan eviction policy.

---

### LRU — Least Recently Used
> Buang data yang **paling lama tidak diakses**

```
Cache size: 4

Waktu →  [A] [B] [C] [D]    ← cache penuh

Request E masuk (miss) → harus buang sesuatu
Urutan terakhir diakses: D(baru) C B A(paling lama)

→ Buang A, masukkan E

Hasil: [E] [B] [C] [D]
```

**Implementasi LRU di Python:**
```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()  # menjaga urutan akses

    def get(self, key):
        if key not in self.cache:
            return None  # miss

        # Pindahkan ke paling akhir (paling baru diakses)
        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            # Buang yang paling depan (paling lama tidak diakses)
            self.cache.popitem(last=False)

# Contoh:
lru = LRUCache(capacity=3)
lru.set("A", 1)
lru.set("B", 2)
lru.set("C", 3)

lru.get("A")      # A jadi paling baru → urutan: B, C, A

lru.set("D", 4)   # Cache penuh → buang B (paling lama)
                  # Hasil: C, A, D
```

**Kapan cocok:** Mayoritas use case — akses data mengikuti pola temporal locality.

---

### LFU — Least Frequently Used
> Buang data yang **paling jarang diakses**

```
Cache: 
  A → diakses 10x
  B → diakses 2x   ← paling jarang
  C → diakses 7x
  D → diakses 5x

Data baru E masuk → buang B
```

**Perbedaan LRU vs LFU:**

| Skenario | LRU | LFU |
|---------|-----|-----|
| Data populer tapi lama tidak diakses | ❌ Bisa terbuang | ✅ Aman (frekuensi tinggi) |
| Data baru yang cuma diakses sekali | ✅ Bertahan sebentar | ⚠️ Rentan dibuang |
| Implementasi | Sederhana | Lebih kompleks |

**Kapan cocok:** Data punya pola popularitas yang stabil — misalnya konten viral yang sering diakses.

---

### FIFO — First In First Out
> Buang data yang **pertama kali masuk**

```
Cache: [A, B, C, D]  ← A masuk pertama

Data E masuk → buang A (paling pertama masuk)
Hasil: [B, C, D, E]
```

**Kapan cocok:** Jarang dipakai karena tidak memperhitungkan pola akses. Cocok untuk pipeline data yang urutan masuknya penting.

---

### Perbandingan Eviction Policy:

```
                   Performa    Kompleksitas    Use Case
LRU                ⭐⭐⭐⭐       Sedang          General purpose
LFU                ⭐⭐⭐⭐⭐      Tinggi          Popularitas stabil
FIFO               ⭐⭐          Rendah          Sederhana/pipeline
Random             ⭐⭐⭐         Sangat rendah   Tidak butuh presisi
```

**Di dunia nyata:** Redis pakai LRU atau LFU (bisa dikonfigurasi). CPU cache pakai LRU.

---

## 6. Cache Invalidation — Masalah Paling Sulit

> *"There are only two hard things in Computer Science: cache invalidation and naming things."* — Phil Karlton

### Kenapa sulit?

Karena cache menyimpan **salinan** data. Ketika data asli berubah, cache bisa jadi **stale** (basi) — masih menyimpan versi lama.

```
DB:    user Budi → email: budi@lama.com
Cache: user Budi → email: budi@lama.com  ✅ sinkron

-- Budi update email --

DB:    user Budi → email: budi@baru.com  ← updated
Cache: user Budi → email: budi@lama.com  ❌ STALE!
```

### Strategi Invalidation:

**TTL-based (paling umum)**
```python
# Cache otomatis expired setelah N detik
cache.set("user:123", user_data, ttl=300)  # expired setelah 5 menit
```
- ✅ Sederhana, tidak perlu logika tambahan
- ❌ Data bisa stale sampai TTL habis

---

**Event-based (paling akurat)**
```python
def update_user(user_id, new_data):
    # 1. Update di DB
    db.update("users", user_id, new_data)

    # 2. Langsung hapus/update cache
    cache.delete(f"user:{user_id}")

# Sekarang request berikutnya akan cache miss
# → ambil data terbaru dari DB → simpan ke cache lagi
```
- ✅ Cache selalu up-to-date
- ❌ Harus ingat invalidate cache di setiap tempat yang update data

---

**Cache versioning**
```python
# Tambahkan versi ke key
cache.set("user:123:v2", user_data)

# Saat update, bump versinya
cache.set("user:123:v3", new_user_data)
# v2 otomatis tidak dipakai lagi → akan dibuang saat TTL habis
```
- ✅ Aman untuk deployment bertahap
- ❌ Key lama menumpuk di memori

---

## 7. Write Strategies — Kapan Cache Diperbarui Saat Menulis?

Ini tentang **bagaimana data ditulis** — ke cache, ke DB, atau keduanya, dan dalam urutan apa.

---

### Write-Through
> Tulis ke **cache dan DB secara bersamaan**

```
Aplikasi → tulis data
              ↓
    ┌─────────────────┐
    │   Cache (sync)  │ → DB (sync)
    └─────────────────┘
```

```python
def update_product(product_id, new_data):
    # Tulis ke DB dulu
    db.update("products", product_id, new_data)
    # Langsung update cache juga
    cache.set(f"product:{product_id}", new_data)
```

- ✅ Cache selalu konsisten dengan DB
- ✅ Read selalu dapat data terbaru
- ❌ Write lebih lambat (harus tunggu keduanya selesai)
- ❌ Cache sering diisi data yang mungkin tidak pernah dibaca lagi

**Cocok untuk:** Data yang sering dibaca setelah ditulis.

---

### Write-Back (Write-Behind)
> Tulis ke **cache dulu**, DB diperbarui belakangan (async)

```
Aplikasi → tulis data
              ↓
    ┌─────────────────┐
    │   Cache (cepat) │
    └─────────────────┘
              ↓ (async, beberapa detik/menit kemudian)
             DB
```

```python
def update_product(product_id, new_data):
    # Tulis ke cache dulu — cepat!
    cache.set(f"product:{product_id}", new_data)

    # Tandai sebagai "dirty" (perlu disync ke DB)
    dirty_queue.push({"id": product_id, "data": new_data})

# Background worker yang jalan terpisah:
def sync_to_db():
    while True:
        item = dirty_queue.pop()
        db.update("products", item["id"], item["data"])
```

- ✅ Write sangat cepat (hanya ke cache)
- ✅ Bisa batch write ke DB → efisien
- ❌ **Risiko data loss** jika cache mati sebelum sync ke DB
- ❌ Kompleksitas tinggi

**Cocok untuk:** High write throughput, data yang boleh sedikit delay — misalnya view count, analytics, game score.

---

### Write-Around
> Tulis **langsung ke DB**, bypass cache

```
Aplikasi → tulis data → DB (langsung)
                        Cache TIDAK diupdate
```

```python
def create_log(log_data):
    # Log ditulis langsung ke DB, tidak ke cache
    db.insert("logs", log_data)
    # Cache tidak disentuh sama sekali
```

- ✅ Cache tidak kotor dengan data yang mungkin tidak dibaca
- ❌ Read pertama setelah write akan selalu cache miss

**Cocok untuk:** Data yang ditulis sekali tapi jarang dibaca — misalnya log, audit trail, data historis.

---

### Perbandingan Write Strategies:

```
                Write Speed   Konsistensi   Risk of Data Loss
Write-Through   Lambat        Tinggi        Rendah
Write-Back      Cepat         Rendah        TINGGI ⚠️
Write-Around    Sedang        Sedang        Rendah
```

---

## 8. Cache Stampede / Thundering Herd

Ini adalah **masalah klasik** yang sering tidak diperhatikan pemula.

### Skenario:

```
Cache untuk "trending_products" → TTL 60 detik

Detik ke-60: TTL habis → cache expired

Detik ke-61: 500 request datang BERSAMAAN
  → Semua miss (cache kosong)
  → Semua langsung hit DB
  → DB collapse! 💥
```

Itulah **Cache Stampede** — banyak request menyerbu sumber asli secara bersamaan saat cache expired.

---

### Solusi 1: Locking / Mutex
```python
import threading

lock = threading.Lock()

def get_trending_products():
    cached = cache.get("trending_products")
    if cached:
        return cached  # hit, langsung return

    # Miss → hanya SATU thread yang boleh query DB
    with lock:
        # Cek lagi setelah dapat lock
        # (mungkin thread lain sudah isi cache)
        cached = cache.get("trending_products")
        if cached:
            return cached

        # Benar-benar kosong → query DB
        data = db.query("SELECT * FROM products ORDER BY views DESC")
        cache.set("trending_products", data, ttl=60)
        return data

# Thread lain yang menunggu lock → setelah lock dilepas,
# cache sudah terisi → langsung return dari cache
```

---

### Solusi 2: Probabilistic Early Expiration
> Perbarui cache **sebelum** TTL benar-benar habis

```python
import math, random, time

def get_with_early_expiry(key, beta=1.0):
    item = cache.get_with_metadata(key)
    if item is None:
        return None

    ttl_remaining = item["expires_at"] - time.time()
    delta = item["compute_time"]  # berapa lama hitung datanya

    # Hitung apakah perlu early refresh
    # Semakin dekat expired, semakin besar probabilitas refresh
    if -delta * beta * math.log(random.random()) >= ttl_remaining:
        return None  # pura-pura miss → refresh lebih awal

    return item["value"]
```

---

### Solusi 3: Stale-While-Revalidate
> Kembalikan data lama (stale) dulu, perbarui di background

```python
def get_trending_products():
    item = cache.get_with_metadata("trending_products")

    if item is None:
        # Benar-benar kosong → harus query DB
        data = db.query("...")
        cache.set("trending_products", data, ttl=60)
        return data

    if item["is_stale"]:
        # Data sudah expired tapi masih ada
        # → Kembalikan data lama dulu (cepat!)
        # → Refresh di background (tidak blocking)
        threading.Thread(target=refresh_cache).start()
        return item["value"]  # return stale data

    return item["value"]
```

- ✅ User tidak menunggu
- ✅ DB tidak diserbu bersamaan
- ❌ User sesekali mendapat data yang sedikit stale

**Ini adalah strategi yang dipakai HTTP Cache (header `stale-while-revalidate`).**

---

## ✅ Ringkasan Fase 2

```
Eviction Policy → siapa yang dibuang saat cache penuh
  LRU  → buang yang paling lama tidak diakses (paling umum)
  LFU  → buang yang paling jarang diakses
  FIFO → buang yang pertama masuk

Cache Invalidation → cara menjaga cache tetap sinkron
  TTL-based   → otomatis expired (sederhana)
  Event-based → hapus saat data berubah (akurat)

Write Strategy → kapan cache diperbarui saat menulis
  Write-Through  → tulis ke cache & DB bersamaan (konsisten)
  Write-Back     → tulis ke cache dulu, DB belakangan (cepat, risky)
  Write-Around   → bypass cache, langsung ke DB (untuk data jarang dibaca)

Cache Stampede → banyak request menyerbu DB saat cache expired
  Solusi: Locking, Early Expiration, Stale-While-Revalidate
```

---

Fase 2 selesai! Kamu sekarang sudah paham cara kerja internal cache secara mendalam.

Siap lanjut ke **Fase 3** — cache di dunia nyata: Redis, HTTP Cache, dan Database Cache? 🚀