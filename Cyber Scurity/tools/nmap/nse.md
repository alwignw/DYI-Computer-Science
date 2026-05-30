NSE adalah singkatan dari Nmap Scripting Engine, yaitu salah satu fitur paling canggih dan fleksibel pada Nmap yang memungkinkan pengguna untuk menjalankan skrip bawaan (atau kustom) guna mengotomatiskan berbagai tugas jaringan, mulai dari deteksi kerentanan, pengumpulan informasi lanjutan, hingga pengujian brute-force.


Berikut adalah detail penting mengenai NSE:
1. Kategori Skrip NSESkrip dikelompokkan ke dalam beberapa kategori utama:

auth: Menangani otentikasi dan pencarian kredensial (seperti brute-force login).

default: Kumpulan skrip standar yang paling sering digunakan untuk deteksi umum (diaktifkan otomatis dengan flag -sC atau -A).

discovery: Mengumpulkan informasi jaringan secara mendalam, seperti menemukan database atau hostname.vuln: Mendeteksi kerentanan keamanan atau celah exploit pada layanan yang aktif.

malware: Memeriksa apakah target terinfeksi malware atau backdoor.


2. Contoh PenggunaanBeberapa implementasi perintah yang umum digunakan dalam pentesting atau audit keamanan:

Menjalankan skrip default:

nmap -sC target.com Menjalankan kategori skrip tertentu (misal: vuln):

nmap --script vuln target.comMenjalankan skrip spesifik:

nmap --script smb-enum-users target.com

nmap --script=http-enum <ip>