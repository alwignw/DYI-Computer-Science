---
tags: [reverse-engineering, cara-program-berjalan, cpu, register, memory]
tahap: 2
status: paham
---

# CPU, register, dan memory

CPU mengeksekusi [[Machine code]] satu instruksi demi satu, memakai [[Register]] (penyimpanan super cepat di dalam CPU) untuk data yang sedang diolah, dan [[Memory (RAM)]] untuk menyimpan kode serta data program. Memahami ini adalah dasar membaca assembly di Tahap 3.

```
        ┌──────────── CPU ────────────┐
        │  Register: rax rbx ... rip  │   ← kecil (puluhan), sangat cepat
        └──────────────▲──────────────┘
                       │ load / store (alamat)
        ┌──────────────▼──────────────┐
        │  Memory (RAM)               │   ← besar (GB), lebih lambat
        │  alamat 0x1000: 48 69 00 .. │
        └─────────────────────────────┘
```

## Siklus fetch–decode–execute
1. **Fetch:** CPU ambil instruksi dari memory di alamat yang ditunjuk [[Program counter]] (`rip` di x86-64, `pc` di ARM64).
2. **Decode:** CPU menerjemahkan byte menjadi operasi (misal `B8 2A 00 00 00` = isi register dengan 42).
3. **Execute:** operasi dijalankan, `rip` maju ke instruksi berikutnya (atau lompat kalau ada jump/call).

## Register penting
| Peran | x86-64 | ARM64 (Mac M-series) |
|---|---|---|
| Program counter (instruksi berikutnya) | `rip` | `pc` |
| Stack pointer (puncak stack) | `rsp` | `sp` |
| Hasil return fungsi | `rax` | `x0` |
| Serba guna | `rbx`, `rcx`, `rdx`, ... | `x1`–`x28` |

## Memory
- Memory = deretan byte, tiap byte punya **alamat** (angka, biasanya ditulis hex: `0x1000`).
- Kode program dan datanya sama-sama berupa byte di memory; bedanya hanya cara CPU memperlakukannya.
- Membaca banyak byte sekaligus mengikuti [[Endianness]].

> [!example] contoh
> Instruksi `mov rax, [0x1000]` artinya: baca 8 byte dari alamat `0x1000` di memory, taruh ke register `rax`. Register itu ibarat meja kerja, memory ibarat gudang.

> [!warning] miskonsepsi
> - Register **bukan** bagian dari RAM. Register ada di dalam CPU dan jumlahnya sangat sedikit.
> - `rip` bukan variabel program; ia menunjuk ke instruksi, bukan data.
> - Alamat memory bukan isi memory. Alamat `0x1000` adalah "lokasi", isinya bisa `48 69 00`.

> [!question] latihan
> Lihat [[Latihan 2.2 - CPU, register, dan memory]] (sudah dijawab, benar semua).
