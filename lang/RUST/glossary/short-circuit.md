Short-circuit evaluation (evaluasi hubung singkat) adalah teknik dalam pemrograman di mana program berhenti mengevaluasi bagian dari ekspresi logika begitu hasil akhir dari ekspresi tersebut sudah bisa dipastikan. [1] (https://www.geeksforgeeks.org/c/short-circuit-evaluation-in-programming/), [2] (https://www.youtube.com/watch?v=AhNUQ6Hn3qM)
Dengan kata lain, jika ekspresi sebelah kiri sudah cukup untuk menentukan hasil benar (true) atau salah (false), maka ekspresi di sebelah kanannya tidak akan pernah dijalankan. [1] (https://comp.mga.edu/learning/python/module/3/topic/170), [2] (https://www.youtube.com/watch?v=AhNUQ6Hn3qM)

Cara Kerja Operator Short-Circuit

Teknik ini biasanya menggunakan operator logika AND (&& / and) dan OR (|| / or): [1] (https://www.youtube.com/watch?v=AhNUQ6Hn3qM)
1. Operator AND (&& / and)
	• Syarat agar hasilnya true adalah semua kondisi harus benar.
	• Jika kondisi pertama sudah false, maka hasilnya pasti false. Program akan langsung berhenti dan tidak mengevaluasi kondisi kedua.
	• Contoh: (false && doSomething()) -> Fungsi doSomething() tidak akan pernah dipanggil. [1] (https://comp.mga.edu/learning/python/module/3/topic/170), [2] (https://www.youtube.com/watch?v=AhNUQ6Hn3qM)
2. Operator OR (|| / or)
	• Syarat agar hasilnya true adalah salah satu kondisi saja sudah cukup bernilai benar.
	• Jika kondisi pertama sudah true, maka hasilnya pasti true. Program akan langsung berhenti dan tidak mengevaluasi kondisi kedua.
	• Contoh: (true || doSomething()) -> Fungsi doSomething() tidak akan pernah dipanggil. [1] (https://comp.mga.edu/learning/python/module/3/topic/170), [2] (https://www.youtube.com/watch?v=AhNUQ6Hn3qM)

Fungsi dan Keuntungan

• Mencegah Error (Runtime Error): Sangat berguna untuk pengamanan data.
	• Contoh: if (user != null && user.getName() == 'Budi')
	• Jika variabel user bernilai null, kondisi pertama bernilai false, sehingga program langsung berhenti. Pemanggilan user.getName() tidak dieksekusi, sehingga terhindar dari NullPointerException. [1] (https://stackoverflow.com/questions/9344305/what-is-short-circuiting-and-how-is-it-used-when-programming-in-java)
• Meningkatkan Efisiensi: Menghindari proses komputasi yang berat, pemanggilan fungsi yang memakan waktu, atau query database yang tidak perlu jika hasilnya sudah jelas sejak awal. [1] (https://www.geeksforgeeks.org/c/short-circuit-evaluation-in-programming/), [2] (https://stackoverflow.com/questions/9344305/what-is-short-circuiting-and-how-is-it-used-when-programming-in-java)
• Penulisan Kode Lebih Ringkas (Shorthand): Dalam bahasa seperti JavaScript, operator short-circuit sering dipakai untuk memberi nilai bawaan (default value):
	• Contoh: const nama = userInput || "Tamu"; (Jika userInput kosong/falsy, variabel nama otomatis bernilai "Tamu").

Hal yang Perlu Diwaspadai

• Efek Samping (Side Effects): Jika ekspresi kedua berisi fungsi yang mengubah state atau variabel penting (misalnya updateCount()), fungsi tersebut tidak akan berjalan ketika ekspresi pertama sudah men-short-circuit-kan kondisi. [1] (https://dev.to/mainulspace/short-circuit-evaluation-making-your-code-more-concise-2jne)
Jika Anda mau, beri tahu saya:
• Bahasa pemrograman apa yang sedang Anda gunakan (misalnya JavaScript, Java, C++, atau Python)
• Atau bagian mana yang ingin Anda lihat contoh kodenya
Saya bisa bantu buatkan ilustrasi kode yang sesuai.
