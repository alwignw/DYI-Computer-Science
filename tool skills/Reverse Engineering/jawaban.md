1\. Binary aplikasi:

- Masih bisa diketahui: library eksternal yang digunakan (dynamic linking).
- Sudah hilang: informasi simbol yang dihapus oleh proses stripping, misalnya nama fungsi lokal yang tidak dipertahankan.

2\. Nama variabel lokal: Umumnya hilang saat compile, kecuali informasi debug dipertahankan.

3\. String C `"Hi"` dalam hex per byte: `48 69 00` (termasuk null terminator `00`).