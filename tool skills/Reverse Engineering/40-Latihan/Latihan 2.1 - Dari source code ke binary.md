---
tags: [latihan, reverse-engineering]
tahap: 2
status: belajar
---

# Latihan 2.1 – Dari source code ke binary

Konsep terkait: [[Dari source code ke binary]]

## Jawaban saya
1. Aplikasi dynamic linking dan di-strip. Masih diketahui: library eksternal yang dipakai. Hilang: informasi simbol, misalnya nama fungsi lokal.
2. Nama variabel lokal umumnya hilang saat compile, kecuali informasi debug dipertahankan.
3. Ulangan: `"Hi"` sebagai string C → `48 69 00`.

## Koreksi
1. **Benar.** Catatan: yang dihapus strip adalah nama fungsi lokal; nama fungsi library yang diimpor tetap terlihat, jadi tetap bisa jadi petunjuk.
2. **Benar**, termasuk kualifikasi tentang debug info.
3. **Benar.** `H` = `0x41 + 7` = `0x48`, `i` = `0x61 + 8` = `0x69`, lalu NUL `00`. Kelemahan sesi lalu sudah teratasi.

## Catatan
Pemahaman pipeline dan sifat lossy sudah baik.
