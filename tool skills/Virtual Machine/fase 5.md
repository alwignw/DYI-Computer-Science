Soal cek pemahaman tadi: untuk menjalankan kode pelanggan yang tidak dikenal, **VM lebih aman**. Container berbagi kernel host, jadi satu celah kernel bisa dipakai untuk kabur ke host dan menyerang container lain (*container escape*). Pada VM, penyerang harus menembus hypervisor, yang permukaan serangnya jauh lebih kecil. Karena itu platform seperti ini biasanya memakai VM atau microVM (Firecracker, gVisor, Kata Containers), bukan container biasa.

Sekarang Fase 5, fase terakhir.

## Fase 5: Use Case Nyata

### 1. VM di cloud: contoh AWS EC2

Waktu kamu "menyewa server" di cloud, yang kamu dapat sebenarnya adalah **VM**. EC2 (Elastic Compute Cloud) adalah layanan VM milik AWS.

**Pemetaan konsep Fase 1-3 ke EC2:**

| Konsep VM | Di EC2 |
|---|---|
| Image / template Guest OS | **AMI** (Amazon Machine Image) |
| Alokasi vCPU dan RAM | **Instance type** (t3.micro, m5.large, c6i.xlarge, dst.) |
| Disk virtual | **EBS** (disk jaringan yang bisa di-snapshot) atau instance store |
| vNIC dan virtual switch | **ENI** dan **VPC** (jaringan virtual terisolasi) |
| Firewall tingkat VM | **Security Group** |
| Hypervisor | **Nitro**, berbasis KVM dengan offload ke kartu hardware khusus |

Nitro menarik karena fungsi jaringan dan storage dipindahkan ke hardware khusus, sehingga hampir seluruh CPU host tersedia untuk VM pelanggan dan overhead hypervisor sangat kecil.

**Model harga (efek dari sifat VM yang bisa dialokasi fleksibel):**
- **On-Demand**: bayar per detik/jam, bisa dimatikan kapan saja
- **Reserved / Savings Plans**: komitmen 1-3 tahun, lebih murah
- **Spot**: memakai kapasitas sisa dengan diskon besar, tapi bisa diambil kembali sewaktu-waktu

---

### 2. Use case umum VM

**a. Isolasi environment**
Dev, staging, dan production dipisah dalam VM berbeda. Satu eksperimen yang merusak OS tidak menyentuh lingkungan lain.

**b. Testing lintas OS**
Developer menjalankan Windows, berbagai distro Linux, atau versi OS lama di satu laptop untuk menguji kompatibilitas (VirtualBox, VMware, Hyper-V).

**c. Aplikasi legacy**
Aplikasi lama yang butuh OS atau library tertentu bisa "dibekukan" di dalam VM, sehingga tidak perlu menyimpan hardware lama.

**d. Konsolidasi server**
Kembali ke masalah awal di Fase 1: server yang cuma terpakai 10-20% digabung jadi banyak VM di sedikit mesin fisik.

**e. High availability dan disaster recovery**
Karena VM pada dasarnya file dan state, ia bisa:
- di-**snapshot** dan di-**clone**,
- dipindahkan ke host lain (**live migration**, misalnya vMotion di VMware) tanpa mati, berguna saat hardware host perlu maintenance,
- direplikasi ke lokasi lain untuk pemulihan bencana.

**f. Lab dan sandbox keamanan**
Menganalisis malware atau menjalankan kode tak dipercaya di lingkungan yang bisa dibuang dan di-rollback.

**g. Fondasi platform lain**
Kubernetes cluster di cloud umumnya berjalan di atas VM (node = VM). Layanan serverless seperti Lambda memakai microVM. VM jadi lapisan dasar yang sering tidak terlihat.

---

### 3. Trade-off performa di dunia nyata

Dengan VT-x/AMD-V, EPT, dan driver paravirtual, overhead CPU biasanya kecil (satu digit persen). Masalah yang lebih sering muncul justru:

**Noisy neighbor**
VM lain di host yang sama menghabiskan CPU, disk, atau network, sehingga VM kamu ikut melambat. Tanda khasnya di Linux adalah **steal time** (`%st` di `top`) yang tinggi, artinya vCPU kamu siap jalan tapi core fisik sedang dipakai VM lain.

**Overhead I/O**
Jalur disk dan network lewat lapisan virtual selalu lebih panjang daripada langsung ke hardware. Mitigasinya: driver paravirtual (virtio/ENA), atau teknologi seperti **SR-IOV** dan **PCI passthrough** yang memberi VM akses hampir langsung ke perangkat.

**NUMA dan CPU pinning**
Di server multi-socket, VM yang vCPU-nya tersebar lintas socket bisa mengakses memori "jauh" yang lebih lambat. Workload sensitif latensi biasanya memakai CPU pinning dan penempatan sadar-NUMA.

**Overcommit**
Seperti di Fase 3: efisien saat beban rendah, berbahaya saat semua sibuk bersamaan.

**Opsi kalau butuh performa maksimal atau isolasi total:**

| Kebutuhan | Opsi |
|---|---|
| Hindari noisy neighbor, patuhi lisensi atau compliance | **Dedicated Host / Dedicated Instance** |
| Tanpa lapisan hypervisor sama sekali | **Bare-metal instance** (mis. EC2 `.metal`) |
| Akses GPU atau NIC langsung | **Passthrough / SR-IOV** |

---

### 4. Cara memilih: kerangka keputusan singkat

1. **Butuh OS berbeda atau isolasi keamanan kuat?** → VM
2. **Aplikasi modern, stateless, perlu deploy dan scale cepat?** → Container (sering di atas VM)
3. **Kode tak dipercaya dan perlu start cepat?** → microVM
4. **Performa mentah, latensi ekstrem, atau lisensi per-core?** → Bare-metal atau dedicated host
5. **Beban singkat dan sporadis?** → Serverless

---

### Cek pemahaman (fase terakhir)

*Aplikasi kamu di EC2 tiba-tiba lambat, padahal CPU usage di dalam VM cuma 30% dan tidak ada perubahan kode. Apa yang akan kamu curigai dan metrik apa yang kamu cek?*

Petunjuk: ingat bagian noisy neighbor.

---

## Rekap Seluruh Roadmap

1. **Konsep dasar**: VM adalah komputer dari software, memberi isolasi, efisiensi, dan fleksibilitas
2. **Hypervisor**: pengatur resource. Tipe 1 (bare-metal) untuk server, Tipe 2 (hosted) untuk desktop
3. **Mekanisme**: vCPU, memori 3 level, disk sebagai file, vNIC dan virtual switch
4. **VM vs Container**: VM memvirtualisasi hardware, container memvirtualisasi OS dan berbagi kernel
5. **Dunia nyata**: EC2, konsolidasi, DR, sandbox, serta trade-off performa dan keamanan

Kalau mau lanjut, ada beberapa arah yang nyambung: mendalami container (namespaces, cgroups, Docker image layers), Kubernetes, atau kembali ke roadmap Load Balancer di **Fase 2: algoritma** (round robin, least connections, sticky session). Mau lanjut ke yang mana?