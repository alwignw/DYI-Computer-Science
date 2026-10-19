---
tags: [latihan, reverse-engineering]
tahap: 1
status: belajar
---

# Latihan 1.3 – Endianness

Konsep terkait: [[Endianness]]

## Jawaban saya
1. `0xAABBCCDD` little-endian = `AA BB CC DD`; big-endian = `DD CC BB AA`.
2. `2A 00 00 00` little-endian → balik jadi `00 00 00 2A` = 2×16 + 10 = 42.
3. `0x1F` = 1×16 + 15 = 31.

## Koreksi
1. **Terbalik.** Little-endian = `DD CC BB AA` (LSB di alamat terendah); big-endian = `AA BB CC DD` (sama dengan penulisan biasa).
2. **Benar**: 42. Langkah membalik byte dan memakai bobot 16 sudah tepat.
3. **Benar**: 31. Kesalahan bobot dari sesi 1.2 sudah teratasi.

## Catatan
Konsep pada soal 2 sudah dipahami (balik byte lalu hitung), tetapi soal 1 menunjukkan label little/big masih tertukar. Pengingat: little-endian = "yang kecil (LSB) di depan/alamat kecil".

## Klarifikasi dari saya
Soal 1 salah karena salah baca: `AA BB CC DD` dikira sudah little-endian yang harus diubah ke big-endian. Padahal `0xAABBCCDD` adalah **nilai** (ditulis biasa), dan yang diminta adalah cara menyimpannya sebagai little-endian. Tips: tanya dulu "ini nilai atau isi memory?" sebelum membalik byte.
