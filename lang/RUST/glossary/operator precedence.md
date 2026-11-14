Operator precedence (prioritas operator) adalah aturan dalam bahasa pemrograman yang menentukan urutan suatu operasi dievaluasi ketika sebuah ekspresi memiliki lebih dari satu operator. [1] (https://translate.google.com/translate?u=https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence&hl=id&sl=en&tl=id&client=sge), [2] (https://www.termasmedia.com/pemrograman/java/17-operator-precedence-dan-ekspresi-numerik-di-pemrograman-java.html), [3] (https://www.youtube.com/watch?v=hOLAoo2p7gM&t=17)
Operator dengan prioritas lebih tinggi akan dikerjakan terlebih dahulu dibandingkan operator yang memiliki prioritas lebih rendah. [1] (https://translate.google.com/translate?u=https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence&hl=id&sl=en&tl=id&client=sge), [2] (https://www.termasmedia.com/pemrograman/java/17-operator-precedence-dan-ekspresi-numerik-di-pemrograman-java.html)

Contoh Sederhana

Perhatikan ekspresi matematika berikut di dalam kode pemrograman:
text
hasil = 2 + 3 * 4;
Use code with caution.
• Hasilnya adalah 14, bukan 20.
• Mengapa? Karena operator perkalian (*) memiliki prioritas lebih tinggi daripada operator penjumlahan (+). Oleh karena itu, 3 * 4 dihitung terlebih dahulu (menjadi 12), kemudian ditambahkan dengan 2. [1] (https://www.youtube.com/watch?v=hOLAoo2p7gM&t=17)

Mengubah Prioritas dengan Tanda Kurung

Jika Anda ingin mendahulukan operasi yang sebenarnya memiliki prioritas lebih rendah, Anda bisa menggunakan tanda kurung (...) karena tanda kurung memiliki prioritas paling tinggi dalam hampir semua bahasa pemrograman: [1] (https://translate.google.com/translate?u=https://www.php.net/manual/en/language.operators.precedence.php&hl=id&sl=en&tl=id&client=sge), [2] (https://www.youtube.com/watch?v=nNgfHCZbicY), [3] (https://www.youtube.com/watch?v=lgKxFMldeDY)
text
hasil = (2 + 3) * 4; // Hasilnya adalah 20
Use code with caution.

Hubungan dengan Asosiativitas (Associativity)

Ketika ada beberapa operator yang memiliki tingkat prioritas yang sama di dalam satu ekspresi, aturan asosiativitas yang akan menentukan arah pengelompokannya (apakah dari kiri ke kanan atau dari kanan ke kiri): [1] (https://translate.google.com/translate?u=https://en.cppreference.com/cpp/language/operator_precedence&hl=id&sl=en&tl=id&client=sge), [2] (https://translate.google.com/translate?u=https://www.php.net/manual/en/language.operators.precedence.php&hl=id&sl=en&tl=id&client=sge)
• Asosiativitas kiri ke kanan (contoh: pada operator +, -, *, /):
4 / 3 / 2 dibaca sebagai (4 / 3) / 2.
• Asosiativitas kanan ke kiri (contoh: pada operator penugasan =):
a = b = 5 dibaca sebagai a = (b = 5). [1] (https://translate.google.com/translate?u=https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence&hl=id&sl=en&tl=id&client=sge)
Anda dapat melihat daftar lengkap urutan prioritas ini pada dokumentasi resmi seperti Prioritas operator di JavaScript MDN atau panduan Prioritas Operator PHP. [1] (https://translate.google.com/translate?u=https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence&hl=id&sl=en&tl=id&client=sge), [2] (https://translate.google.com/translate?u=https://www.php.net/manual/en/language.operators.precedence.php&hl=id&sl=en&tl=id&client=sge)
Apakah Anda sedang mempelajari operator precedence untuk bahasa pemrograman tertentu (seperti C, Java, JavaScript, atau Python) atau ingin melihat tabel prioritas lengkapnya?
