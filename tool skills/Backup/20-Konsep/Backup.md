---
tags: [backup, fondasi]
tahap: 1
status: belajar
---

# Backup

**Backup adalah salinan data atau sistem yang disimpan terpisah dari aslinya, supaya kondisi tersebut bisa dikembalikan (restore) saat yang asli rusak, hilang, atau berubah.**

Kata kunci: **salinan** dan **terpisah**. Konsep terkait berikutnya: [[Backup vs Archive vs Replication]], [[RPO dan RTO]], [[Aturan 3-2-1]].

## Backup melindungi dari
- Kerusakan hardware (disk, PSU, motherboard)
- Kesalahan manusia (salah hapus / salah ubah konfigurasi)
- Serangan siber (ransomware)
- Bencana (banjir, kebakaran, listrik padam)
- Update atau perubahan yang gagal

## Dimensi "terpisah"
- **Fisik**: perangkat berbeda
- **Logis/akses**: kredensial dan jaringan berbeda, supaya ransomware tidak ikut mengenkripsi backup
- **Lokasi**: gedung atau site berbeda

> [!example] Contoh industri
> PC HMI (Windows 7 + SCADA lama) di lini botol rusak disk-nya. Tanpa backup, install ulang bisa berhari-hari (lisensi, tag, screen harus dibangun ulang). Dengan backup image, PC pengganti di-restore dalam hitungan jam. Downtime Rp50 juta/jam.

> [!warning] Miskonsepsi
> "Sudah ada RAID, berarti sudah di-backup." Salah. RAID melindungi dari kegagalan satu disk (availability), bukan dari salah hapus, korupsi, atau ransomware, karena semuanya ikut tersalin ke disk mirror. **RAID bukan backup.**

> [!question] Latihan
> Server Historian pakai RAID 1 dan folder `D:\Backup` di server yang sama. Sebutkan 2 skenario data tetap hilang dan kelemahan utamanya dari sisi "terpisah". Jawaban: [[1.1 Backup]]
