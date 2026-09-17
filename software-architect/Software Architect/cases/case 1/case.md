Selamat! 🎉 Memutuskan untuk belajar menjadi Software Architect adalah langkah yang luar biasa. 

Hari pertama sebagai architect berarti kamu harus melakukan **pergeseran mindset (mindset shift)**:
*   **Developer** bertanya: *"Bagaimana cara membuat fitur ini?"*
*   **Architect** bertanya: *"Apa risiko dari sistem ini? Di mana letak bottleneck-nya? Apa trade-off (kompromi) dari keputusan yang saya ambil?"*

Untuk tantangan **Hari 1**, kita tidak akan langsung melompat ke sistem perbankan global yang rumit. Kita akan mulai dengan kasus klasik yang menguji pemahamanmu tentang *scalability, concurrency,* dan *data consistency*.

---

### 🚀 TANTANGAN HARI 1: "The Flash Sale Problem"

**Skenario:**
Kamu adalah Lead Architect di sebuah startup e-commerce. Besok siang, perusahaan akan mengadakan **Flash Sale** sepatu edisi terbatas.
*   **Stok barang:** Hanya **1.000** sepatu.
*   **Traffic:** Diprediksi ada **50.000 user** yang akan menekan tombol "Beli" di detik yang sama (Tepat pukul 12:00:00).
*   **Target:** Sistem tidak boleh *down*, dan **TIDAK BOLEH** terjadi *overselling* (stok minus / lebih dari 1.000 yang terjual).

**Tugas Kamu:**
Buat rancangan arsitektur tingkat tinggi (High-Level Design) dan jelaskan strategimu untuk menjawab 4 poin berikut. Kamu bisa menjawabnya dengan teks, atau jika bisa, buat diagram sederhana (bisa pakai ASCII art atau deskripsi alur).

#### 1. Arsitektur & Traffic Management
Bagaimana caramu melindungi Database utama dari 50.000 request yang masuk di detik yang sama? Komponen apa saja yang akan kamu letakkan di depan Database? *(Hint: Pikirkan tentang CDN, Load Balancer, Cache, dan Antrian).*

#### 2. Concurrency & Data Consistency
Saat user menekan "Beli", bagaimana caramu memastikan stok tidak berkurang menjadi minus jika ada 2 user yang mengambil barang terakhir di milidetik yang sama? 
*(Hint: Riset tentang Optimistic vs Pessimistic Locking, atau penggunaan Redis untuk atomic operations).*

#### 3. Asynchronous Processing
Setelah user klik "Beli", apakah sistem langsung memproses pembayaran dan update stok secara *real-time* (synchronous)? Atau ada cara lain agar user tidak perlu menunggu loading lama? Jelaskan alurnya!

#### 4. Trade-off Analysis
Setiap keputusan arsitektur punya harga yang harus dibayar. Dari desain yang kamu buat di atas, apa **kelemahan** atau **risiko** terbesar dari sistemmu? Dan bagaimana caramu memitigasinya?

---

### 💡 Tips untuk Mengerjakan (Bahan Riset)
Karena ini hari pertama, jangan ragu untuk mencari tahu istilah-istilah ini jika belum paham:
*   *Rate Limiting / API Gateway*
*   *Redis / In-Memory Data Store*
*   *Message Queue (RabbitMQ / Kafka)*
*   *Database Locking (Row-level lock)*
*   *Idempotency*

### 🎯 Cara Menjawab
Silakan balas pesan ini dengan **jawaban dan pemikiranmu** untuk ke-4 poin di atas. Tidak harus sempurna, yang penting kamu bisa berargumen *mengapa* kamu memilih solusi tersebut. 

Nanti saya akan review jawabanmu, memberikan *feedback*, dan kita akan bedah bersama apa yang biasanya dilakukan oleh Senior/Principal Architect di dunia nyata untuk kasus ini.

Siap? Silakan mulai merancang! 🏗️💻