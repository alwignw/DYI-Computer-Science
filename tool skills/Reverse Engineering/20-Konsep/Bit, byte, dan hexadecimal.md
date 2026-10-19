---
tags: [reverse-engineering, fondasi, biner, hex]
tahap: 1
status: belajar
---

# Bit, byte, dan hexadecimal

Komputer hanya menyimpan 0 dan 1 ([[Bit]]); 8 bit membentuk 1 [[Byte]] (nilai 0–255). [[Hexadecimal]] adalah cara singkat menulis byte: 1 byte = tepat 2 digit hex.

## Bobot posisi bit
```
posisi:  7    6    5    4    3    2    1    0
bobot:  128   64   32   16    8    4    2    1
```

## Hex
- Digit: `0-9` lalu `A=10 B=11 C=12 D=13 E=14 F=15`.
- 1 digit hex = 4 bit. Awalan `0x` menandakan hex.
- Konversi ke desimal: **setiap digit dikali bobot posisinya (pangkat 16)**, lalu dijumlahkan.
  - `0x2A` = 2×16 + 10 = 42
  - `0xFF` = 15×16 + 15 = 255
  - `0xFFFF` = 65.535 (2 byte)
  - `0xFFFFFF` = 16.777.215 (3 byte)
- Nilai maksimum n byte = 2^(8n) − 1.

> [!example] contoh
> `0011 1100` → `0011`=3, `1100`=C → `0x3C` = 3×16 + 12 = **60**.

> [!warning] miskonsepsi
> - Hex bukan jenis data lain; `0x41`, `65`, dan `01000001` adalah angka yang sama.
> - Jangan menjumlahkan digit tanpa bobot (`0x2A` ≠ 2+10). Digit kiri bernilai 16× lipat digit kanannya.

> [!question] latihan
> Lihat [[Latihan 1.2 - Bit, byte, dan hexadecimal]].
