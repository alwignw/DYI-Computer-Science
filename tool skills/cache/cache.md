# Cache

Cache adalah **mekanisme penyimpanan sementara** yang menyimpan data atau hasil komputasi agar bisa diakses lebih cepat di masa mendatang, tanpa perlu mengambil atau menghitung ulang dari sumber aslinya.

---

## Konsep Dasar

Prinsip utamanya sederhana: **daripada melakukan pekerjaan yang sama berulang kali, simpan hasilnya dan gunakan kembali.**

Analogi: Bayangkan kamu sering membuka buku resep yang sama. Daripada selalu bolak-balik ke rak buku, kamu fotokopi halaman yang sering dipakai dan taruh di meja dapur — itulah cache.

---

## Mengapa Cache Penting?

| Masalah | Solusi Cache |
|--------|-------------|
| Akses memori utama lambat | CPU Cache menyimpan data di dekat prosesor |
| Query database berulang | Database cache menyimpan hasil query |
| Download aset web berulang | Browser cache menyimpan file lokal |
| Komputasi berat berulang | Memoization menyimpan hasil fungsi |

---

## Jenis-Jenis Cache

### 1. CPU Cache (Hardware Cache)
Cache yang berada di dalam atau sangat dekat dengan prosesor.

- **L1 Cache** — Tercepat, terkecil (~32–64 KB), ada di dalam core CPU
- **L2 Cache** — Lebih besar (~256 KB – 1 MB), sedikit lebih lambat
- **L3 Cache** — Terbesar (~4–64 MB), dibagi antar core, lebih lambat dari L1/L2

Hierarki aksesnya: CPU → L1 → L2 → L3 → RAM → Storage

### 2. Browser Cache
Menyimpan file web (HTML, CSS, JS, gambar) di perangkat lokal pengguna. Saat kamu membuka situs yang sama, browser memuat file lokal alih-alih mengunduh ulang dari server.

### 3. Database Cache
- **Query Cache** — Menyimpan hasil query SQL yang sering dijalankan
- **Object Cache** — Menyimpan objek/data hasil query (Redis, Memcached)

### 4. Application Cache / Memoization
Di level kode, menyimpan hasil fungsi berdasarkan input-nya:
```python
from functools import lru_cache

@lru_cache(maxsize=128)
def hitung_fibonacci(n):
    if n < 2:
        return n
    return hitung_fibonacci(n-1) + hitung_fibonacci(n-2)
```

### 5. CDN Cache (Content Delivery Network)
Server cache yang tersebar secara geografis. Konten disimpan di server yang dekat dengan pengguna untuk mengurangi latensi.

### 6. DNS Cache
Menyimpan hasil resolusi nama domain (misal: `google.com` → `142.250.x.x`) agar tidak perlu query DNS server setiap saat.

---

## Cara Kerja Cache

```
Permintaan Data
      ↓
 Cache Hit? ──── YA ──→ Kembalikan data dari cache ✅
      │
      NO
      ↓
 Ambil dari sumber asli (DB, server, disk)
      ↓
 Simpan ke cache
      ↓
 Kembalikan data ke pengguna
```

- **Cache Hit** — Data ditemukan di cache → cepat ✅
- **Cache Miss** — Data tidak ada di cache → ambil dari sumber → lebih lambat ⚠️

**Hit Rate** = (Cache Hit / Total Request) × 100%
Semakin tinggi hit rate, semakin efektif cache-nya.

---

## Strategi Penggantian Cache (Eviction Policy)

Cache punya kapasitas terbatas. Ketika penuh, data lama harus diganti:

| Strategi | Kepanjangan | Cara Kerja |
|---------|------------|-----------|
| **LRU** | Least Recently Used | Buang data yang paling lama tidak diakses |
| **LFU** | Least Frequently Used | Buang data yang paling jarang diakses |
| **FIFO** | First In First Out | Buang data yang pertama kali masuk |
| **MRU** | Most Recently Used | Buang data yang paling baru diakses |
| **Random** | — | Buang data secara acak |

LRU adalah yang paling umum digunakan.

---

## Cache Invalidation

Salah satu masalah paling sulit dalam pemrograman: **kapan cache harus dihapus/diperbarui?**

Ada beberapa pendekatan:

- **TTL (Time To Live)** — Cache otomatis kadaluarsa setelah waktu tertentu
- **Write-Through** — Setiap penulisan data langsung update cache dan sumber
- **Write-Back (Write-Behind)** — Tulis ke cache dulu, sinkron ke sumber belakangan
- **Cache-Aside (Lazy Loading)** — Aplikasi sendiri yang mengelola cache secara manual
- **Event-based** — Cache dihapus saat ada event tertentu (misalnya data diupdate)

> *"There are only two hard things in Computer Science: cache invalidation and naming things."*
> — Phil Karlton

---

## Keuntungan & Kerugian Cache

### ✅ Keuntungan
- Performa jauh lebih cepat
- Mengurangi beban server/database
- Menghemat bandwidth
- Meningkatkan skalabilitas

### ❌ Kerugian
- Data bisa **stale** (usang/tidak up-to-date)
- Menambah kompleksitas sistem
- Butuh memori tambahan
- Cache invalidation sulit dikelola

---

## Contoh Nyata dalam Kehidupan Sehari-hari

- **YouTube/Netflix** — Video di-buffer/cache lokal saat diputar
- **Google Maps** — Peta area tertentu di-cache di HP
- **Instagram/TikTok** — Feed di-cache sementara agar scroll tetap mulus
- **OS Windows/macOS** — File yang sering diakses di-cache di RAM

---

Ada aspek cache tertentu yang ingin kamu pelajari lebih dalam? Misalnya implementasi Redis, CPU cache architecture, atau strategi caching di web development?