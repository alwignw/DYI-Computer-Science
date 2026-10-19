## Fase 2: Hypervisor

**Kembali ke analogi apartemen**

Di Fase 1, gedung dibagi jadi unit-unit apartemen. Siapa yang membagi dan mengatur semuanya? **Pengelola gedung**. Dia memastikan:

- tiap unit dapat jatah listrik dan air sesuai porsinya,
- penghuni satu unit tidak bisa masuk ke unit lain,
- kalau ada unit baru, dia yang menyiapkannya.

Di dunia VM, pengelola gedung itu adalah **hypervisor**.

**Definisi teknis**

Hypervisor (disebut juga **Virtual Machine Monitor / VMM**) adalah software yang membuat, menjalankan, dan mengelola VM. Tugas utamanya:

1. **Alokasi resource**: membagi CPU, RAM, disk, dan network dari host ke tiap VM
2. **Isolasi**: memastikan satu VM tidak bisa mengintip atau mengganggu VM lain
3. **Penjadwalan**: mengatur giliran VM memakai CPU fisik
4. **Penerjemah**: meneruskan permintaan hardware dari Guest OS ke hardware asli

Guest OS merasa dirinya berjalan di hardware sungguhan. Hypervisor yang "menipu" dengan sopan.

---

### Dua tipe hypervisor

**Tipe 1: Bare-metal**

Hypervisor dipasang **langsung di atas hardware**, tanpa OS di tengahnya.

```
VM 1 | VM 2 | VM 3
-------------------
    Hypervisor
-------------------
  Hardware fisik
```

- Contoh: **VMware ESXi, Microsoft Hyper-V, Xen, KVM**
- Performa tinggi karena jalurnya pendek
- Dipakai di data center dan cloud (AWS, GCP, Azure memakai hypervisor tipe ini)
- Analogi: pengelola gedung yang memang ditugaskan khusus mengurus gedung

**Tipe 2: Hosted**

Hypervisor berjalan **sebagai aplikasi biasa di atas OS** yang sudah ada.

```
VM 1 | VM 2
-------------
 Hypervisor (aplikasi)
-------------
   Host OS (Windows/macOS/Linux)
-------------
 Hardware fisik
```

- Contoh: **VirtualBox, VMware Workstation, Parallels**
- Mudah dipasang, cocok untuk laptop, belajar, dan testing
- Performa lebih rendah karena ada satu lapisan tambahan (Host OS)
- Analogi: penghuni yang sekaligus "mengelola" sendiri unit-unit sewaan di dalam apartemennya, jadi harus lewat aturan gedung dulu

---

### Perbandingan singkat

| Aspek | Tipe 1 (Bare-metal) | Tipe 2 (Hosted) |
|---|---|---|
| Posisi | Langsung di hardware | Di atas Host OS |
| Performa | Tinggi | Lebih rendah |
| Penggunaan | Server, data center, cloud | Laptop, desktop, belajar |
| Contoh | ESXi, Hyper-V, KVM, Xen | VirtualBox, VMware Workstation |

**Catatan:** batas antara dua tipe ini kadang kabur. **KVM** adalah modul di dalam kernel Linux, jadi secara teknis Linux-nya sendiri berubah fungsi menjadi hypervisor tipe 1. **Hyper-V** juga begitu: meski terlihat seperti fitur di Windows, saat aktif ia sebenarnya berjalan di bawah Windows dan menjadikannya "VM utama". Jadi jangan terlalu kaku soal kategori, yang penting paham posisi lapisannya.

---

### Cek pemahaman

Coba jawab dengan kata-katamu sendiri:
*Kalau kamu install VirtualBox di laptop untuk menjalankan Ubuntu, itu hypervisor tipe berapa, dan kenapa?*

Kalau sudah nangkep, kita lanjut ke **Fase 3: Cara kerja virtualisasi**, yaitu bagaimana CPU, memori, storage, dan network benar-benar "dipalsukan" untuk tiap VM.