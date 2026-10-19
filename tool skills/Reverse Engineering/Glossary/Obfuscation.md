---
tags: [glossary]
---


Obfuscation (atau obfuskasi) adalah teknik membuat kode program, data, atau informasi menjadi sangat sulit dipahami oleh manusia maupun alat analisis, tanpa mengubah fungsi atau hasil kerjanya.



Tujuan Utama Obfuscation

• Melindungi Kekayaan Intelektual: Mencegah orang lain menyalin atau membongkar logika bisnis aplikasi Anda.

• Mempersulit Reverse Engineering: Menyulitkan hacker atau pihak tidak sah dalam menganalisis kode untuk mencari celah keamanan.

• Menghindari Deteksi Statis: Kadang digunakan untuk menyembunyikan skrip atau payload tertentu dari sistem keamanan.
Catatan: Obfuscation bukan enkripsi. Jika enkripsi memerlukan kunci khusus untuk membuka data kembali, obfuscation hanya membuat tampilannya ruwet tanpa sistem kunci yang ketat.


Jenis-Jenis Teknik Obfuscation pada Kode

• Variable Renaming: Mengganti nama variabel, fungsi, atau kelas dengan karakter acak atau nama yang tidak bermakna (misalnya mengubah hitungTotal() menjadi _0x1a2b()).

• Control Flow Obfuscation: Mengubah struktur alur logika program (seperti memecah perulangan atau menambahkan percabangan rumit) agar sulit diikuti.

• String Encryption / Encoding: Menyimpan teks atau string penting (seperti API key atau URL) dalam bentuk tersamar.

• Dead Code Insertion: Menambahkan baris kode sampah yang tidak memiliki fungsi apa pun selain mengecoh orang yang sedang membaca kode tersebut.



Perbedaan Obfuscation dengan Metode Lain

• Encoding: Mengubah format data agar aman dikirim antar sistem (contoh: Base64), dapat dikembalikan dengan mudah tanpa key.

• Obfuscation: Membuat data/kode sulit dibaca manusia, tetapi tetap bisa dieksekusi oleh mesin.

• Hashing: Mengubah data menjadi sidik jari digital satu arah yang tidak bisa dikembalikan lagi (contoh: SHA-256).

• Encryption: Mengunci data secara matematis sehingga hanya bisa dibaca jika memiliki kunci dekripsi.