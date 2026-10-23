Pertama, jangan panik. Kamu punya waktu 3 hari, dan kamu tidak harus menjadi ahli bare-metal dalam waktu sesingkat itu. Targetmu adalah memahami arsitektur deployment, mempersiapkan checklist, memastikan semua akses tersedia, dan mengetahui kapan harus berhenti serta meminta bantuan senior.

Karena kamu akan men-deploy frontend (FE), backend (BE), dan database (DB) langsung ke server bare-metal di data center, ini bukan sekadar menjalankan aplikasi. Kamu juga harus memahami jaringan, sistem operasi, keamanan, penyimpanan, dan prosedur operasional server.

Satu hal penting: karena kamu masih baru di perusahaan, jangan merasa harus melakukan semuanya sendirian. Deployment ke server fisik perusahaan bisa berdampak ke layanan produksi. Meminta senior melakukan review sebelum perubahan penting adalah praktik profesional, bukan tanda kamu tidak mampu.

# 1. Pahami dulu apa yang akan kamu kerjakan

[신성씨앤에스 | B2B 전용 IT 솔루션·장비 공급](https://images.openai.com/static-rsc-4/3fLWrPxv2EzQI5sA3kqapoIiL-T3GNTc16xlQ9jaG1VV2WRrAGBLqd-33WSxOZpZX4bLH66a4yLJclPpNvjopZKGfTw09ngG1QRDoBMAh6u07zKW2V8iBpLhC1CMZN9SzL-Ksy8puh2dYAuP0Ca7X-RJQV_x0IZsSJgfrOg7O-Q?purpose=inline)

Bare-metal server

Server fisik yang menjalankan sistem operasi secara langsung, bukan sebagai virtual machine di atas hypervisor. Kamu mungkin akan mengelola Linux, storage, network interface, firewall, dan service aplikasi.

[Expert Computer & IT Services in Trivandrum |  Logtech- India's Largest Tech Store](https://images.openai.com/static-rsc-4/H5iJDO5jSauC47quKtxzR1jeOEXKc2lXZdATZtS_PlAr1PaD6yYGu7c2ojoP8Mz9VIGdsSYXMPzPwr07WxiRRYlJq0D7ewDaZ-ZueizcRPaQQ8UY634LRgFReD7x73bdzIVTH5r3INwZ6OGgAcn8W_c_3A6jfUSaGhovWaCUSn4?purpose=inline)

Data center

Tempat server ditempatkan, dengan infrastruktur listrik, pendinginan, jaringan, keamanan fisik, dan prosedur akses. Kamu perlu tahu siapa yang memberi akses, bagaimana mengakses server, dan siapa yang menangani masalah hardware.

Bayangkan arsitektur yang akan kamu deploy seperti ini:

User / Browser

Mengakses domain aplikasi

DNS / Firewall / Reverse Proxy

Routing, HTTPS, dan pembatasan akses

Frontend

Nginx atau web server untuk menyajikan UI

Backend API

Aplikasi, business logic, dan API

Database

Penyimpanan data persisten

Ilustrasi logis; FE, BE, dan DB bisa berada pada satu atau beberapa server fisik.

Perlu diperhatikan: diagram ini adalah arsitektur konseptual, bukan berarti kamu harus memasang semua komponen tersebut. Bisa saja perusahaan sudah menyediakan load balancer, reverse proxy, firewall, atau database server tersendiri.

Hal pertama yang harus kamu cari tahu adalah: apakah FE, BE, dan DB akan ditempatkan pada satu server fisik atau beberapa server? Ini memengaruhi desain jaringan, keamanan, deployment, dan recovery.

# 2. Roadmap belajar selama 3 hari

Jangan belajar semua hal tentang server. Prioritaskan hal yang langsung dibutuhkan untuk deployment.

HARI 1

## Pahami server dan infrastruktur

Fondasi

- Linux server dan SSH.
- IP address, subnet, gateway, DNS, port, routing.
- CPU, RAM, disk, filesystem, dan RAID.
- Memahami topologi server dan diagram deployment perusahaan.
- Memastikan akses VPN, SSH, akun, dan prosedur data center tersedia.

Target: kamu dapat menjelaskan server mana yang menjalankan FE, BE, dan DB serta bagaimana ketiganya berkomunikasi.

HARI 2

## Latihan deployment di Linux

Praktik

- Menjalankan aplikasi backend sebagai service.
- Build dan publish frontend.
- Memasang konfigurasi reverse proxy dan HTTPS sesuai desain perusahaan.
- Menghubungkan backend ke database.
- Membaca log, memeriksa port, dan menguji koneksi.
- Menguji backup serta prosedur restore di lingkungan latihan.

Target: aplikasi dapat dijalankan, diakses, dan diperiksa kondisinya tanpa bergantung pada terminal yang terus terbuka.

HARI 3

## Rehearsal dan persiapan produksi

Validasi

- Simulasikan deployment dari awal hingga akhir.
- Verifikasi firewall, port, DNS, sertifikat TLS, dan konfigurasi rahasia.
- Siapkan checklist pengujian FE, BE, dan DB.
- Siapkan rollback ke versi sebelumnya.
- Pastikan backup database bisa dipulihkan.
- Review rencana perubahan dengan senior atau PIC infrastruktur.

Target: kamu memiliki runbook tertulis dan tahu langkah berikutnya jika deployment gagal.

Kamu sudah pernah mempelajari konsep hypervisor dan bare-metal. Fondasi itu membantu, tetapi kali ini fokusnya adalah pengoperasian server fisik, jaringan nyata, dan deployment aplikasi.&#x20;

# 3. Materi teknis yang wajib kamu kuasai

## A. Linux server dan SSH

Kamu perlu nyaman bekerja melalui terminal. Pelajari perintah berikut dan pahami fungsinya sebelum menjalankannya di server perusahaan.

| Perintah                        | Kegunaan                                     |
| ------------------------------- | -------------------------------------------- |
| `hostnamectl`                   | Melihat identitas dan informasi OS server    |
| `ip addr`                       | Melihat interface dan alamat IP              |
| `ip route`                      | Melihat routing                              |
| `df -h`                         | Memeriksa kapasitas filesystem               |
| `free -h`                       | Memeriksa penggunaan RAM                     |
| `lsblk`                         | Melihat disk dan partisi                     |
| `systemctl status nama-service` | Memeriksa status service                     |
| `journalctl -u nama-service`    | Memeriksa log service                        |
| `ss -lntp`                      | Melihat port TCP yang sedang listen          |
| `uptime`                        | Melihat lama server menyala dan load average |

Latih perintah tersebut di VM Linux terlebih dahulu. Kamu tidak perlu menunggu sampai berada di data center untuk belajar.

Hal yang harus dipahami: SSH adalah jalur administrasi ke server, sedangkan aplikasi yang berjalan di server mempunyai port dan jalur jaringan tersendiri. Keduanya jangan disamakan.

## B. Jaringan dan firewall

Ini salah satu materi terpenting. Aplikasi bisa berjalan normal tetapi tetap tidak dapat diakses karena jaringan salah.

Pelajari konsep berikut:

- IP address dan subnet mask/CIDR.
- Default gateway dan routing.
- DNS dan resolusi nama domain.
- TCP versus UDP.
- Port dan proses yang listen.
- Firewall host dan firewall jaringan.
- NAT, reverse proxy, serta TLS/HTTPS.

Contoh arsitektur koneksi yang umum:

Client

HTTPS :443

Frontend / Reverse proxy

HTTP :80 atau HTTPS :443 sesuai konfigurasi

Backend API

Contoh: TCP :3000, jika memang dikonfigurasi begitu

Database

Contoh PostgreSQL: TCP :5432

Port adalah contoh, bukan instruksi untuk membuka semua port tersebut ke jaringan publik.

Idealnya, hanya layanan yang memang perlu diakses pengguna yang dibuka ke jaringan pengguna. Port database seharusnya hanya dapat diakses oleh backend dan jalur administrasi yang diizinkan.

## C. Deployment FE, BE, dan DB

[ezyrentalsweb](https://images.openai.com/static-rsc-4/uhsyx7u36VlC4YfmVFsOfDEMGoFwJL7D7GlGmEMmRfnES-AxrmbJLIHOXZ6fI-mhz0H6tG32hyaqeevA-IaMEBWMqRAsOe4nfF9uE2XVAuw-rihMuq4w9pHR6Hc5SwgLmefKWf0EUcOhnTTnT2GKAoYLL3u946MOXAxRdPiGE-c?purpose=inline)

Frontend (FE)

Pahami cara build aplikasi, lokasi hasil build, konfigurasi environment, URL API, routing SPA, serta penyajian file statis melalui web server atau metode deployment yang ditetapkan perusahaan.

[KiwisCAD | Browser-Based Arduino Circuit Design & Simulation](https://images.openai.com/static-rsc-4/gW_9bQTKtjkxjDwdmHHlra1gXhqTqWN-Ui6YC8Zau0TZljbuwV2yKq5cSKgJiD-vvlVWle5nTMH6neK_8UcLDfcZAzZwe_dg53n6kNJCfjMQowPvUzPdcrvSvGcMctHL4KLJbfHDj8ETHlRfDZFYd52_cE0u3S8SoD5o-oTvFLo?purpose=inline)

Backend (BE)

Pahami runtime yang diperlukan, versi bahasa dan dependensi, environment variables, koneksi DB, pengelolaan process/service, log, health check, serta cara restart yang aman.

[NETCOM’s Intern and Fellowship Programs Attracts New Talent | Article | The United States Army](https://images.openai.com/static-rsc-4/v44ZWCVuiTVS6hz3JrAHCqxLKAhtRCZx0QRG8r3dbGX_FcvZGnvP4AfW0hMXAGO95ajvsHY7zXprBoZoQUFV46iaZXa-F5czPUgMVTZCQUgRADPvGgpG-byAFDN-oZN4XvdsK2OZq8VcgV4uqfURp7MlscfmEGjDM9b2xvPpeYs?purpose=inline)

Database (DB)

Pahami versi DB, lokasi data persisten, user dan privilege, migrasi schema, koneksi, backup, restore, kapasitas disk, dan kompatibilitas versi aplikasi. Jangan menghapus atau menginisialisasi ulang database yang berisi data penting.

Satu detail yang sering terlewat: environment variable untuk frontend kadang dimasukkan saat proses build, bukan dibaca ketika server menjalankan file statis. Jadi, perubahan URL API belum tentu berlaku hanya dengan me-restart web server.

# 4. Apa yang harus kamu lakukan sebelum masuk data center?

Ini bagian yang tidak boleh kamu abaikan. Jangan sampai kamu sudah berada di depan server tetapi tidak tahu IP-nya, tidak memiliki akses, atau tidak tahu prosedur jika server gagal boot.

## Checklist yang perlu kamu konfirmasi ke senior

## Checklist persiapan

0/15 selesai

Akses dan tanggung jawab

Siapa PIC infrastruktur yang mendampingi deployment?

Apakah akses data center, VPN, SSH, dan akun sudah tersedia?

Apakah ada prosedur change approval dan maintenance window?

Server dan jaringan

Berapa server fisik yang akan digunakan dan apa fungsi masing-masing?

OS dan versinya apa? Apakah server sudah terinstal dan siap digunakan?

Berapa IP, subnet, gateway, DNS, VLAN, dan hostname yang ditetapkan?

Apakah firewall dan jalur jaringan ke DB sudah dikonfigurasi?

Aplikasi

Apa versi FE, BE, DB, runtime, dan dependency yang akan dipasang?

Bagaimana mekanisme deployment dan pengelolaan service yang ditetapkan perusahaan?

Di mana file konfigurasi dan secret disimpan?

Apakah domain, sertifikat HTTPS, dan konfigurasi reverse proxy sudah siap?

Backup dan pemulihan

Apakah backup DB sudah ada dan siapa yang bertanggung jawab?

Bagaimana cara restore yang sudah diuji?

Apa prosedur rollback aplikasi jika deployment gagal?

Siapa yang berwenang melakukan perubahan pada firewall, storage, atau konfigurasi OS?

&#x20; Salin checklist

Kalau banyak jawaban masih belum jelas, jangan menebak sendiri. Minta informasi tersebut dari PIC infrastruktur sebelum hari deployment.

# 5. Urutan deployment pada hari pelaksanaan

Gunakan urutan ini sebagai gambaran umum. Urutan sebenarnya harus disesuaikan dengan runbook dan standar perusahaan.

1. Verifikasi kondisi awal

   Pastikan server, OS, jaringan, akses administrasi, waktu sistem, kapasitas disk, dan status backup sesuai rencana. Catat kondisi awal sebelum mengubah apa pun.
2. Siapkan environment

   Pasang atau verifikasi runtime, dependency, direktori aplikasi, permission, konfigurasi service, dan kebutuhan storage. Gunakan versi yang sudah disetujui.
3. Siapkan database

   Verifikasi versi DB, penyimpanan persisten, akun aplikasi, permission, konfigurasi koneksi, dan backup yang dapat dipulihkan. Jalankan migrasi melalui prosedur yang disepakati.
4. Deploy backend

   Pasang artifact atau kode dari sumber yang disetujui, isi konfigurasi environment, jalankan service, dan periksa log serta health check.
5. Deploy frontend

   Deploy hasil build, atur konfigurasi API dan web server, lalu pastikan frontend dapat mengakses backend melalui jalur yang benar.
6. Konfigurasi akses dan keamanan

   Verifikasi DNS, HTTPS, reverse proxy, firewall, dan akses antarservice. Jangan membuka port tambahan hanya karena koneksi belum berhasil.
7. Uji end-to-end

   Buka aplikasi dari perangkat pengguna, login jika tersedia, jalankan fungsi utama, uji API, baca dan tulis data uji yang aman, serta periksa log semua komponen.
8. Serah terima dan monitoring

   Catat versi yang terpasang, konfigurasi yang relevan, status pengujian, hasil backup/restore, masalah yang tersisa, dan prosedur rollback. Pantau layanan setelah deployment.

## 6. Kenali masalah yang paling mungkin muncul

| Gejala                           | Hal pertama yang diperiksa                            |
| -------------------------------- | ----------------------------------------------------- |
| Domain tidak bisa dibuka         | DNS, routing, firewall, reverse proxy                 |
| FE terbuka tetapi API gagal      | URL API, CORS, TLS, jalur jaringan                    |
| Backend tidak berjalan           | Log service, runtime, konfigurasi environment         |
| Backend tidak dapat mengakses DB | IP/hostname DB, port, firewall, kredensial, privilege |
| Aplikasi berjalan lalu mati      | Log, memory, disk, process manager, dependency        |
| Disk penuh                       | `df -h`, log, kapasitas dan lokasi data               |
| Deploy baru merusak aplikasi     | Perbedaan versi, migrasi DB, konfigurasi, rollback    |

Jangan langsung restart seluruh server setiap kali terjadi masalah. Mulailah dari gejala, log, dan komponen yang terlibat. Restart atau perubahan konfigurasi harus mengikuti prosedur operasional perusahaan.

# 7. Tiga hal yang jangan sampai kamu lakukan

Jangan mengubah konfigurasi produksi tanpa persetujuan

Termasuk firewall, IP, routing, partisi disk, RAID, dan konfigurasi storage. Perubahan yang salah bisa membuat server tidak dapat diakses.

Jangan membuka database ke jaringan publik

Batasi akses sesuai kebutuhan dan jangan menaruh password database atau secret dalam repository, log, maupun frontend.

Jangan menganggap backup berhasil hanya karena job sukses

Backup harus dapat dipulihkan. Untuk database penting, pastikan restore sudah diuji dan disetujui sebelum melakukan perubahan berisiko.

Jika server belum memiliki OS, belum ada akses administrasi, atau topologi jaringan belum jelas, itu bukan sesuatu yang harus kamu selesaikan dengan menebak-nebak saat berada di data center. Minta bantuan engineer yang bertanggung jawab atas infrastruktur fisik.

# 8. Sekarang, kita buat rencana yang benar-benar sesuai tugasmu

Saya ingin membimbingmu secara praktik, bukan sekadar memberikan teori. Ada satu informasi paling penting yang perlu saya ketahui dahulu.

# Profil deployment kamu

Isi yang sudah kamu ketahui. Kalau belum tahu, pilih "Belum tahu" — itu juga informasi yang berguna.

1\. Sistem operasi server

Linux (Ubuntu, Debian, RHEL, Rocky, atau lainnya)

Windows Server

Belum tahu

2\. FE, BE, dan DB ditempatkan di mana?

Satu server fisik

Beberapa server fisik

Belum tahu

3\. Teknologi aplikasi yang digunakan

React/Vue + Node.js + PostgreSQL

Stack lainnya

Belum tahu

4\. Kondisi server saat ini

OS sudah terpasang, server siap diakses

Server fisik baru, OS belum dipasang

Belum tahu

Susun rencana deployment saya

Setelah informasi ini jelas, kita bisa mulai dari Hari 1: mengenali server, mengaksesnya dengan aman, membaca konfigurasi jaringan, dan memahami topologi deployment. Dengan begitu, kamu datang ke data center membawa rencana yang konkret, bukan sekadar hafalan perintah Linux.