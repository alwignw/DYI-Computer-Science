
▎ [!question] Latihan Sesi 1
▎ Sebuah workload punya dua bagian:
▎ - A: menghitung 1 juta penjumlahan vektor independen (c[i] = a[i] + b[i])
▎ - B: memproses sebuah state machine di mana langkah ke-n bergantung pada hasil langkah ke-(n-1), dengan banyak if/else
▎
▎ 1. Bagian mana yang cocok untuk GPU, dan mana untuk CPU?
▎ 2. Jelaskan alasannya memakai istilah latency, throughput, dan independen.
▎ 3. Apa yang terjadi pada GPU jika dijalankan dengan hanya 10 thread saja, mengingat cara GPU menyembunyikan latency memory?