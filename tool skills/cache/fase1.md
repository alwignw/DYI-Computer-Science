# Fase 1 — Fondasi Cache

Kita mulai dari akar masalahnya dulu. Bukan langsung "apa itu cache", tapi **"kenapa cache perlu ada?"**

---

## 1. Masalah yang Diselesaikan Cache

### Bayangkan skenario ini:

Kamu punya aplikasi yang setiap request menjalankan query ini:

```sql
SELECT * FROM products WHERE category = 'electronics' ORDER BY rating DESC LIMIT 20;
```

Query ini:
- Dijalankan **10.000 kali per menit**
- Hasilnya **hampir tidak pernah berubah**
- Butuh **200ms** setiap kali dijalankan

Tanpa cache → database kamu kerja keras untuk hal yang sama terus-menerus.

Dengan cache → jalankan sekali, simpan hasilnya, pakai ulang → **turun jadi 1ms**.

---

### Tiga masalah utama yang diselesaikan cache:

**🐢 Latency** — Akses data dari sumber asli (disk, network, DB) itu lambat.
```
RAM      →  ~100 nanosecond
SSD      →  ~100 microsecond  (1.000x lebih lambat dari RAM)
HDD      →  ~10 millisecond   (100.000x lebih lambat dari RAM)
Network  →  ~100 millisecond  (bisa lebih tergantung jarak)
```

**💥 Throughput** — Sumber data punya batas kapasitas. Database tidak bisa melayani unlimited request sekaligus.

**🔁 Redundant computation** — Menghitung hal yang sama berulang kali itu buang-buang CPU.

---

## 2. Lokalitas Data — *Kenapa Cache Bisa Bekerja*

Ini adalah **alasan fundamental** mengapa cache efektif. Kalau tidak ada lokalitas, cache tidak akan berguna sama sekali.

Ada dua jenis lokalitas:

---

### 🕐 Temporal Locality
> *"Data yang baru diakses, kemungkinan besar akan diakses lagi dalam waktu dekat."*

**Contoh nyata:**
```python
# User login → profil mereka diambil
user = db.get_user(user_id)

# Lalu di halaman berikutnya... profil diambil lagi
user = db.get_user(user_id)  # data yang SAMA!

# Dan lagi di halaman checkout...
user = db.get_user(user_id)  # data yang SAMA lagi!
```

Karena pola ini **sangat umum**, menyimpan `user` di cache setelah pertama kali diambil adalah keputusan yang masuk akal.

---

### 📦 Spatial Locality
> *"Data yang berada 'berdekatan' dengan data yang diakses, kemungkinan besar juga akan segera diakses."*

**Contoh nyata:**
```python
# Kamu akses artikel blog dengan id = 42
article = db.get_article(42)

# Kemungkinan besar berikutnya kamu akses:
comments = db.get_comments(article_id=42)  # data yang "berdekatan"
author   = db.get_user(article.author_id)  # data yang "berdekatan"
tags     = db.get_tags(article_id=42)      # data yang "berdekatan"
```

Inilah kenapa banyak sistem cache **sekaligus menyimpan data terkait** — bukan hanya data yang diminta.

---

### Gabungan keduanya dalam kehidupan nyata:

```
User buka halaman produk
  → Temporal: produk yang sama dibuka berkali-kali (trending item)
  → Spatial:  produk → review → seller info → related products
```

Tanpa kedua prinsip ini, cache hanya akan buang-buang memori karena data yang disimpan tidak pernah dipakai ulang.

---

## 3. Cache Hit vs Miss

Sekarang kita masuk ke mekanisme dasarnya.

```
Request masuk
     ↓
┌─────────────────┐
│   Cek Cache     │
└─────────────────┘
     ↓          ↓
  HIT ✅      MISS ❌
     ↓          ↓
Ambil dari    Ambil dari
  cache       sumber asli
                 ↓
            Simpan ke cache
                 ↓
            Kembalikan data
```

### Cache Hit ✅
Data **ditemukan** di cache. Langsung dikembalikan. Cepat.

### Cache Miss ❌
Data **tidak ada** di cache. Harus ke sumber asli. Ada tiga jenis miss:

