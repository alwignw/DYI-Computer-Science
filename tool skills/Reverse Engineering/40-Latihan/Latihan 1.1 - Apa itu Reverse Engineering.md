---
tags: [latihan, reverse-engineering]
tahap: 1
status: belajar
---

# Latihan 1.1 – Apa itu Reverse Engineering

Konsep terkait: [[Apa itu Reverse Engineering]]

## Soal
Pikirkan satu situasi kerja sebagai arsitek teknis yang bisa diselesaikan dengan RE: situasinya, yang ingin diketahui, dan static atau dynamic.

## Jawaban saya
1. **Situasi:** aplikasi lawas, tidak ada .exe tapi ada hasil compile di Windows, tidak kompatibel dengan Windows 11, sehingga perlu RE.
2. **Ingin tahu:** flow aplikasi dan logic.
3. **Pendekatan:** static, karena yang dianalisis file hasil install, bukan program yang berjalan.

## Koreksi
- Poin 1 dan 2 tepat (legacy recovery + interoperability). Tambahan yang berguna: dependency (DLL/library), akses data/database, dan protokol komunikasi.
- Poin 3: static adalah awal yang bagus (aman, tanpa menjalankan apa pun). Tetapi alasannya bukan "karena file install". Untuk memahami flow dan logic, dan khususnya untuk mendiagnosis kenapa gagal di Windows 11, biasanya perlu [[Dynamic Analysis]] juga (misalnya di VM Windows lama untuk melihat API call dan error).
- Kesimpulan: static dulu untuk peta, dynamic untuk verifikasi.
