---
tags: [reverse-engineering, fondasi]
tahap: 1
status: belajar
---

# Apa itu Reverse Engineering

Reverse Engineering (RE) adalah membongkar sesuatu yang sudah jadi untuk memahami cara kerjanya tanpa punya desain atau source code aslinya. Pada software, objek analisisnya biasanya [[Binary]].

```
Normal:  source code  →  compile  →  binary
RE:      binary       →  analisis →  pemahaman logika asli
```

## Tujuan umum
- **Security:** analisis malware, mencari vulnerability.
- **Interoperability:** membuat sistem baru kompatibel dengan sistem lama yang dokumentasinya hilang.
- **Legacy recovery:** source code hilang tapi aplikasi masih dipakai.
- **Audit:** memeriksa perilaku software atau library pihak ketiga.

## Dua pendekatan
- [[Static Analysis]]: membaca program tanpa menjalankannya.
- [[Dynamic Analysis]]: menjalankan program lalu mengamati perilakunya.

> [!example] contoh
> Aplikasi lawas tidak kompatibel dengan Windows 11 dan source code-nya tidak ada. RE dipakai untuk memahami flow dan logic-nya sebelum dimigrasi.

> [!warning] miskonsepsi
> - RE tidak otomatis ilegal. Legalitas bergantung pada tujuan, lisensi, dan hukum setempat.
> - Static vs dynamic bukan soal "file install vs program berjalan" saja. Dalam praktik, keduanya hampir selalu dipakai bergantian.

> [!question] latihan
> Lihat jawaban di [[Latihan 1.1 - Apa itu Reverse Engineering]].
