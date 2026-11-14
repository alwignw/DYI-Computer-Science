Truncation toward zero (pemotongan menuju nol) adalah metode matematika atau pemrograman untuk membuang bagian pecahan (desimal) dari suatu angka tanpa melakukan pembulatan nilai, sehingga nilai hasilnya bergerak atau tetap berada lebih dekat (atau sama) dengan angka nol pada garis bilangan. [1] (https://www.roundingsolver.com/blog/truncation-vs-rounding/), [2] (https://calculatorgoat.com/mathematics/arithmetic/truncation-calculator/)

Cara Kerjanya

• Angka Positif: Bagian desimal dihilangkan begitu saja (sama seperti pembulatan ke bawah/floor).
	• Contoh: 5,789 menjadi 5
	• Contoh: 3,5 menjadi 3 [1] (https://www.geeksforgeeks.org/python/g-fact-35-truncate-in-python/), [2] (https://www.roundingsolver.com/blog/truncation-vs-rounding/)
• Angka Negatif: Bagian desimal dihilangkan tanpa menggeser angka lebih jauh ke kiri (negatif tak hingga); nilai mutlaknya justru mengecil atau mendekati nol (sama seperti pembulatan ke atas/ceil untuk bilangan negatif).
	• Contoh: -5,789 menjadi -5 (bukan -6)
	• Contoh: -3,5 menjadi -3 (bukan -4) [1] (https://www.fastly.com/documentation/reference/vcl/functions/math-rounding/math-trunc/), [2] (https://www.geeksforgeeks.org/python/g-fact-35-truncate-in-python/), [3] (https://www.roundingsolver.com/blog/truncation-vs-rounding/)

Perbedaan dengan Pembulatan Lain

• Bukan pembulatan biasa (Rounding): Truncation tidak melihat angka di belakang koma (misalnya apakah \(\ge 5\) atau \(<5\)) untuk menaikkan nilai. Semua ekor desimal langsung dihapus. [1] (https://www.roundingsolver.com/blog/truncation-vs-rounding/)
• Bukan Floor (Pembulatan ke bawah menuju \(-\infty \)): Untuk angka positif, hasilnya sama seperti floor. Namun, untuk angka negatif, floor akan menggeser angka ke kiri (misalnya -3,2 menjadi -4), sedangkan truncation toward zero memotong desimal dan menjadi -3. [1] (https://www.roundingsolver.com/blog/truncation-vs-rounding/), [2] (https://www.geeksforgeeks.org/python/g-fact-35-truncate-in-python/)

Penerapan dalam Pemrograman

Banyak bahasa pemrograman (seperti C, Java, atau fungsi seperti math.trunc() di Python dan C++) menggunakan metode truncation toward zero saat melakukan typecasting atau pembagian bilangan bulat (integer division), di mana sisa pembagian mengikuti tanda dari angka yang dibagi (dividend). [1] (https://stackoverflow.com/questions/18917717/advantages-of-using-truncation-towards-minus-infinity-vs-towards-zero), [2] (https://www.codecademy.com/resources/docs/cpp/math-functions/trunc), [3] (https://www.fastly.com/documentation/reference/vcl/functions/math-rounding/math-trunc/), [4] (https://www.geeksforgeeks.org/python/g-fact-35-truncate-in-python/)
Anda dapat membaca penjelasan lebih lanjut mengenai perbedaan metode pembulatan di Wikipedia: Truncation. [1] (https://en.wikipedia.org/wiki/Truncation)
Apakah Anda ingin melihat contoh penerapan truncation toward zero dalam bahasa pemrograman tertentu (seperti Python, Java, atau C++)?
