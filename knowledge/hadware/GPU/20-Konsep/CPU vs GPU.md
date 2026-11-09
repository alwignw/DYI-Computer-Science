---
tags: [gpu, fondasi, arsitektur]
tahap: 1
status: belajar
---

CPU dioptimalkan untuk **latency** (menyelesaikan satu tugas secepat mungkin), GPU dioptimalkan untuk **throughput** (menyelesaikan sebanyak mungkin tugas per detik). Perbedaan tujuan ini membuat alokasi transistor kedua chip sangat berbeda.

## Ide inti
- CPU: sedikit core yang besar dan kompleks, cache besar, branch prediction, out-of-order execution. Semua itu menyembunyikan latency untuk satu thread.
- GPU: ribuan unit hitung sederhana, cache per unit kecil, kontrol logic minim. Latency memory disembunyikan dengan **menjalankan thread lain** saat satu thread menunggu, bukan dengan cache besar.
- Trade-off: GPU sangat cepat untuk pekerjaan yang bisa dipecah menjadi banyak operasi identik dan independen, tetapi lambat untuk pekerjaan serial atau penuh percabangan.

Terkait: [[Latency]], [[Throughput]]

> [!example] Contoh industri
> Inference LLM: perkalian matriks besar berisi jutaan perkalian-penjumlahan independen cocok untuk GPU. Sedangkan tokenization, HTTP handling, dan scheduling request tetap berjalan di CPU.

> [!warning] Miskonsepsi
> "GPU lebih cepat dari CPU." Tidak selalu. Untuk satu operasi tunggal yang serial, satu core CPU lebih cepat. GPU menang pada total pekerjaan per detik.

> [!question] Latihan
> Lihat [[PROGRES]] dan folder 40-Latihan.
