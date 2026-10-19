Soal cek pemahaman tadi: saat semua VM sibuk bersamaan, jatah yang "dijanjikan" lebih besar dari yang benar-benar ada.
- **CPU**: banyak vCPU berebut core fisik yang terbatas, jadi harus antre. Efeknya latensi naik dan aplikasi terasa lambat (di VMware disebut *CPU ready time*).
- **Memori**: RAM fisik tidak cukup, sehingga hypervisor terpaksa memakai ballooning atau swap ke disk. Disk jauh lebih lambat daripada RAM, jadi performa bisa anjlok drastis.

Sekarang Fase 4.

## Fase 4: VM vs Container

**Masalahnya di VM**

Tiap VM membawa **Guest OS lengkap**: kernel, library, dan service sistem. Akibatnya:
- ukurannya besar (GB),
- booting lambat (puluhan detik sampai menit),
- boros RAM, karena tiap VM menjalankan OS sendiri padahal aplikasi di dalamnya mungkin kecil.

Container muncul untuk menjawab ini: bagaimana kalau kita tetap dapat isolasi, tapi tanpa membawa OS utuh untuk setiap aplikasi?

**Analogi: apartemen vs kamar kos dalam satu rumah**

- **VM** = unit apartemen. Tiap unit punya dapur, kamar mandi, dan instalasi sendiri. Isolasi kuat, tapi mahal dan butuh ruang besar.
- **Container** = kamar kos dalam satu rumah. Tiap penghuni punya kamar pribadi, tapi berbagi dapur dan instalasi (kernel) yang sama. Lebih murah, lebih cepat disiapkan, dan lebih padat, tapi isolasinya lebih tipis.

---

### Perbedaan arsitektur

```
        VM                          Container
┌────────┬────────┐          ┌────────┬────────┐
│  App A │  App B │          │  App A │  App B │
│  Libs  │  Libs  │          │  Libs  │  Libs  │
│Guest OS│Guest OS│          ├────────┴────────┤
├────────┴────────┤          │ Container Engine│
│   Hypervisor    │          │ (Docker, dll.)  │
├─────────────────┤          ├─────────────────┤
│     Host OS     │          │     Host OS     │
├─────────────────┤          │  (kernel dibagi)│
│    Hardware     │          ├─────────────────┤
└─────────────────┘          │    Hardware     │
                             └─────────────────┘
```

Perbedaan kuncinya: **VM memvirtualisasi hardware, container memvirtualisasi sistem operasi.** Semua container berbagi **satu kernel yang sama** milik host.

---

### Bagaimana container diisolasi tanpa OS sendiri?

Container pada dasarnya hanyalah **proses biasa di Linux** yang dibatasi dengan dua fitur kernel:

1. **Namespaces**: membatasi apa yang *bisa dilihat* proses. Tiap container punya tampilan sendiri untuk daftar proses (PID), network, filesystem (mount), hostname, dan user. Dari dalam container, kamu merasa sendirian di mesin itu.
2. **cgroups (control groups)**: membatasi apa yang *bisa dipakai* proses, misalnya maksimal 0,5 CPU dan 256 MB RAM.

Analogi: namespaces itu sekat dan tirai antar kamar kos, cgroups itu meteran listrik dan air per kamar.

Docker sendiri adalah tool yang memudahkan pembuatan dan pengelolaan semua ini, ditambah **image** (paket berisi aplikasi beserta dependensinya) yang bisa dijalankan di mana saja yang punya container engine. Itulah solusi masalah "di laptop saya jalan, di server kok error".

---

### Perbandingan

| Aspek | Virtual Machine | Container |
|---|---|---|
| Virtualisasi | Hardware | Sistem operasi |
| OS | Tiap VM punya Guest OS sendiri | Berbagi kernel host |
| Ukuran | GB | MB |
| Startup | Detik sampai menit | Milidetik sampai detik |
| Kepadatan | Puluhan per server | Ratusan per server |
| Isolasi | Kuat (batas hardware) | Lebih lemah (kernel dibagi) |
| Fleksibilitas OS | Bisa beda OS (Windows di atas Linux) | Harus kompatibel dengan kernel host |
| Overhead | Lebih tinggi | Sangat rendah |

---

### Trade-off yang sering terlewat

**1. Keamanan**
Karena kernel dibagi, celah di kernel bisa berdampak ke semua container di host itu (*container escape*). Pada VM, penyerang harus menembus hypervisor, yang permukaan serangnya jauh lebih kecil. Karena itu workload multi-tenant yang tidak saling percaya (misalnya penyedia cloud yang menjalankan kode pelanggan) biasanya tetap memakai VM sebagai batas isolasi.

**2. Container Linux butuh kernel Linux**
Kalau kamu menjalankan Docker di Windows atau macOS, sebenarnya Docker berjalan di dalam **sebuah VM Linux kecil** yang disembunyikan. Jadi container tidak benar-benar lepas dari VM.

**3. Container itu sementara (ephemeral)**
Container lazimnya dianggap bisa dihapus dan dibuat ulang kapan saja. Data yang penting harus disimpan di *volume*, bukan di dalam container.

---

### Bukan "atau", tapi sering "dan"

Di dunia nyata keduanya sering dipakai **bersamaan**:

```
Hardware → Hypervisor → VM (misalnya EC2) → Docker/Kubernetes → Container
```

VM memberi isolasi dan batas antar tenant atau lingkungan, container memberi pengemasan dan deployment yang ringan di dalamnya. Ada juga jalur tengah seperti **microVM** (Firecracker, Kata Containers): isolasi ala VM dengan kecepatan hampir sekelas container. AWS Lambda dan Fargate memakai pendekatan seperti ini.

**Kapan pilih yang mana (aturan praktis):**
- **VM**: butuh OS berbeda, isolasi keamanan kuat, aplikasi legacy yang butuh OS utuh, atau lingkungan multi-tenant
- **Container**: microservices, deployment cepat dan konsisten, scaling elastis, pipeline CI/CD

---

### Cek pemahaman

*Sebuah startup ingin menjalankan kode dari pelanggan yang tidak mereka kenal (misalnya platform online code-runner). Mereka mempertimbangkan container biasa vs VM. Mana yang lebih aman sebagai batas isolasi, dan kenapa?*

Kalau sudah nangkep, kita lanjut ke **Fase 5: Use case nyata**, yaitu EC2, isolasi environment, dan trade-off performa di dunia nyata.