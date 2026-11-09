- Default Immutability: Mengapa Rust mendesain variabel menjadi immutable (tidak bisa diubah) secara default jika dideklarasikan dengan let? Apa keuntungan dari sisi computer science / keamanan memori?

- Shadowing vs Mutability:  kita menggunakan shadowing (mendeklarasikan ulang variabel dengan nama yang sama). Apa perbedaan mendasar antara menggunakan shadowing dibandingkan menggunakan let mut? Kapan kamu harus memilih shadowing?

- Type Annotation: Jika kamu menulis let throughput = 100;, tipe data apa yang secara otomatis ditebak (inferred) oleh compiler Rust? Bagaimana jika kamu ingin memastikan itu adalah f64 (float 64-bit) tanpa menulis tipe datanya secara eksplisit di belakang variabel?

- const vs static: Sebelumnya kita pakai const. Rust juga punya static (contoh: static MAX_CONN: u32 = 1000;). Apa perbedaan mendasar antara const dan static dari segi alamat memori dan penggunaannya?


- Aturan Inisialisasi:
```
let throughput: f64;
if is_congested {
    throughput = 50.5;
} else {
    throughput = 100.0;
}
println!("Throughput: {}", throughput);
```
 Pada Kode tersebut, variabel throughput dideklarasikan tanpa nilai awal. Mengapa Rust mengizinkan hal ini, dan apa yang akan terjadi jika kita menghapus blok else pada kode tersebut?


