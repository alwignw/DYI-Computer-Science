# Fase 3 — Cache di Dunia Nyata

Sekarang kita lihat bagaimana konsep dari Fase 1 & 2 diterapkan di berbagai layer sistem nyata.

---

## 9. In-Memory Cache & Memoization

Ini adalah cache yang hidup **di dalam proses aplikasi kamu** — paling sederhana, paling cepat, tapi tidak shared antar server.

### Memoization — Cache di Level Fungsi

```python
# Tanpa memoization → dihitung ulang setiap kali
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(40)  # lambat, hitung berulang-ulang

# ─────────────────────────────────────────

# Dengan memoization → hasil disimpan
from functools import lru_cache

@lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

fibonacci(40)  # cepat, hasil sebelumnya dipakai ulang
```

### Kapan pakai in-memory cache?

```
✅ Cocok untuk:
  - Data yang sama dipakai berulang dalam satu request
  - Komputasi berat (parsing, kalkulasi, transformasi)
  - Single server / tidak butuh share antar instance

❌ Tidak cocok untuk:
  - Multi-server (setiap server punya cache sendiri → tidak konsisten)
  - Data yang harus persist saat server restart
  - Cache yang butuh diakses dari service lain
```

---

## 10. Application-Level Cache — Redis & Memcached

Ini adalah **cache yang berdiri sendiri sebagai server terpisah** — bisa diakses oleh banyak instance aplikasi sekaligus.

### Arsitektur:

```
  App Server 1 ──┐
                 ├──→ Redis Server ──→ DB
  App Server 2 ──┘

Semua app server share cache yang sama ✅
```

---

### Redis — Yang Paling Populer

Redis (Remote Dictionary Server) adalah **in-memory data store** yang bisa dipakai sebagai cache, message broker, dan database.

**Tipe data yang didukung Redis:**
```
String  → nilai tunggal
Hash    → mirip object/dict
List    → ordered list
Set     → unordered, unique values
ZSet    → sorted set (ada score-nya)
```

**Operasi dasar Redis:**
```bash
# Set nilai dengan TTL
SET user:123 '{"name":"Budi","email":"budi@email.com"}' EX 300

# Get nilai
GET user:123

# Hapus key
DEL user:123

# Cek TTL yang tersisa
TTL user:123

# Set hanya jika key belum ada (untuk locking)
SET lock:product:456 "1" NX EX 30
```

**Pakai Redis dari Python:**
```python
import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

def get_user(user_id):
    key = f"user:{user_id}"

    # Cek cache
    cached = r.get(key)
    if cached:
        print("Cache HIT")
        return json.loads(cached)

    # Cache miss → query DB
    print("Cache MISS")
    user = db.query(f"SELECT * FROM users WHERE id = {user_id}")

    # Simpan ke Redis dengan TTL 5 menit
    r.setex(key, 300, json.dumps(user))
    return user

def update_user(user_id, new_data):
    # Update DB
    db.update("users", user_id, new_data)

    # Invalidate cache (event-based)
    r.delete(f"user:{user_id}")
```

---

### Redis vs Memcached:

| | Redis | Memcached |
|--|-------|-----------|
| Tipe data | String, Hash, List, Set, ZSet | String saja |
| Persistensi | ✅ Bisa disimpan ke disk | ❌ Pure in-memory |
| Replikasi | ✅ Master-replica | ❌ Tidak ada |
| Clustering | ✅ Redis Cluster | ✅ Built-in |
| Lua scripting | ✅ | ❌ |
| Kecepatan | Sangat cepat | Sangat cepat |
| Use case | General purpose | Simple caching saja |

**Kesimpulan:** Pakai Redis hampir selalu. Memcached hanya kalau kamu butuh pure simplicity dan sudah punya legacy system.

---

### Pola Umum dengan Redis:

**Cache-Aside (paling umum):**
```python
def get_product(product_id):
    # 1. Cek cache dulu
    cached = r.get(f"product:{product_id}")
    if cached:
        return json.loads(cached)

    # 2. Miss → ambil dari DB
    product = db.find("products", product_id)

    # 3. Simpan ke cache
    r.setex(f"product:{product_id}", 3600, json.dumps(product))

    return product
```

