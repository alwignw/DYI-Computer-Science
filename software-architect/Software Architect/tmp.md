🚀 TANTANGAN HARI 1: "The Flash Sale Problem"

Skenario:
Kamu adalah Lead Architect di sebuah startup e-commerce. Besok siang, perusahaan akan mengadakan Flash Sale sepatu edisi terbatas.
Stok barang: Hanya 1.000 sepatu.
Traffic: Diprediksi ada 50.000 user yang akan menekan tombol "Beli" di detik yang sama (Tepat pukul 12:00:00).
Target: Sistem tidak boleh down, dan TIDAK BOLEH terjadi overselling (stok minus / lebih dari 1.000 yang terjual).


Tugas Kamu:

1. Arsitektur & Traffic Management
Bagaimana caramu melindungi Database utama dari 50.000 request yang masuk di detik yang sama? Komponen apa saja yang akan kamu letakkan di depan Database?

2. Concurrency & Data Consistency
Saat user menekan "Beli", bagaimana caramu memastikan stok tidak berkurang menjadi minus jika ada 2 user yang mengambil barang terakhir di milidetik yang sama?

3. Asynchronous Processing
Setelah user klik "Beli", apakah sistem langsung memproses pembayaran dan update stok secara real-time (synchronous)? Atau ada cara lain agar user tidak perlu menunggu loading lama? Jelaskan alurnya!


4. Trade-off Analysis
Setiap keputusan arsitektur punya harga yang harus dibayar. Dari desain yang kamu buat di atas, apa kelemahan atau risiko terbesar dari sistemmu? Dan bagaimana caramu memitigasinya?

