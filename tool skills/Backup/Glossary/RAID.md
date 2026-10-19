Oke, kita bayangkan dari kehidupan sehari-hari dulu ya. 😁

RAID (Redundant Array of Independent Disks) adalah teknik menggabungkan beberapa hard disk atau SSD agar bekerja sebagai satu sistem penyimpanan, dengan tujuan meningkatkan kecepatan, keamanan data, atau keduanya.

## 1. Bayangkan kamu punya 2 hard disk

Misalnya, kamu punya server dengan dua hard disk, masing-masing berkapasitas 1 TB.

Tanpa RAID

Hard disk 1 — 1 TB

Menyimpan data A, B, C.

Hard disk 2 — 1 TB

Penyimpanan terpisah, bisa digunakan untuk data lain.

Sekarang, kita atur keduanya menggunakan RAID.

Dengan RAID

Disk 1

## 1 TB

Disk 2

## 1 TB

Satu sistem penyimpanan RAID

Cara kedua disk bekerja bergantung pada konfigurasi RAID yang dipilih.

## 2. Ada beberapa jenis RAID

Nah, bagian ini yang paling penting. RAID punya beberapa cara kerja.

## RAID 0 — Mengejar kecepatan

Data dibagi ke dua disk.

### A

### C

### E

### G

### B

### D

### F

### H

Disk 1

Disk 2

- Kapasitas total: 2 TB
- Kecepatan baca/tulis bisa meningkat.
- Risiko: jika satu disk rusak, data pada keseluruhan array bisa hilang.

## RAID 1 — Mengejar keamanan

Data yang sama disalin ke kedua disk (mirroring).

Disk 1

A, B, C, D

Disk 2

A, B, C, D

- Kapasitas efektif: 1 TB
- Jika satu disk rusak, data masih tersedia di disk lainnya, selama disk tersebut berfungsi.
- Cocok untuk membantu menjaga ketersediaan data.

## RAID 5 — Seimbang

Data dan informasi pemulihan (parity) disebar ke beberapa disk.

Data A

Data B

Parity

Data C

Parity

Data D

- Minimal 3 disk.
- Kapasitas efektif dari 3 disk 1 TB: 2 TB.
- Dapat bertahan dari kerusakan satu disk, dengan konfigurasi yang sehat dan benar.

## 3. Kalau RAID bukan backup, lalu apa bedanya?

Misalnya kamu punya server yang menyimpan data penting perusahaan.

- RAID: membantu server tetap berjalan ketika disk tertentu rusak, tergantung jenis RAID.
- Backup: menyediakan salinan data yang bisa dipulihkan jika data asli terhapus, terkena ransomware, atau mengalami kerusakan.

Jadi, RAID bukan pengganti backup. Kalau data terhapus dari RAID 1, misalnya, penghapusan itu dapat ikut terjadi pada kedua disk.

Intinya: RAID adalah cara mengatur beberapa disk supaya bekerja bersama. Jenis RAID menentukan apakah prioritasnya kecepatan, kapasitas, atau perlindungan dari kerusakan disk.

Kalau kamu sedang belajar server dan infrastruktur, konsep berikutnya yang bagus dipahami adalah bagaimana RAID digunakan di server fisik atau melalui RAID controller.