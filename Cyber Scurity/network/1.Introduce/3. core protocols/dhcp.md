# 📡 Protokol DHCP: Penjelasan 5W+1H
*Untuk Mahasiswa Network Engineering*

Sebagai mahasiswa yang sedang mempelajari network engineering, berikut penjelasan lengkap tentang protokol DHCP menggunakan metode **5W+1H**:

---

## 🔹 WHAT — Apa itu DHCP?
**DHCP (Dynamic Host Configuration Protocol)** adalah protokol jaringan standar yang digunakan untuk mengotomatiskan pemberian alamat IP dan parameter konfigurasi lainnya kepada perangkat dalam jaringan IP [[1]]. 

DHCP bekerja pada *Application Layer* dan menggunakan **UDP port 67 (server)** dan **UDP port 68 (client)** untuk komunikasi [[9]].

**Parameter yang dikirimkan DHCP Server:**
- Alamat IP unik untuk setiap perangkat
- Subnet mask (menentukan range jaringan lokal)
- Default gateway (untuk komunikasi ke luar jaringan lokal)
- DNS server (untuk resolusi nama domain) [[9]]

---

## 🔹 WHO — Siapa yang terlibat?
DHCP menggunakan model **client-server** dengan komponen utama [[9]]:

| Komponen | Peran |
|----------|-------|
| **DHCP Client** | Perangkat (PC, HP, printer, IoT) yang meminta konfigurasi jaringan |
| **DHCP Server** | Router/server yang mengelola pool IP dan memberikan konfigurasi |
| **DHCP Relay** | Fitur router/switch yang meneruskan request DHCP antar subnet berbeda |
| **Administrator** | Orang yang mengatur kebijakan alokasi IP dan opsi DHCP |

---

## 🔹 WHEN — Kapan DHCP digunakan?
DHCP digunakan saat:
- ✅ Perangkat baru pertama kali terhubung ke jaringan
- ✅ Perangkat *booting* tanpa konfigurasi IP valid
- ✅ Masa sewa (*lease*) alamat IP habis dan perlu diperbarui
- ✅ Perangkat berpindah titik akses jaringan (mobilitas pengguna) [[6]]

---

## 🔹 WHERE — Di mana DHCP diterapkan?
DHCP diimplementasikan di:
- 🏠 Jaringan rumah (router rumah tangga)
- 🏢 Jaringan perusahaan/kantor
- 🎓 Jaringan kampus dan institusi pendidikan
- ☁️ Infrastruktur cloud dan data center
- 📱 Jaringan nirkabel (Wi-Fi) dan seluler

> DHCP sangat kritis pada jaringan berskala besar karena menghindari konfigurasi manual yang rentan error [[6]].

---

## 🔹 WHY — Mengapa DHCP penting?
DHCP memberikan tiga nilai utama bagi manajemen jaringan [[6]]:

1. **Mengurangi beban operasional**  
   Administrator tidak perlu mengonfigurasi setiap client secara manual.

2. **Optimasi penggunaan alamat IP**  
   Alamat IP yang tidak terpakai dikembalikan ke pool dan dapat digunakan ulang oleh client baru.

3. **Mendukung mobilitas pengguna**  
   Client dapat berpindah jaringan tanpa perlu konfigurasi ulang manual.

Selain itu, DHCP juga **mencegah konflik IP** (dua perangkat menggunakan IP yang sama) yang dapat mengganggu konektivitas jaringan [[21]].

---

## 🔹 HOW — Bagaimana cara kerja DHCP?
DHCP menggunakan proses **4 langkah DORA** [[6]][[9]][[21]]:

```
📡 DHCP Discover → 🎁 DHCP Offer → ✋ DHCP Request → ✅ DHCP Acknowledge
```

### Tahapan DORA:

| Langkah | Pengirim | Tujuan | Keterangan |
|---------|----------|--------|------------|
| **Discover** | Client | Broadcast ke jaringan | Client mencari server DHCP yang tersedia |
| **Offer** | Server | Ke client | Server menawarkan IP + konfigurasi (subnet, gateway, DNS, lease time) |
| **Request** | Client | Ke server terpilih | Client menerima penawaran dan meminta alokasi resmi |
| **Acknowledge** | Server | Ke client | Server mengonfirmasi; client mulai menggunakan IP tersebut |

### Konsep Penting:
- **Lease Time**: Alamat IP diberikan untuk periode tertentu. Client harus memperbarui (*renew*) sebelum lease habis.
- **IP Address Pool**: Range alamat IP yang tersedia untuk dialokasikan.
- **DHCP Options**: Parameter tambahan seperti NTP server, domain name, dll [[9]].

---

## 💡 Tips Belajar untuk Network Engineer Pemula:
1. Praktikkan konfigurasi DHCP di simulator seperti **Cisco Packet Tracer** atau **GNS3**.
2. Pelajari perintah CLI untuk mengatur DHCP di router (misal: Cisco IOS: `ip dhcp pool`, `network`, `default-router`).
3. Analisis traffic DHCP menggunakan **Wireshark** untuk melihat paket DORA secara real-time.
4. Pahami perbedaan **DHCP Static Reservation** vs **Dynamic Assignment**.

> 📚 *Referensi: [[1]][[6]][[9]][[21]]*

Jika ada bagian yang ingin diperdalam (misal: DHCP relay, keamanan DHCP, atau troubleshooting), silakan tanyakan! 🚀