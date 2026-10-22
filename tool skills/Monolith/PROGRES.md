# PROGRES — Belajar Arsitektur Monolith

## Posisi saat ini
- Tahap: 1
- Konsep selesai: 1.1 (status: belajar)
- Konsep berikutnya: 1.2 Ciri-ciri aplikasi monolith
- Catatan: pertegas beda lokasi deploy (VM) vs artifact vs proses runtime

## Roadmap

### Tahap 1 — Dasar
- [x] 1.1 Apa itu Monolith (belajar)
- [ ] 1.2 Ciri-ciri aplikasi monolith (single codebase, single deployable, shared database)
- [ ] 1.3 Monolith vs Distributed system (gambaran singkat)

### Tahap 2 — Struktur internal
- [ ] 2.1 Layered architecture (presentation, business, data)
- [ ] 2.2 Separation of concerns
- [ ] 2.3 Coupling dan cohesion
- [ ] 2.4 Shared database dan transaksi ACID

### Tahap 3 — Modular Monolith
- [ ] 3.1 Module dan boundary
- [ ] 3.2 Dependency rule dan public API antar module
- [ ] 3.3 Domain-Driven Design dasar (bounded context)
- [ ] 3.4 Menjaga boundary (arsitektur test, package rules)

### Tahap 4 — Operasional
- [ ] 4.1 Build dan deployment satu artifact
- [ ] 4.2 Scaling monolith (vertical, horizontal, stateless)
- [ ] 4.3 Testing strategy
- [ ] 4.4 Observability (logging, monitoring)

### Tahap 5 — Evolusi
- [ ] 5.1 Kelebihan dan kekurangan monolith
- [ ] 5.2 Kapan monolith tepat dipilih
- [ ] 5.3 Technical debt dan "Big Ball of Mud"
- [ ] 5.4 Strangler Fig dan migrasi ke microservices

### Tahap 6 — Penerapan proyek
- [ ] 6.1 Review arsitektur proyek nyata (30-Proyek/)

## Riwayat sesi
- Sesi 1: 1.1 Apa itu Monolith. Catatan: [[Apa itu Monolith]]. MOC: [[MOC Tahap 1 - Dasar]].

## Jawaban latihan
- Latihan 1.1: ciri 1 dan 3 benar, ciri 2 ("1 VM") kurang tepat karena itu lokasi, bukan artifact/proses. Soal 2 benar. Detail: [[Latihan 1.1 - Apa itu Monolith]].
