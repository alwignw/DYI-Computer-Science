---
tags: [glossary]
---


Hex dump adalah tampilan teks dari data biner (baik dari file, memori komputer, maupun aliran data/network stream) yang disajikan dalam bentuk angka heksadesimal (basis 16).
Setiap satu byte (8-bit) data direpresentasikan menggunakan dua digit angka heksadesimal (dari 00 hingga FF)


Struktur Format Standar (Canonical Format)

Tampilan hex dump biasanya dibagi menjadi 3 kolom utama pada setiap barisnya:
1. Offset (Alamat Byte): Menunjukkan posisi atau alamat awal byte dalam file/memori (biasanya ditulis dalam format heksadesimal).
2. Nilai Heksadesimal: Menampilkan isi data mentah sebanyak 8 hingga 16 byte per baris, dipisahkan spasi.
3. Representasi ASCII / Karakter: Menampilkan terjemahan dari byte tersebut ke dalam karakter teks yang bisa dibaca; karakter yang tidak bisa dicetak (non-printable) biasanya diganti dengan tanda titik (.).


Contoh tampilan baris hex dump:

00000000  48 65 6c 6c 6f 2c 20 57  6f 72 6c 64 
21           |Hello, World!|



Kegunaan Hex Dump

• Debugging & Pemecahan Masalah: Membantu pengembang melihat nilai mentah suatu data atau struktur paket komunikasi yang dikirim/diterima perangkat.
• Reverse Engineering & Analisis Malware: Membongkar file biner untuk melihat isi header, logika instruksi, atau mendeteksi kode berbahaya.
• Digital Forensics: Memeriksa isi asli penyimpanan atau file yang rusak/tersembunyi secara low-level tanpa diproses oleh aplikasi tertentu.
• Identifikasi Jenis File (Magic Number): Mengetahui format asli suatu file (misalnya file PNG atau PDF) dengan melihat beberapa byte pertama (signature file).





Alat / Tools untuk Membuat Hex Dump

Beberapa perintah terminal atau aplikasi populer untuk membuat dan melihat hex dump:
• hexdump: Utilitas bawaan sistem operasi Unix/Linux untuk mencetak isi file biner.
• xxd: Alat baris perintah di Linux untuk membuat atau mengembalikan (reverse) hex dump.
• HxD: Perangkat lunak editor heksadesimal berbasis Windows yang gratis untuk melihat dan mengubah data biner secara interaktif.
• Online Hex Dump Generator: Layanan berbasis web untuk mengunggah dan membaca isi file secara heksadesimal.



Jika Anda sedang mencoba memeriksa file atau mempelajari cara kerja perintah tertentu, beri tahu saya tools apa yang Anda gunakan (misalnya Linux terminal atau aplikasi Windows) agar saya bisa memberikan contoh perintahnya.


