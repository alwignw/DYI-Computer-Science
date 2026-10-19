---
tags: [reverse-engineering, cara-program-berjalan, compile, link]
tahap: 2
status: belajar
---

# Dari source code ke binary

Source code diterjemahkan ke [[Machine code]] lewat pipeline: [[Preprocess]] → [[Compile]] → [[Assemble]] → [[Linking]]. Reverse Engineering menempuh jalur ini ke arah sebaliknya, dan karena prosesnya *lossy*, sebagian informasi tidak bisa dipulihkan. Lihat dasar angkanya di [[Endianness]].

```
source (.c)
   │ ① Preprocess  → tempel #include, ganti #define
   │ ② Compile     → assembly (.s)
   │ ③ Assemble    → machine code dalam object file (.o)
   │ ④ Link        → gabung .o + library jadi 1 executable
   ▼
executable (binary)
```

| Tahap | Input → Output | Yang hilang / berubah |
|---|---|---|
| Compile | `.c` → assembly | Nama variabel lokal, komentar, struktur `for`/`while` |
| Assemble | assembly → `.o` | Instruksi jadi byte hex, misal `B8 2A 00 00 00` |
| Link | `.o` + library → binary | Alamat antar-file diselesaikan, fungsi library disambungkan |

- **Static linking:** kode library disalin ke binary (besar, mandiri).
- **Dynamic linking:** binary hanya mencatat library yang dibutuhkan (`.dylib`, `.so`, `.dll`), dimuat saat program jalan. Daftar library ini bisa dibaca tanpa menjalankan program.
- **Symbol table** menyimpan nama fungsi. Binary yang di-*strip* tidak memilikinya.

> [!example] contoh
> `int main() { return 42; }` menjadi kira-kira `B8 2A 00 00 00 C3`: `B8` = isi register, `2A 00 00 00` = 42 (little-endian), `C3` = return.

> [!warning] miskonsepsi
> - Decompile **tidak** mengembalikan source asli. Compile itu lossy, decompiler hanya menebak source yang setara fungsinya.
> - Nama variabel lokal hilang di tahap **compile**, bukan di link. Nama bisa bertahan kalau informasi debug disertakan.
> - Strip menghapus nama fungsi lokal, tapi nama fungsi library yang dipanggil lewat dynamic linking tetap terlihat.

> [!question] latihan
> Lihat [[Latihan 2.1 - Dari source code ke binary]].