**Menyimpan List/Counter:**
```python
# Increment view count (atomic!)
r.incr(f"views:product:{product_id}")

# Simpan top 10 produk sebagai sorted set
r.zadd("trending", {product_id: score})
top10 = r.zrevrange("trending", 0, 9)  # ambil 10 teratas
```

---

## 11. HTTP Cache — Cache di Level Web

Ini adalah cache yang bekerja di level protokol HTTP — antara browser, CDN, dan server kamu.

### Siapa yang bisa cache HTTP response?

```
Browser → Proxy/CDN → Origin Server

Setiap layer bisa menyimpan cache response
```

### Header HTTP Cache yang Penting:

**Cache-Control — Raja dari semua header cache:**
```http
# Response dari server:
Cache-Control: max-age=3600          → cache valid 1 jam
Cache-Control: no-cache              → harus validasi ke server sebelum pakai
Cache-Control: no-store              → jangan cache sama sekali
Cache-Control: private               → hanya browser yang boleh cache (bukan CDN)
Cache-Control: public                → siapa saja boleh cache (CDN included)
Cache-Control: stale-while-revalidate=60  → boleh pakai stale 60 detik sambil refresh
```

**ETag — Validasi berbasis fingerprint:**
```http
# Server kirim ETag (hash dari konten)
Response: ETag: "abc123"

# Browser request berikutnya:
Request: If-None-Match: "abc123"

# Kalau konten tidak berubah:
Response: 304 Not Modified  ← tidak perlu kirim body lagi!

# Kalau konten berubah:
Response: 200 OK + body baru + ETag: "xyz789"
```

**Last-Modified — Validasi berbasis waktu:**
```http
# Server:
Response: Last-Modified: Wed, 17 Sep 2026 10:00:00 GMT

# Browser:
Request: If-Modified-Since: Wed, 17 Sep 2026 10:00:00 GMT

# Tidak berubah:
Response: 304 Not Modified
```

---

### Alur HTTP Cache secara lengkap:

```
Browser request GET /products/123
        ↓
Cek browser cache
        ↓
  Ada & belum expired?
  ─── YES → return dari cache (tanpa ke server) ✅
  ─── NO  → kirim request ke server
               ↓
        Ada ETag/Last-Modified?
        ─── YES → kirim conditional request
                     ↓
              Server cek: berubah?
              ─── NO  → 304 Not Modified (hemat bandwidth!)
              ─── YES → 200 + data baru
        ─── NO  → request normal → 200 + data
```

---

### Contoh implementasi di backend (Go):

```go
func getProductHandler(w http.ResponseWriter, r *http.Request) {
    productID := r.URL.Query().Get("id")
    product := db.GetProduct(productID)

    // Generate ETag dari data
    etag := generateHash(product)

    // Cek apakah client punya versi yang sama
    if r.Header.Get("If-None-Match") == etag {
        w.WriteHeader(http.StatusNotModified)  // 304
        return
    }

    // Set cache headers
    w.Header().Set("Cache-Control", "public, max-age=3600")
    w.Header().Set("ETag", etag)

    json.NewEncoder(w).Encode(product)
}
```

---

### Strategi per tipe konten:

```
Tipe Konten           Cache-Control                  Alasan
──────────────────────────────────────────────────────────────
HTML halaman          no-cache                       Selalu validasi
CSS/JS (dengan hash)  max-age=31536000, immutable    Tidak pernah berubah
Gambar produk         public, max-age=86400          Jarang berubah
API user data         private, max-age=300           Per user, 5 menit
API public data       public, max-age=60             Boleh di-cache CDN
Real-time data        no-store                       Jangan cache
```

---

## 12. Database Cache — Cache di Level DB

### Query Result Cache

Beberapa database punya built-in query cache, tapi cara yang lebih umum adalah **cache di layer aplikasi** sebelum query sampai ke DB.