| Jenis Miss | Penjelasan | Contoh |
|-----------|-----------|--------|
| **Cold Miss** | Cache masih kosong, belum pernah diisi | Aplikasi baru restart |
| **Capacity Miss** | Cache penuh, data lama terpaksa dibuang | Cache terlalu kecil |
| **Conflict Miss** | Data ada tapi tertimpa data lain | Hash collision di cache |

### Hit Rate — Metrik paling penting:

```
Hit Rate = (Cache Hit / Total Request) × 100%

Contoh:
- 1.000 request masuk
- 850 hit, 150 miss
- Hit Rate = 850/1000 × 100% = 85%
```

**Berapa hit rate yang bagus?**
- < 70% → cache kurang efektif, perlu evaluasi
- 70–90% → cukup baik
- \> 90% → sangat baik
- ~99%+ → excellent (untuk use case tertentu seperti CDN)

---

## 4. Anatomi Cache — Struktur Dasarnya

Cache pada dasarnya adalah **key-value store**:

```
┌─────────────────────────────────────────────┐
│                  CACHE                       │
├──────────────────┬──────────────────┬────────┤
│       KEY        │      VALUE       │  TTL   │
├──────────────────┼──────────────────┼────────┤
│ "user:123"       │ {name:"Budi"...} │ 300s   │
│ "product:456"    │ {name:"Laptop"}  │ 3600s  │
│ "trending:posts" │ [id1, id2, id3]  │ 60s    │
└──────────────────┴──────────────────┴────────┘
```

- **Key** — Identifikasi unik untuk data. Biasanya string yang deskriptif.
- **Value** — Data yang disimpan. Bisa apa saja: string, object, list, dll.
- **TTL (Time To Live)** — Berapa lama cache valid sebelum kadaluarsa.

### Contoh implementasi sederhana di Python:

```python
import time

class SimpleCache:
    def __init__(self):
        self.store = {}

    def set(self, key, value, ttl=60):
        self.store[key] = {
            "value": value,
            "expires_at": time.time() + ttl
        }

    def get(self, key):
        item = self.store.get(key)

        if item is None:
            return None  # Cache miss

        if time.time() > item["expires_at"]:
            del self.store[key]
            return None  # Expired → cache miss

        return item["value"]  # Cache hit ✅

# Penggunaan:
cache = SimpleCache()

def get_user(user_id):
    key = f"user:{user_id}"

    # Cek cache dulu
    cached = cache.get(key)
    if cached:
        print("Cache HIT")
        return cached

    # Cache miss → ambil dari DB
    print("Cache MISS → query DB")
    user = db.query(f"SELECT * FROM users WHERE id = {user_id}")

    # Simpan ke cache dengan TTL 5 menit
    cache.set(key, user, ttl=300)
    return user
```

### Kenapa TTL penting?

TTL menjawab pertanyaan: **"Berapa lama data ini masih relevan?"**

```
Data profil user      → TTL lama  (jarang berubah)     → 1 jam
Harga produk          → TTL sedang (kadang berubah)    → 5 menit
Notifikasi real-time  → TTL pendek (sering berubah)    → 10 detik
Data live score bola  → Jangan di-cache / TTL sangat pendek
```

---

## ✅ Ringkasan Fase 1

```
Cache ada karena:
  1. Akses sumber asli itu LAMBAT & TERBATAS
  2. Data punya pola LOKALITAS (temporal & spatial)
     → Data yang sama sering diakses ulang
     → Data yang berdekatan sering diakses bersama

Cara kerjanya:
  - Simpan data dengan KEY → VALUE → TTL
  - Kalau ada di cache = HIT (cepat ✅)
  - Kalau tidak ada    = MISS (ambil dari sumber, simpan ke cache)

Ukuran keberhasilan:
  - Hit Rate → semakin tinggi semakin baik
```

---

Fase 1 selesai! Kamu sudah punya **fondasi yang kuat**.

Siap lanjut ke **Fase 2** — masuk ke cara kerja internal: eviction policy, cache invalidation, dan write strategies? Atau ada yang mau didalami dulu dari Fase 1?