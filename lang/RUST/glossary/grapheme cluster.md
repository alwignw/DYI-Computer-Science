Grapheme cluster (atau sering disebut extended grapheme cluster) adalah unit teks terkecil yang terlihat oleh mata pengguna sebagai satu "karakter" tunggal, meskipun secara di balik layar (dalam standar Unicode) ia bisa terdiri dari satu atau lebih titik kode (code points) yang digabungkan bersama. [1] (https://en.wiktionary.org/wiki/grapheme_cluster), [2] (https://webglossary.info/terms/grapheme-cluster/)

Contoh Grapheme Cluster

• Karakter dengan tanda diaketik: Huruf "é" bisa terbentuk dari dua code points Unicode, yaitu huruf dasar "e" ditambah tanda aksen "".
• Emoji kompleks: Emoji seperti "👩🏽‍💻" (wanita dengan warna kulit tertentu + laptop) sebenarnya tersusun dari beberapa code points (emoji wanita + pemilih warna kulit + zero width joiner + laptop) yang dirender menjadi satu ikon tunggal di layar. [1] (https://webglossary.info/terms/grapheme-cluster/)

Mengapa Grapheme Cluster Penting?

• Pemrosesan Teks & Kursor: Saat pengguna memindahkan kursor atau memilih teks (menggunakan tombol panah), sistem harus memperhitungkan satu grapheme cluster sebagai satu langkah utuh agar kursor tidak "nyangkut" di tengah-tengah komponen karakter seperti aksen atau emoji. [1] (https://dev.to/bbkr/utf-8-grapheme-clusters-42o7), [2] (https://webglossary.info/terms/grapheme-cluster/)
• Penghitungan Karakter & Metrik: Jika panjang string dihitung hanya berdasarkan jumlah code points mentah alih-alih grapheme cluster, aplikasi bisa menghasilkan kesalahan hitung pada operasi seperti jarak Levenshtein (string distance) atau panjang karakter di layar. [1] (https://stringalign.com/concepts/grapheme_clusters.html), [2] (https://webglossary.info/terms/grapheme-cluster/)
• Standar Unicode: Aturan pembagian dan penentuan batas-batas ini diatur secara resmi oleh Unicode dalam dokumen teknis UAX #29. Anda dapat mempelajari konsep istilah ini lebih lanjut di WebGlossary Info atau melihat bagaimana pengaturannya bekerja melalui Stack Explained. [1] (https://mitchellh.com/writing/grapheme-clusters-in-terminals), [2] (https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/stringsClusters.html), [3] (https://webglossary.info/terms/grapheme-cluster/), [4] (https://stackexplained.com/glossary/grapheme-cluster)
Apakah Anda sedang mengalami kendala saat memproses atau menghitung string teks di dalam bahasa pemrograman tertentu (seperti Python, JavaScript, atau Swift)?
