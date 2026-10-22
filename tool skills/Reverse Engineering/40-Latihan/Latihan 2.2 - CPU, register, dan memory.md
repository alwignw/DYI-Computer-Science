---
tags: [latihan, reverse-engineering]
tahap: 2
status: paham
---

# Latihan 2.2 – CPU, register, dan memory

Konsep terkait: [[CPU, register, dan memory]]

## Soal
> [!question] latihan
> 1. Sebutkan urutan tiga tahap siklus CPU, dan register mana yang dipakai CPU untuk tahu instruksi berikutnya.
> 2. Memory dari alamat `0x2000` berisi: `10 00 00 00 00 00 00 00`. Setelah `mov rax, [0x2000]`, berapa nilai `rax` dalam desimal?
> 3. Dalam satu kalimat, jelaskan beda register dan memory. Pakai kata "alamat".

## Jawaban saya
1. Fetch → Decode → Execute. Register penunjuk instruksi: Program Counter (`rip` di x86-64, `pc` di ARM64).
2. `rax` = 16. Little-endian: byte `10` di alamat terendah adalah byte paling tidak signifikan, jadi nilainya `0x0000000000000010` = 16.
3. Register = penyimpanan internal CPU yang sangat cepat, diakses lewat nama; memory = penyimpanan eksternal CPU yang lebih besar, data diakses lewat alamat tertentu.

## Koreksi
Semua benar.
- Soal 1: urutan dan register tepat.
- Soal 2: konversi little-endian benar, byte dibalik dulu baru dibaca. Kelemahan di 1.2 (bobot ×16) tidak muncul lagi: `0x10` = 1×16 = 16.
- Soal 3: benar dan memakai "alamat". Catatan kecil: pada soal 3 memory disebut "eksternal CPU", yang tepat untuk RAM. Hati-hati, cache ada di dalam CPU tapi bukan register.
