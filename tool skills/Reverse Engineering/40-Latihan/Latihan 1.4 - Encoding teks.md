---
tags: [latihan, reverse-engineering]
tahap: 1
status: belajar
---

# Latihan 1.4 – Encoding teks

Konsep terkait: [[Encoding teks]]

## Jawaban saya
1. `52 45 56 45 52 53 45` → `REVERSE`.
2. `"Go"` sebagai string C → `0x424342`.
3. `0x7A` = `z`; huruf besarnya `5A`, 1 byte.
4. `0xAABBCCDD`: little-endian = `0xDDCCBBAA`; big-endian = `0xAABBCCDD`.

## Koreksi
1. **Benar.**
2. **Salah.** Seharusnya `47 6F 00`: `G` = `0x41 + 6` = `0x47`, `o` = `0x61 + 14` = `0x6F`, lalu NUL `00` di akhir. Jawaban `42 43 42` terbaca `BCB`, dan tidak ada NUL.
3. **Benar.** `0x7A` = `z`, `0x5A` = `Z`, keduanya 1 byte.
4. **Benar secara isi**, label little/big sudah tidak tertukar lagi. Catatan notasi: yang ditanya urutan byte di memory, jadi tulis `DD CC BB AA` (little) dan `AA BB CC DD` (big). Penulisan `0x...` terbaca sebagai nilai angka, yang selalu `0xAABBCCDD`.

## Catatan
Membaca hex → teks sudah lancar. Kelemahan: mencari kode ASCII dari sebuah huruf. Pakai rumus `0x41 + (urutan huruf - 1)` untuk huruf besar dan `0x61 + (urutan huruf - 1)` untuk huruf kecil.
