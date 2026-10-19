Soal cek pemahaman tadi: VirtualBox di laptop itu **Tipe 2**, karena berjalan sebagai aplikasi di atas Host OS. Sekarang lanjut ke Fase 3.

## Fase 3: Cara Kerja Virtualisasi

Pertanyaan intinya: **bagaimana Guest OS bisa merasa punya CPU, RAM, disk, dan network sendiri, padahal semuanya cuma jatah dari satu mesin fisik?** Jawabannya: hypervisor membuat **versi virtual** dari tiap komponen dan menerjemahkannya ke hardware asli.

---

### 1. CPU Virtualization

**Konsep vCPU**

VM tidak mendapat CPU fisik utuh, melainkan **vCPU (virtual CPU)**. vCPU adalah "jatah waktu" di core fisik. Hypervisor menjadwalkan vCPU dari banyak VM bergantian di core fisik, mirip beberapa penghuni berbagi satu dapur bersama dengan sistem giliran.

**Masalah klasik: instruksi privileged**

Sistem operasi biasanya berasumsi dia "penguasa" hardware dan menjalankan instruksi khusus (privileged instructions). Kalau Guest OS bebas menjalankan itu langsung, dia bisa merusak host dan VM lain. Solusi lama: hypervisor **menjebak (trap)** instruksi tersebut lalu mengemulasikannya, tapi ini lambat.

**Solusi modern: hardware-assisted virtualization**

CPU modern punya fitur bawaan untuk virtualisasi:
- **Intel VT-x**
- **AMD-V**

Dengan fitur ini, CPU punya mode khusus untuk Guest OS. Kode guest berjalan **langsung di CPU** dengan kecepatan hampir native, dan hanya saat ada hal sensitif, kendali dilempar ke hypervisor (disebut **VM Exit**), lalu dikembalikan lagi (**VM Entry**).

Itu sebabnya di BIOS sering ada opsi "Enable Virtualization / VT-x". Kalau mati, VM jadi lambat atau tidak jalan.

**Overcommit**: total vCPU boleh lebih banyak dari core fisik (misalnya 16 vCPU di mesin 8 core), selama VM tidak semuanya sibuk bersamaan. Enak untuk efisiensi, tapi kalau semua sibuk, performa turun.

---

### 2. Memory Virtualization

Di komputer biasa, ada dua level alamat: **virtual address** (yang dilihat program) dan **physical address** (lokasi RAM asli). OS yang menerjemahkan keduanya.

Di VM jadi **tiga level**:

```
Guest virtual address  → Guest "physical" address → Host physical address
   (dilihat aplikasi)      (dikira RAM asli oleh      (RAM fisik sungguhan)
                            Guest OS)
```

"RAM fisik" yang dilihat Guest OS sebenarnya palsu. Hypervisor yang memetakannya ke RAM asli. Penerjemahan dua tahap ini dulu dilakukan lewat **shadow page table** (software, lambat). Sekarang dibantu hardware lewat **EPT (Intel)** atau **NPT (AMD)**, jadi jauh lebih cepat.

**Teknik pengelolaan memori:**
- **Memory overcommit**: total RAM semua VM boleh melebihi RAM fisik, dengan asumsi tidak semua VM memakai penuh
- **Ballooning**: hypervisor "meminjam balik" RAM yang tidak terpakai dari sebuah VM lewat driver khusus di dalam guest
- **Page sharing (mis. KSM di KVM)**: kalau beberapa VM punya isi memori identik (misalnya OS yang sama), disimpan sekali saja dan dibagi bersama

Analoginya: nomor unit yang dipakai penghuni ("unit 5") bukan lokasi fisik sebenarnya di gedung. Pengelola punya buku catatan yang memetakan "unit 5 penghuni A" ke lokasi asli.

---

### 3. Storage Virtualization

Disk VM sebenarnya hanyalah **file biasa** di storage host.

- Format umum: **VMDK** (VMware), **VDI** (VirtualBox), **VHDX** (Hyper-V), **qcow2** (KVM/QEMU)
- Guest OS melihatnya sebagai hard disk utuh, lalu mem-format dan mempartisinya seperti biasa

**Thin vs Thick provisioning**
- **Thick**: ruang dialokasikan penuh di awal (disk 100 GB langsung makan 100 GB)
- **Thin**: ruang dipakai sesuai isi sebenarnya, dan tumbuh seiring data bertambah

**Snapshot** memanfaatkan konsep **copy-on-write**: saat snapshot dibuat, kondisi disk "dibekukan", dan semua perubahan berikutnya ditulis ke file terpisah. Mau kembali ke kondisi lama tinggal buang file perubahannya. Ini yang membuat fitur "rollback" di VM terasa instan.

---

### 4. Network Virtualization

Tiap VM mendapat **virtual NIC (vNIC)** dengan MAC address sendiri. Hypervisor menyediakan **virtual switch** yang menghubungkan vNIC ke jaringan. Ada beberapa mode, dan ini yang paling sering kamu temui di VirtualBox/VMware:

| Mode | Cara kerja | Cocok untuk |
|---|---|---|
| **NAT** | VM keluar internet lewat IP host, tapi tidak bisa diakses dari luar | Browsing, install paket |
| **Bridged** | VM mendapat IP sendiri di jaringan yang sama dengan host, seperti perangkat terpisah | Menjalankan server yang diakses dari perangkat lain |
| **Host-only** | VM hanya bisa berkomunikasi dengan host dan sesama VM | Lab terisolasi |

---

### Bonus konsep: Emulation vs Paravirtualization (virtio)

Secara default hypervisor bisa **mengemulasikan** hardware lawas (misalnya kartu jaringan Intel e1000) supaya Guest OS apa pun punya driver-nya. Tapi emulasi itu lambat. Alternatifnya **paravirtualization**: Guest OS memakai driver khusus (misalnya **virtio** di KVM, atau VMware Tools / Guest Additions) yang "sadar" dirinya VM dan berkomunikasi langsung dengan hypervisor. Hasilnya I/O jauh lebih cepat. Itulah gunanya menginstal *Guest Additions* di VirtualBox.

---

### Ringkasan

| Komponen | Cara virtualisasi | Teknologi kunci |
|---|---|---|
| CPU | vCPU dijadwalkan di core fisik | VT-x / AMD-V |
| Memori | Pemetaan 3 level + overcommit | EPT / NPT, ballooning |
| Storage | Disk = file di host | VMDK/qcow2, thin provisioning, snapshot |
| Network | vNIC + virtual switch | NAT, Bridged, Host-only |

---

### Cek pemahaman

*Kenapa memory overcommit dan CPU overcommit bisa bikin performa turun drastis kalau semua VM tiba-tiba sibuk bersamaan?*

Kalau sudah nangkep, kita lanjut ke **Fase 4: VM vs Container**, yaitu kenapa Docker muncul dan kapan memilih salah satunya.