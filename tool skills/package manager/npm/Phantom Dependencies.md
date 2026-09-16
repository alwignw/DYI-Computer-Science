**Phantom Dependencies** (Depensi Hantu) adalah salah satu "masalah tersembunyi" yang paling umum dan berbahaya dalam ekosistem Node.js, khususnya terkait dengan cara NPM mengelola folder `node_modules`.

Secara sederhana: **Phantom dependency terjadi ketika Anda menggunakan sebuah package di dalam kode Anda, tetapi package tersebut TIDAK terdaftar secara eksplisit di `package.json` proyek Anda.**

Lalu, kenapa kodenya tetap bisa berjalan tanpa error? Karena package tersebut "menghantui" proyek Anda dengan cara menumpang di dalam `node_modules` milik package lain.

Mari kita bedah bagaimana ini bisa terjadi, kenapa ini berbahaya, dan cara mengatasinya.

---

### 1. Bagaimana Phantom Dependency Bisa Terjadi?

Untuk memahaminya, kita harus mengerti sejarah cara NPM menginstal package (disebut **Flattening / Hoisting**).

Sejak NPM versi 3, NPM mengubah cara instalasi untuk menghemat ruang disk dan menghindari duplikasi. NPM akan "meratakan" (flatten) struktur `node_modules`.

**Contoh Kasus:**
Misalkan proyek Anda membutuhkan **Package A**.
Di dalam `package.json` milik **Package A**, ia membutuhkan **Package B**.

Saat Anda menjalankan `npm install package-a`, NPM akan mengunduh keduanya. Agar efisien, NPM tidak menaruh Package B di dalam folder Package A, melainkan **mengangkatnya ke root `node_modules`**.

Struktur folder Anda akan terlihat seperti ini:
```text
node_modules/
├── package-a/
└── package-b/   <-- INI ADALAH "HANTU" NYA
```

**Kesalahan Developer:**
Karena Anda melihat folder `package-b` ada di root `node_modules`, Anda tergoda untuk langsung menggunakannya di kode Anda:
```javascript
// Di file kode Anda
import something from 'package-b'; 
```
Kode ini **BERHASIL** dijalankan oleh Node.js karena folder `package-b` memang ada di root. **TAPI**, Anda lupa (atau malas) menambahkan `package-b` ke dalam `package.json` proyek Anda. Inilah yang disebut Phantom Dependency.

---

### 2. Kenapa Phantom Dependency Sangat Berbahaya?

Anda mungkin berpikir, *"Ah, yang penting kodenya jalan."* Ini adalah pola pikir yang sangat berisiko. Berikut adalah bencana yang bisa terjadi:

#### A. Proyek Tiba-tiba Crash Setelah Update (The Update Trap)
Besok harinya, tim di balik **Package A** merilis versi baru. Di versi baru ini, mereka memutuskan untuk **tidak lagi menggunakan Package B** (mungkin mereka menggantinya dengan Package C).
Anda menjalankan `npm update`. Package B hilang dari root `node_modules`. Tiba-tiba, proyek Anda **CRASH** dan error `Module not found`, padahal Anda tidak mengubah kode Anda sama sekali.

#### B. Konflik Versi (Version Mismatch)
**Package A** mengupdate **Package B** ke versi mayor yang baru (misal dari v1 ke v2) yang memiliki *breaking changes*. Karena kode Anda menumpang menggunakan Package B, kode Anda yang ditulis untuk v1 tiba-tiba error karena sekarang dipaksa berjalan di v2.

#### C. "Works on My Machine" Syndrome
Kode Anda berjalan di komputer Anda karena kebetulan struktur `node_modules` sedang rata. Namun, ketika rekan tim Anda melakukan `npm install`, atau ketika kode di-deploy ke server produksi (CI/CD), struktur `node_modules` mungkin terselesaikan (resolved) dengan cara yang sedikit berbeda, dan aplikasi langsung gagal build.

---

### 3. Aturan Emas Menghindari Phantom Dependency

Aturannya sangat mutlak:
> **"Jika Anda melakukan `import` atau `require` terhadap sebuah package di dalam kode Anda, package tersebut WAJIB ada di dalam `dependencies` atau `devDependencies` di `package.json` Anda."**

Jika Anda butuh `lodash`, Anda harus `npm install lodash`, meskipun kebetulan `express` (yang sudah Anda install) juga menggunakan `lodash` di dalamnya.

---

### 4. Cara Mendeteksi Phantom Dependency

Karena ini sulit dilihat dengan mata telanjang (karena folder `node_modules` bisa berisi ratusan package), kita butuh bantuan alat (tools):

1.  **Menggunakan ESLint:**
    Install plugin `eslint-plugin-import` dan aktifkan rule `no-extraneous-dependencies`. ESLint akan memperingatkan Anda setiap kali Anda mengimport package yang tidak ada di `package.json`.
2.  **Menggunakan `depcheck`:**
    Ini adalah CLI tool yang memindai proyek Anda dan memberi tahu package mana yang ada di `package.json` tapi tidak dipakai, dan **package mana yang dipakai di kode tapi tidak ada di `package.json`** (Phantom).
    ```bash
    npx depcheck
    ```
3.  **Menggunakan `npm ls`:**
    Perintah ini akan menampilkan pohon dependency. Jika ada yang tidak beres atau ada package yang "nyasar", `npm ls` biasanya akan memberikan peringatan.

---

### 5. Solusi Modern: Package Manager yang "Kebal" Phantom Dependency

Karena masalah ini sangat meresahkan, package manager generasi baru dirancang secara fisik untuk **mencegah** phantom dependency terjadi sejak awal:

*   **pnpm:** Ini adalah keunggulan utama pnpm. pnpm tidak menggunakan struktur folder `node_modules` yang rata seperti NPM. pnpm menggunakan *symlink* yang sangat ketat. Jika `package-b` tidak ada di `package.json` Anda, Node.js **secara fisik tidak akan bisa menemukannya**, meskipun package tersebut ada di dalam `node_modules` milik package lain. Anda dipaksa untuk menginstalnya secara eksplisit.
*   **Yarn Berry (Yarn v2+):** Menggunakan fitur **PnP (Plug'n'Play)**. Yarn ini bahkan **tidak membuat folder `node_modules` sama sekali**. Ia membuat file `.pnp.cjs` yang memetakan secara eksak package mana yang boleh dipakai. Phantom dependency 100% mustahil terjadi di Yarn PnP.

### Kesimpulan
Phantom dependency adalah seperti **memakai barang tetangga tanpa izin dan tanpa sepengetahuan pemilik rumah**. Saat ini barangnya ada dan bisa dipakai, tapi begitu tetangga Anda memindahkan atau membuang barang tersebut, Anda akan kehabisan barang dan panik. 

Selalu pastikan setiap library yang Anda panggil di dalam kode terdaftar resmi di `package.json` Anda.