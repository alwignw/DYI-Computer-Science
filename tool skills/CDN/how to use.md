Pertanyaan yang bagus! Intinya, kamu tidak perlu memindahkan apapun dari servermu. Kamu cukup mengubah **siapa yang menjawab request DNS domain-mu**. Berikut alur dan langkah-langkahnya.## Langkah-langkah detail pasang Cloudflare

### Langkah 1 — Daftar akun Cloudflare

Buka [cloudflare.com](https://cloudflare.com) dan buat akun gratis. Plan Free sudah mencakup CDN, DDoS protection, dan SSL — lebih dari cukup untuk kebanyakan website.

---

### Langkah 2 — Tambahkan domain kamu

Setelah login, klik "Add a Site" dan masukkan nama domain (misal `namadomain.com`). Cloudflare akan otomatis membaca DNS records yang sudah ada dari registrar kamu — proses ini biasanya hanya beberapa detik.

---

### Langkah 3 — Ganti Nameserver di registrar domain (ini inti utamanya)

Cloudflare akan memberikan dua nameserver miliknya, contoh:

```
ava.ns.cloudflare.com
bob.ns.cloudflare.com
```

Kamu perlu login ke **tempat kamu beli domain** (Niagahoster, Namecheap, GoDaddy, dll.) dan ganti nameserver lama dengan dua nameserver dari Cloudflare di atas. Proses propagasi DNS biasanya 5 menit hingga 48 jam — tapi sering langsung aktif dalam hitungan menit.

> Penting: servermu sendiri tidak perlu disentuh sama sekali. IP address server tetap sama, tidak ada yang berubah di sana.

---

### Langkah 4 — Aktifkan "Proxy" (orange cloud)

Di dashboard DNS Cloudflare, pastikan setiap A record atau CNAME yang mengarah ke servermu dalam status **proxy aktif** (ikon awan oranye). Ini yang membuat traffic melewati Cloudflare:

| Status | Ikon | Artinya |
|--------|------|---------|
| Proxy aktif | awan oranye | Traffic lewat Cloudflare (CDN + proteksi aktif) |
| DNS only | awan abu-abu | Cloudflare hanya jadi DNS resolver, tidak ada CDN |

---

## Yang terjadi setelah aktif

Cloudflare menjadi "pintu depan" websitemu. Pengguna tidak pernah langsung menyentuh server aslimu — mereka bicara ke edge server Cloudflare yang paling dekat. Cloudflare kemudian meneruskan request ke servermu hanya ketika konten tidak ada di cache (cache miss).

Selain CDN, kamu juga otomatis dapat SSL gratis (HTTPS), perlindungan DDoS dasar, dan analitik traffic — semuanya tanpa perlu install apapun di servermu.