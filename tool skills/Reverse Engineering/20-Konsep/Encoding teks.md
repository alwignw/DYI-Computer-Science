---
tags: [reverse-engineering, fondasi, encoding]
tahap: 1
status: belajar
---

# Encoding teks

Aturan yang mengubah karakter menjadi angka lalu menjadi [[Byte]], sehingga deretan byte di [[Hex-Dump]] bisa dibaca sebagai teks. Dasarnya ada di [[Bit, byte, dan hexadecimal]].

## ASCII
- 1 karakter = **1 byte**, hanya memakai `0x00`–`0x7F` (128 karakter).
- Nilai yang perlu dihafal:

| Hex | Karakter |
|---|---|
| `0x30`–`0x39` | `0`–`9` |
| `0x41`–`0x5A` | `A`–`Z` |
| `0x61`–`0x7A` | `a`–`z` |
| `0x20` | spasi |
| `0x0A` | newline |
| `0x00` | NUL (akhir string C) |

- Huruf kecil = huruf besar + `0x20`.
- Cara hitung cepat: `A` = `0x41`, huruf ke-N = `0x41 + (N-1)`. `a` = `0x61`, huruf ke-N = `0x61 + (N-1)`.
  - `G` (ke-7) = `0x41 + 6` = `0x47`
  - `o` (ke-15) = `0x61 + 14` = `0x6F`

## UTF-8
- [[Unicode]] memberi nomor ke semua karakter; [[UTF-8]] menyimpannya dalam **1–4 byte**.
- Karakter ASCII tetap 1 byte (identik dengan ASCII). Karakter lain 2–4 byte, semua byte-nya ≥ `0x80`.
- String tidak punya [[Endianness]]: urutan byte = urutan karakter.

> [!example] contoh
> `"Hi!"` → `48 69 21`.
> String C `"Hi"` → `48 69 00` (ada NUL di akhir).
> String C `"Go"` → `47 6F 00`.
> `é` dalam UTF-8 → `C3 A9`.

> [!warning] miskonsepsi
> - Karakter `'9'` disimpan sebagai `0x39`, bukan `0x09`.
> - "1 karakter = 1 byte" hanya benar untuk ASCII.
> - Menulis byte array sebagai `0x424342` (satu angka) membingungkan; tulis per byte: `47 6F 00`.

## Kenapa penting di RE
`strings` mencari rangkaian byte ASCII yang bisa dicetak, sehingga pesan error, path, dan URL bisa ditemukan tanpa membaca assembly.

> [!question] latihan
> Lihat [[Latihan 1.4 - Encoding teks]].
