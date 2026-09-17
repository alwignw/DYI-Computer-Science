Oke, langsung masuk Fase 2!

---

## Fase 2 — Distribusi & Caching

### 1. TTL (Time To Live)

TTL adalah angka yang menentukan **berapa lama sebuah file boleh tersimpan di cache CDN** sebelum edge server harus mengambil versi terbaru dari origin server.

Misalnya kamu set TTL = 3600 detik (1 jam), artinya:
- Edge server menyimpan file itu selama 1 jam
- Selama 1 jam, semua request dijawab dari cache tanpa menyentuh origin
- Setelah 1 jam habis, request berikutnya akan ke origin untuk mengambil versi terbaru, lalu disimpan lagi ke cache

Semakin panjang TTL → makin efisien (origin jarang disentuh), tapi berisiko menyajikan konten yang sudah usang. Semakin pendek TTL → konten selalu fresh, tapi cache kurang efektif.

---

### 2. Cache Invalidation

Masalah: bagaimana kalau kamu update file sebelum TTL habis? Cache di edge server masih menyimpan versi lama.

Di sinilah **cache invalidation** masuk — yaitu proses memaksa CDN membuang cache lama sebelum TTL-nya habis. Ada beberapa caranya:

**Purge by URL** — hapus cache untuk satu file spesifik. Misalnya kamu update logo, kamu purge hanya `https://domain.com/logo.png`. Cara paling presisi dan umum digunakan.

**Purge by tag/prefix** — beberapa CDN mendukung penghapusan cache secara massal berdasarkan tag atau prefix URL. Berguna kalau satu perubahan mempengaruhi banyak file sekaligus.

**Purge all** — hapus seluruh cache. Efektif tapi "mahal" karena setelah ini semua request akan cache miss dan menghantam origin secara bersamaan. Harus digunakan dengan hati-hati pada traffic tinggi.

**Cache busting** — pendekatan alternatif yang tidak memerlukan purge sama sekali. Caranya dengan mengubah nama file setiap kali ada update, biasanya dengan menambahkan versi atau hash ke nama file:

```
/assets/style.v3.css
/assets/app.a3f9b2.js
```

Karena nama file berubah, CDN menganggapnya sebagai file baru dan langsung mengambil dari origin. Cara ini sangat populer di dunia frontend modern — hampir semua build tool seperti Webpack dan Vite melakukan ini secara otomatis.

---

### 3. Cache-Control Headers

Ini adalah mekanisme standar HTTP yang digunakan untuk mengontrol perilaku cache, baik di CDN maupun di browser pengguna. Kamu set header ini di response dari origin server, lalu CDN dan browser akan mengikutinya.

Beberapa directive yang paling penting:

**`max-age=N`** — konten boleh di-cache selama N detik. Berlaku untuk browser maupun CDN.

```
Cache-Control: max-age=86400
```

**`s-maxage=N`** — sama seperti max-age, tapi khusus untuk shared cache seperti CDN. Jika keduanya ada, CDN akan mengikuti s-maxage, browser mengikuti max-age. Ini berguna kalau kamu mau cache di CDN lebih lama dari cache di browser.

```
Cache-Control: max-age=300, s-maxage=86400
```

Artinya: browser cache 5 menit, CDN cache 24 jam.

**`no-cache`** — konten tidak boleh langsung disajikan dari cache tanpa validasi dulu ke origin. Sering disalahartikan sebagai "jangan cache sama sekali" — padahal sebenarnya file tetap disimpan, tapi setiap request harus dikonfirmasi ke origin apakah versi cache masih valid (via ETag atau Last-Modified).

**`no-store`** — ini yang benar-benar melarang penyimpanan cache. Tidak ada file yang tersimpan di manapun. Digunakan untuk data sangat sensitif seperti respons banking atau data medis.

**`public`** — menyatakan bahwa response ini boleh di-cache oleh siapapun, termasuk CDN. Biasanya tidak perlu ditulis eksplisit karena CDN sudah mengasumsikan ini untuk konten statis.

**`private`** — response ini hanya boleh di-cache di browser pengguna, tidak boleh di CDN. Digunakan untuk halaman yang personalized, misalnya dashboard setelah login.

```
Cache-Control: private, max-age=300
```

---

### 4. Static vs Dynamic Caching — apa yang boleh dan tidak boleh di-cache

Ini keputusan arsitektural yang sangat penting dan sering jadi sumber masalah kalau salah.

**Konten yang aman di-cache (static):**
- File gambar, video, font
- CSS dan JavaScript (apalagi kalau sudah pakai cache busting)
- File HTML yang isinya sama untuk semua pengguna
- File download seperti PDF atau installer

**Konten yang tidak boleh di-cache atau perlu penanganan khusus (dynamic):**
- Halaman setelah login yang menampilkan data personal
- Response API yang berisi data real-time seperti harga saham atau stok barang
- Halaman checkout dan transaksi
- Apapun yang bergantung pada cookie session pengguna

Yang sering menjadi jebakan adalah **konten semi-dynamic** — misalnya halaman beranda yang sebagian besar sama untuk semua orang, tapi ada bagian kecil yang personalized (nama pengguna di pojok kanan atas). Solusi arsitekturalnya ada beberapa:

Pertama, **edge-side includes (ESI)** — halaman di-cache di CDN, tapi bagian yang personalized di-fetch secara terpisah. Tidak semua CDN mendukung ini.

Kedua, **fragment caching** — cache hanya bagian konten yang statis, bagian dinamis tetap dari origin.

Ketiga, yang paling umum dan simpel: **pisahkan API call**. Cache halaman HTML-nya, tapi data personal diambil via JavaScript ke API terpisah yang tidak di-cache. Ini yang dilakukan hampir semua SPA (Single Page Application) modern.

---

### Ringkasan Fase 2

| Konsep | Intinya |
|--------|---------|
| TTL | Berapa lama cache disimpan sebelum diperbarui |
| Cache invalidation | Cara memaksa cache lama dibuang sebelum TTL habis |
| Cache-Control headers | Header HTTP yang mengatur perilaku cache secara presisi |
| Static vs dynamic | Keputusan apa yang boleh di-cache dan bagaimana menangani yang tidak boleh |

Sudah nangkep semuanya? Kalau ada yang mau digali lebih dalam sebelum lanjut ke Fase 3, tanyain aja.