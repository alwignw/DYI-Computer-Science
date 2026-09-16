Pertanyaan yang sangat bagus dan mendasar. Memahami siapa yang berada di balik layar NPM membantu kita memahami mengapa ekosistem JavaScript bisa seandal dan sebesar ini.

Berikut adalah penjelasan detail mengenai siapa yang mengelola NPM dan bagaimana prosedur tata kelolanya.

---

### 1. Siapa yang Mengelola NPM?

Saat ini, NPM dikelola oleh **GitHub, Inc.**, yang merupakan anak perusahaan dari **Microsoft**.

*   **Sejarah Singkat:** NPM dibuat pada tahun 2010 oleh Isaac Z. Schlueter sebagai proyek open-source untuk mengelola paket Node.js. Perusahaan di balik NPM (NPM, Inc.) berdiri sendiri selama beberapa tahun.
*   **Akuisisi (2020):** Pada Maret 2020, **Microsoft** (melalui GitHub) mengakuisisi NPM, Inc. 
*   **Status Saat Ini:** Meskipun dimiliki oleh korporasi raksasa, **NPM Registry tetap bersifat publik dan gratis** untuk package open-source. Microsoft menyatakan bahwa tujuan akuisisi ini adalah untuk mendukung ekosistem developer, bukan untuk mengkomersialkan atau menutup akses ke registry dasar.

**Pihak-pihak yang terlibat dalam pengelolaan sehari-hari:**
1. **Tim Inti NPM (NPM Core Team):** Karyawan bergaji penuh dari GitHub/Microsoft yang bertanggung jawab atas infrastruktur registry, pengembangan CLI `npm`, dan website `npmjs.com`.
2. **GitHub Security Lab:** Tim keamanan khusus yang memindai kerentanan (vulnerability) dan malware di dalam registry.
3. **Komunitas Open Source (Working Groups):** Kelompok developer sukarelawan dari seluruh dunia yang berkolaborasi dengan tim NPM untuk membuat kebijakan, standar, dan perbaikan fitur (misalnya: *Package Maintenance Working Group*).

---

### 2. Bagaimana Prosedur Pengelolaannya?

Pengelolaan NPM adalah keseimbangan antara **keterbukaan** (siapa saja bisa mempublikasikan kode) dan **keamanan/stabilitas** (mencegah chaos di ekosistem global). Berikut adalah prosedur dan aturan main utamanya:

#### A. Prosedur Publikasi Package (Publishing)
*   **Akses Terbuka:** Siapa pun yang memiliki akun NPM dapat mempublikasikan package. Tidak ada proses "persetujuan" manual sebelum package muncul di registry. Ini menjaga kecepatan inovasi.
*   **Pencegahan Typosquatting:** NPM memiliki algoritma otomatis yang memblokir publikasi package dengan nama yang terlalu mirip dengan package populer (misalnya, mencoba mempublikasikan `reactt` atau `lodahs` untuk menjebak developer).
*   **Aturan 72 Jam (The 72-Hour Rule):** Ini adalah aturan paling terkenal dan krusial. Seorang developer **hanya boleh menghapus (unpublish) package miliknya dalam waktu 72 jam** setelah dipublikasikan. 
    *   *Mengapa?* Untuk mencegah insiden seperti tragedi **"left-pad" (2016)**, di mana seorang developer menghapus package kecil yang tiba-tiba merusak jutaan proyek (termasuk Facebook dan Netflix) yang bergantung padanya. Setelah 72 jam, package tidak bisa dihapus sembarangan; developer harus menghubungi tim support NPM dengan alasan yang sangat valid.

