---
tags: [reverse-engineering, cara-program-berjalan, stack, heap, memory]
tahap: 2
status: belajar
---

# Stack dan heap

[[Stack]] dan [[Heap]] adalah dua area [[Memory (RAM)]] tempat program menyimpan data saat berjalan. Stack untuk data sementara milik fungsi (otomatis), heap untuk data yang umurnya diatur manual atau lebih panjang.

```
alamat tinggi  ┌─────────────────┐
               │ Stack           │  ← tumbuh ke bawah, puncaknya ditunjuk rsp
               │  (variabel lokal│
               │   & return addr)│
               │        ↓        │
               │                 │
               │        ↑        │
               │ Heap            │  ← tumbuh ke atas (malloc / new)
               ├─────────────────┤
               │ Data (global)   │
               │ Code (.text)    │
alamat rendah  └─────────────────┘
```

## Stack
- Struktur **LIFO** (last in, first out): yang terakhir masuk, pertama keluar.
- Setiap pemanggilan fungsi membuat satu **stack frame**: berisi variabel lokal, argumen, dan **return address** (alamat instruksi untuk kembali ke pemanggil).
- Fungsi selesai → frame dibuang otomatis (`rsp` bergeser balik). Cepat, tanpa perlu dikelola.
- Register `rsp` (ARM64: `sp`) selalu menunjuk puncak stack. Stack tumbuh ke alamat **lebih rendah**.

## Heap
- Area untuk data yang ukurannya baru diketahui saat runtime atau harus hidup lebih lama dari satu fungsi.
- Diminta lewat `malloc()` (C) / `new` (C++/Java), dikembalikan lewat `free()` / garbage collector.
- Lebih lambat dari stack; urusan alokasi dan pembebasan ada di program.

| | Stack | Heap |
|---|---|---|
| Dikelola | otomatis (masuk/keluar fungsi) | manual / allocator |
| Kecepatan | sangat cepat | lebih lambat |
| Umur data | selama fungsi berjalan | sampai di-`free` |
| Ukuran | kecil, terbatas | besar |
| Isi khas | variabel lokal, return address | buffer dinamis, objek |

> [!example] contoh
> ```c
> void f() {
>     int a = 5;                  // a di stack
>     char *p = malloc(100);      // p (pointer) di stack, 100 byte-nya di heap
> }
> ```
> Saat `f` selesai, `a` dan `p` hilang bersama frame. Tapi 100 byte di heap tetap ada kalau tidak di-`free` (memory leak).

> [!warning] miskonsepsi
> - Stack dan heap **bukan** memory fisik yang berbeda; keduanya sama-sama RAM, hanya beda cara pakai.
> - Pointer yang menunjuk ke heap **tersimpan di stack** (kalau variabel lokal), jadi keduanya saling terkait.
> - "Stack tumbuh ke bawah" artinya alamat mengecil, bukan "ke bawah" secara visual saja.

> [!tip] relevansi RE
> Di Tahap 3-5 kamu akan melihat `sub rsp, 0x20` (alokasi frame) dan `call` (menaruh return address di stack). Return address di stack inilah yang dibaca debugger untuk menelusuri urutan pemanggilan fungsi.

> [!question] latihan
> Lihat [[Latihan 2.3 - Stack dan heap]].
