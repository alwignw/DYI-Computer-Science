---
tags: [reverse-engineering, fondasi, memory]
tahap: 1
status: belajar
---

# Endianness

Aturan urutan [[Byte]] saat angka multi-byte disimpan di memory. Dasarnya ada di [[Bit, byte, dan hexadecimal]].

Contoh `0x12345678` (alamat +0 → +3):

```
Big-endian:    12 34 56 78   (MSB dulu)
Little-endian: 78 56 34 12   (LSB dulu, urutan byte dibalik)
```

- **Little-endian:** x86/x86-64, ARM64 (Mac/iPhone) dalam praktik. Paling sering ditemui di RE.
- **Big-endian:** network byte order dan beberapa arsitektur lama.
- Cara baca hex dump little-endian: balik urutan byte dulu, baru konversi.

> [!example] contoh
> `39 05 00 00` (little-endian, 4 byte) → balik → `00 00 05 39` → `0x0539` = 1337.
> Angka 1 = `01 00 00 00`.

> [!warning] miskonsepsi
> - Yang dibalik hanya urutan **byte**, bukan bit atau digit dalam satu byte (`0x78` tetap `78`).
> - "Little-endian" bukan berarti ditulis sama seperti angkanya: bentuk yang sama seperti penulisan biasa (`AA BB CC DD`) justru **big-endian**.
> - Endianness tidak mengubah nilai, hanya cara menyimpan dan membaca.

> [!question] latihan
> Lihat [[Latihan 1.3 - Endianness]].
