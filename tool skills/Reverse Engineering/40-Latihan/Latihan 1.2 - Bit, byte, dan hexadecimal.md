---
tags: [latihan, reverse-engineering]
tahap: 1
status: belajar
---

# Latihan 1.2 – Bit, byte, dan hexadecimal

Konsep terkait: [[Bit, byte, dan hexadecimal]]

## Jawaban saya
1. `0011 1100` → hex `0x3C`, desimal **15**.
2. `0x2A` → desimal **12**.
3. 2 byte maksimum `0xFFFF` = 15×1 + 15×16 + 15×256 + 15×4096 = 65.535. Lalu bertanya: 3 byte apakah `0xFFFFFF`?

## Koreksi
1. Hex `0x3C` **benar**. Desimal **salah**: seharusnya 3×16 + 12 = **60**, bukan 15.
2. **Salah**: 2×16 + 10 = **42**, bukan 12.
3. **Benar**: `0xFFFF` = 65.535, dan perhitungan bobot 1/16/256/4096 sudah tepat. Pertanyaan balik juga benar: 3 byte = `0xFFFFFF` = 16.777.215.

## Pola kesalahan
Pada soal 1 dan 2, digit hanya dijumlahkan tanpa dikali bobot posisi (3+12, 2+10). Di soal 3 caranya sudah benar. Gunakan cara soal 3 untuk semua konversi hex → desimal.
