# PROGRES Belajar Backup (OT/ICS)

Posisi saat ini: **Tahap 1 – siap mulai Konsep 1.2 Backup vs Archive vs Replication**

## Roadmap

### Tahap 1 – Fondasi
- [x] 1.1 Backup (definisi & tujuan)
- [ ] 1.2 Backup vs Archive vs Replication
- [ ] 1.3 RPO & RTO
- [ ] 1.4 Aturan 3-2-1 (3-2-1-1-0)
- [ ] 1.5 Jenis backup: Full, Incremental, Differential
- [ ] 1.6 Retention & Rotation

### Tahap 2 – Backup Software & Hardware
- [ ] 2.1 File-level vs Block-level vs Image-level backup
- [ ] 2.2 Snapshot & Copy-on-Write
- [ ] 2.3 Media backup: disk, tape (LTO), NAS, object storage
- [ ] 2.4 Deduplication & Compression
- [ ] 2.5 Encryption & Immutability (anti-ransomware)
- [ ] 2.6 Agent vs Agentless, Application-consistent (VSS)

### Tahap 3 – Backup Sistem & Virtualisasi
- [ ] 3.1 Bare-metal backup & restore
- [ ] 3.2 Backup VM (hypervisor-level)
- [ ] 3.3 Backup database
- [ ] 3.4 Backup konfigurasi (network, PLC, HMI)
- [ ] 3.5 Restore testing & verifikasi integritas

### Tahap 4 – Backup di OT/ICS
- [ ] 4.1 Karakteristik OT: legacy OS, 24/7, air-gapped
- [ ] 4.2 Backup SCADA / HMI / Historian
- [ ] 4.3 Backup PLC/DCS project & firmware
- [ ] 4.4 Purdue Model & penempatan backup server
- [ ] 4.5 Backup di jaringan air-gapped / DMZ

### Tahap 5 – P2V & Migrasi Industri
- [ ] 5.1 Konsep P2V sebagai backup + migrasi
- [ ] 5.2 Image fisik sebelum P2V (rollback plan)
- [ ] 5.3 Validasi pasca-P2V
- [ ] 5.4 Fallback & cutover plan

### Tahap 6 – DR & BCP Industri
- [ ] 6.1 Disaster Recovery (DR) vs Business Continuity (BCP)
- [ ] 6.2 DR site: cold / warm / hot
- [ ] 6.3 DR runbook & drill
- [ ] 6.4 Standar: IEC 62443, NIST SP 800-82

## Log Sesi
- 2026-10-15 Sesi 1: Konsep 1.1 Backup. Catatan: [[Backup]]. MOC: [[MOC Tahap 1 - Fondasi]]

## Jawaban Latihan
- 1.1: benar (server rusak total, ransomware; backup belum terpisah fisik/infrastruktur). Detail: [[1.1 Backup]]

## Topik Berikutnya
1.2 Backup vs Archive vs Replication
