Spec-Driven Development (SDD) adalah metodologi pengembangan perangkat lunak di mana spesifikasi teknis yang detail, terstruktur, dan dapat dibaca oleh mesin (misalnya menggunakan skema JSON, OpenAPI, atau berkas Markdown terstruktur) menjadi sumber kebenaran tunggal (single source of truth) utama—bukan kodenya.

Konsep Utama SDD

- Spesifikasi Sebelum Kode: Seluruh kontrak API, arsitektur, dan kriteria penerimaan harus ditulis, divalidasi, dan disepakati terlebih dahulu sebelum satu baris pun kode ditulis

- Peran Utama dalam Era AI: SDD berkembang pesat sebagai solusi atas masalah "vibe coding" (ketika asisten AI atau LLM menulis kode cepat tapi sering melenceng dari niat awal atau merusak arsitektur). Dengan SDD, AI diberi cetak biru yang jelas untuk menghasilkan kode yang bersih dan sesuai standa

- Pengembangan Paralel: Tim frontend, backend, dan QA dapat bekerja secara bersamaan menggunakan mock server berdasarkan spesifikasi kontrak API yang sudah dikunci.

- Mengurangi Pengerjaan Ulang (Rework): Kesalahan desain dapat dideteksi sejak dini pada tahap perencanaan (shift-left), bukan saat tahap integrasi akhir.

Alur Kerja Umum SDD

- Intent & Constitution: Menentukan misi proyek, ruang lingkup, dan aturan dasar teknologi.

- Specification: Membuat spesifikasi teknis yang rinci dan terstruktur.


- Plan: Menyusun rencana pengerjaan, pembagian tugas (tasks), dan urutan eksekusi

- Implementation & Verification: Menulis atau menghasilkan kode (baik manual maupun dibantu AI) lalu memverifikasinya terhadap spesifikasi tersebut.

