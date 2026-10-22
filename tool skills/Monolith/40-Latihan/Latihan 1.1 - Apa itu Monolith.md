---
tags: [latihan, monolith]
tahap: 1
status: belajar
---

# Latihan 1.1 - Apa itu Monolith

Konsep: [[Apa itu Monolith]]

> [!question] soal
> 1. Apakah sistem yang kamu kenal itu monolith? Buktikan dengan 3 ciri (codebase, artifact deploy, runtime).
> 2. Kalau satu modul diubah, apa yang harus di-deploy ulang?

## Jawaban
1. Ya.
   - BE dan FE dalam 1 repo.
   - BE dan FE dalam 1 VM.
   - Jika ada perubahan, semua fitur ikut ter-deploy.
2. Semua modul dalam 1 repo itu.

## Review tutor
- Ciri 1 benar (satu codebase).
- Ciri 2 kurang tepat: "1 VM" adalah lokasi deploy, bukan artifact atau proses runtime. Perlu dicek apakah BE dan FE satu paket dan satu proses.
- Ciri 3 benar, merupakan akibat dari satu artifact deploy. Sebutkan artifact-nya secara eksplisit.
- Soal 2 benar.
