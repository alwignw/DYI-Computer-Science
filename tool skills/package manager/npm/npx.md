Jika **NPM** adalah untuk **menginstal dan mengelola** paket, maka **NPX** adalah untuk **mengeksekusi (menjalankan)** paket tersebut.

**NPX** singkatan dari **Node Package Execute**. Ini adalah alat baris perintah (CLI runner) yang dibundel secara default bersama NPM (sejak NPM versi 5.2).

Untuk memahami NPX, mari kita lihat **masalah** yang diselesaikannya sebelum alat ini ada.

---

### 1. Masalah Sebelum Ada NPX
Bayangkan Anda ingin membuat proyek React baru menggunakan `create-react-app`. Sebelum ada `npx`, Anda punya dua pilihan yang sama-sama merepotkan:

*   **Cara 1 (Install Global):** 
    Anda harus menginstalnya secara global di komputer: `npm install -g create-react-app`. 
    *Masalahnya:* Ini mengotori folder global komputer Anda. Jika Anda hanya butuh tool itu sekali pakai, menginstalnya secara permanen adalah pemborosan ruang dan memori.
*   **Cara 2 (Install Lokal):** 
    Anda menginstalnya di proyek: `npm install create-react-app`. Lalu untuk menjalankannya, Anda harus mengetik path yang panjang dan jelek: `./node_modules/.bin/create-react-app my-app`.
    *Masalahnya:* Sangat tidak praktis dan merepotkan.

### 2. Solusi: Keajaiban NPX
Dengan **NPX**, Anda cukup mengetik satu perintah:
```bash
npx create-react-app my-app
```

**Apa yang sebenarnya dilakukan NPX di balik layar?**
1.  **Cek Lokal:** NPX mengecek apakah `create-react-app` sudah ada di folder `node_modules` proyek Anda saat ini. Jika ada, langsung pakai itu.
2.  **Download Sementara:** Jika tidak ada, NPX akan mengunduh package tersebut secara *sementara* dari registry NPM.
3.  **Eksekusi:** Menjalankan perintah tersebut.
4.  **Bersihkan:** Setelah selesai, package tersebut tidak diinstal secara permanen (tidak mengotori global atau lokal Anda).

**Analogi:** Jika NPM adalah **membeli dan menyimpan** alat di gudang, maka NPX adalah **menyewa** alat tersebut hanya untuk dipakai hari ini, lalu dikembalikan.

---

### 3. Perbedaan Singkat NPM vs NPX

| Fitur | NPM | NPX |
| :--- | :--- | :--- |
| **Fungsi Utama** | Menginstal, mengelola, dan menghapus package. | Menjalankan (eksekusi) binary/CLI dari sebuah package. |
| **Sifat Instalasi** | Permanen (masuk ke `node_modules` atau folder global). | Temporer (sementara, kecuali sudah ada di lokal). |
| **Contoh Perintah** | `npm install eslint` | `npx eslint .` |

---

### 4. Fitur "Superpower" NPX: Menjalankan Versi Spesifik
Ini adalah salah satu fitur NPX yang paling berguna. Anda bisa menjalankan package pada **versi tertentu** tanpa perlu menginstalnya terlebih dahulu.

Contoh, Anda ingin melihat bagaimana `cowsay` (package iseng yang membuat teks diucapkan oleh sapi ASCII) bekerja di versi lawas:
```bash
npx cowsay@1.4.0 "Halo Dunia"
```
NPX akan mengunduh `cowsay` versi 1.4.0 secara spesifik, menjalankannya, dan selesai. Anda tidak perlu repot menginstal dan menguninstall versi yang berbeda-beda.

---

### 5. Contoh Penggunaan NPX di Dunia Nyata

NPX sangat sering digunakan untuk **Scaffolding** (membuat kerangka proyek awal) atau menjalankan tool yang hanya dipakai sesekali.

*   **Membuat proyek Vite (Frontend modern):**
    ```bash
    npx create-vite@latest my-project
    ```
*   **Mengunduh template dari GitHub (menggunakan `degit`):**
    ```bash
    npx degit user/repo my-folder
    ```
*   **Menjalankan server lokal sederhana untuk testing HTML statis:**
    ```bash
    npx serve
    ```
*   **Inisialisasi tool konfigurasi (misal ESLint):**
    ```bash
    npx eslint --init
    ```

---

### 6. Catatan Tambahan: `npm create` dan `npm init`
Di versi NPM yang lebih baru, Anda mungkin melihat perintah seperti:
```bash
npm create vite@latest
```
Perintah ini pada dasarnya adalah **alias (jalan pintas)** dari `npm init vite@latest`, yang di bawah kapusnya **memanggil NPX**. Jadi, `npm create`, `npm init`, dan `npx` untuk inisialisasi proyek memiliki efek yang sama, yaitu mengeksekusi package tanpa menginstalnya secara permanen.

### Kesimpulan
Gunakan **`npm install`** ketika Anda membutuhkan package tersebut untuk **kode aplikasi Anda** (seperti React, Express, Lodash).
Gunakan **`npx`** ketika Anda membutuhkan package tersebut hanya sebagai **alat bantu (CLI tool)** untuk membuat proyek, menjalankan script, atau tugas development sesekali.