```python
def get_products_by_category(category, page=1):
    cache_key = f"products:category:{category}:page:{page}"

    # Cek cache
    cached = r.get(cache_key)
    if cached:
        return json.loads(cached)

    # Query DB
    products = db.query("""
        SELECT * FROM products
        WHERE category = %s
        ORDER BY rating DESC
        LIMIT 20 OFFSET %s
    """, (category, (page-1) * 20))

    # Cache 10 menit
    r.setex(cache_key, 600, json.dumps(products))
    return products
```

---

### N+1 Problem & Cache Sebagai Solusi

Ini masalah klasik yang sering muncul:

```python
# ❌ N+1 Problem — 1 query untuk posts + N query untuk setiap author
posts = db.query("SELECT * FROM posts LIMIT 10")  # 1 query

for post in posts:
    # N query — satu per post!
    author = db.query(f"SELECT * FROM users WHERE id = {post.author_id}")
    post.author = author
```

**Solusi dengan cache:**
```python
def get_user_cached(user_id):
    key = f"user:{user_id}"
    cached = r.get(key)
    if cached:
        return json.loads(cached)
    user = db.query(f"SELECT * FROM users WHERE id = {user_id}")
    r.setex(key, 3600, json.dumps(user))
    return user

posts = db.query("SELECT * FROM posts LIMIT 10")

for post in posts:
    # Query ke DB hanya jika belum di-cache
    # Author yang sama tidak di-query ulang
    post.author = get_user_cached(post.author_id)
```

Tapi solusi terbaik tetap **JOIN atau batch loading** — cache hanya sebagai pelengkap.

---

### Connection Pool — Cache untuk Koneksi DB

Membuka koneksi baru ke DB itu mahal (butuh ~50–100ms). Connection pool **menyimpan/reuse koneksi yang sudah dibuka**.

```python
from sqlalchemy import create_engine

# Pool dengan max 20 koneksi
engine = create_engine(
    "postgresql://user:pass@localhost/db",
    pool_size=20,        # koneksi yang selalu siap
    max_overflow=10,     # koneksi extra saat traffic tinggi
    pool_timeout=30,     # berapa lama tunggu koneksi tersedia
    pool_recycle=3600    # recycle koneksi setiap 1 jam
)
```

```
Tanpa pool: setiap request → buka koneksi baru (50–100ms overhead)
Dengan pool: setiap request → ambil koneksi yang sudah ada (<1ms) ✅
```

---

## ✅ Ringkasan Fase 3

```
In-memory cache / Memoization
  → Tercepat, tapi tidak shared antar server
  → Pakai @lru_cache untuk fungsi Python

Redis (Application Cache)
  → Cache terpusat, shared semua server
  → Support berbagai tipe data
  → Operasi atomic (aman untuk counter, locking)

HTTP Cache
  → Cache-Control: atur siapa & berapa lama bisa cache
  → ETag: validasi berbasis fingerprint (hemat bandwidth)
  → Stale-while-revalidate: user tidak menunggu, refresh background

Database Cache
  → Cache query result di Redis sebelum sampai ke DB
  → Connection pool: reuse koneksi DB (bukan cache data, tapi prinsipnya sama)
```

---

### Gambaran besar semua layer cache dalam satu sistem:

```
User
  ↓
Browser Cache          ← HTTP Cache (Cache-Control, ETag)
  ↓ (miss)
CDN Cache              ← HTTP Cache di edge server
  ↓ (miss)
App Server
  ↓
In-Memory Cache        ← Memoization, local cache
  ↓ (miss)
Redis Cache            ← Application cache terpusat
  ↓ (miss)
Database               ← Query + Connection Pool
```

Semakin awal request bisa dijawab (semakin atas), semakin cepat dan murah.

---

Fase 3 selesai! Sekarang kamu sudah paham cache dari level kode sampai level infrastruktur.

Siap lanjut ke **Fase 4** — pola arsitektur cache, distributed cache, dan monitoring? 🚀