#### B. Prosedur Keamanan dan Moderasi (Security & Moderation)
Karena siapa saja bisa mengunggah kode, NPM menerapkan beberapa lapisan keamanan:
1. **Pemindaian Otomatis (Automated Scanning):** Setiap package yang diunggah dipindai oleh sistem otomatis untuk mendeteksi pola kode berbahaya, malware, atau skrip pencurian data (seperti *crypto-mining* atau pencurian variabel lingkungan).
2. **npm audit:** NPM menyediakan database kerentanan keamanan. Saat Anda menjalankan `npm audit`, CLI akan mencocokkan dependency Anda dengan database ini dan memberi tahu jika ada versi yang rentan, lengkap dengan saran perbaikannya.
3. **Pelaporan dan Takedown:** Jika komunitas atau tim keamanan menemukan package yang berisi malware atau melanggar hak cipta, mereka dapat melaporkannya melalui fitur "Report Package". Tim NPM akan meninjau dan dapat menghapus package tersebut atau menangguhkan (suspend) akun pelakunya secara permanen.

#### C. Manajemen Versi (Semantic Versioning / SemVer)
NPM tidak memaksa secara teknis, tetapi **sangat mendorong** dan alatnya dirancang untuk menggunakan standar **Semantic Versioning (SemVer)**: `MAJOR.MINOR.PATCH` (contoh: `1.4.2`).
*   Prosedurnya adalah berbasis kepercayaan dan konvensi komunitas. Developer diwajibkan untuk menaikkan `MAJOR` jika ada perubahan yang merusak kompatibilitas (*breaking changes*), sehingga pengguna lain tahu bahwa mereka perlu berhati-hati saat mengupdate.

#### D. Tata Kelola Berbasis Komunitas (Community Governance)
Microsoft/GitHub tidak membuat keputusan sendirian secara tertutup. NPM memiliki **Working Groups** resmi. 
*   Contoh: *Package Maintenance Working Group*. Kelompok ini terdiri dari maintainer package populer dari berbagai perusahaan. Mereka bertemu secara rutin untuk mendiskusikan masalah seperti: "Bagaimana cara mendanai maintainer open-source?" atau "Bagaimana menangani package yang sudah ditinggalkan (abandoned)?" Rekomendasi dari kelompok ini sering diadopsi menjadi fitur resmi NPM.

#### E. Infrastruktur dan Ketersediaan (Reliability)
*   NPM Registry adalah salah satu registry perangkat lunak terbesar di dunia (menyimpan jutaan package dan melayani miliaran unduhan per hari).
*   Prosedur pengelolaannya melibatkan penggunaan **Content Delivery Network (CDN)** global untuk memastikan unduhan cepat di mana saja, serta sistem redundansi (cadangan) agar registry tidak pernah *down* (memiliki target uptime 99,99%).

---

### 3. Apa yang Berubah Setelah Diakuisisi Microsoft?

Banyak yang awalnya khawatir NPM akan menjadi berbayar atau tertutup. Namun, yang terjadi justru sebaliknya:
1. **Gratis untuk Publik:** Package publik tetap 100% gratis untuk diunduh dan dipublikasikan.
2. **Fitur Keamanan Gratis:** Fitur seperti `npm audit` dan notifikasi ketergantungan yang rentan (dependency alerts) yang sebelumnya berbayar atau terbatas, kini tersedia secara gratis untuk semua repository publik di GitHub.
3. **GitHub Actions Integration:** NPM sekarang terintegrasi sangat mulus dengan GitHub Actions, memungkinkan proses publikasi package (publishing) dilakukan secara otomatis dan aman setiap kali ada rilis baru.

---

### Kesimpulan

NPM dikelola dengan model **hybrid**: 
Didedikasikan dan dibiayai oleh infrastruktur korporat yang kuat (**Microsoft/GitHub**) untuk menjamin kestabilan dan keamanan, namun tetap menjalankan prinsip **open-source** dengan memberikan kebebasan publikasi kepada siapa saja, serta melibatkan komunitas global dalam pengambilan keputusan melalui *Working Groups*. 

Aturan ketat seperti **Aturan 72 Jam** adalah bukti bahwa pengelola NPM memprioritaskan stabilitas ekosistem global di atas keinginan individu developer.