---
tags: [monolith, dasar]
tahap: 1
status: belajar
---

# Apa itu Monolith

Monolith adalah aplikasi yang seluruh fiturnya dibangun, dijalankan, dan di-deploy sebagai **satu kesatuan**. Lawannya secara deployment adalah sistem terdistribusi seperti microservices.

## Tiga ciri "satu"
1. **Satu codebase**: semua modul ada di satu repository. Lihat [[Codebase]].
2. **Satu artifact deploy**: hasil build berupa satu paket. Lihat [[Deployable artifact]].
3. **Satu proses runtime**: modul saling memanggil lewat *function call* di memori yang sama, bukan lewat jaringan. Lihat [[Runtime process]].

> [!example] contoh
> Aplikasi asuransi dengan modul Polis, Premi, Klaim, Laporan dalam satu project dan satu database. Modul Klaim memanggil `polisService.getStatus(id)` langsung di kode, tanpa HTTP.

> [!warning] miskonsepsi
> - "Monolith = kode berantakan/jadul." Salah. Monolith adalah soal packaging dan deployment; kerapian adalah dimensi terpisah (lihat [[Monolith]] di Glossary).
> - "Satu VM = monolith." Salah. Satu VM hanya lokasi deploy. Yang menentukan adalah artifact dan proses runtime.

> [!question] latihan
> Lihat [[Latihan 1.1 - Apa itu Monolith]].

Konsep berikutnya: Ciri-ciri aplikasi monolith (1.2). MOC: [[MOC Tahap 1 - Dasar]].
