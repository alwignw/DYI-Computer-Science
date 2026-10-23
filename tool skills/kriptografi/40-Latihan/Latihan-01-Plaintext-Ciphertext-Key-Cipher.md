---
tags: [latihan, kriptografi]
tahap: 1
status: belajar
---

# Latihan 01 — Plaintext, Ciphertext, Key, Cipher

Konsep: [[Plaintext-Ciphertext-Key-Cipher]]

> [!question] Soal
> Data gaji karyawan dienkripsi dengan AES. File ciphertext dan file key ada di folder yang sama di server yang sama.
> 1. Tunjuk plaintext, ciphertext, key, cipher.
> 2. Apakah data aman jika server diretas?
> 3. Dekripsi Caesar (key = 3): `KHOOR`.

## Jawaban saya
1. plaintext = data gaji karyawan, ciphertext = AES, key = ?, cipher = ?
2. Tidak, karena key ditaruh di folder yang sama di server yang sama.
3. Hello

## Koreksi
1. **Sebagian benar.** Plaintext benar. Yang keliru: AES adalah **cipher**, bukan ciphertext. Ciphertext = file gaji yang sudah terenkripsi. Key = file berisi key itu.
2. **Benar.** Penyerang yang masuk ke server mengambil ciphertext sekaligus key, jadi enkripsi tidak berguna. Key harus dipisah (KMS/HSM).
3. **Benar.** `HELLO` (K→H, H→E, O→L, O→L, R→O).

## Cek cepat (ulang)
> [!question] Caesar key 5: `HALO` → `MFQT`. Sebutkan keempat komponen.

Jawaban saya: plaintext = HALO, ciphertext = MFQT, key = 5, cipher = caesar.

Koreksi: **Benar semua.** Pembedaan cipher vs ciphertext sudah tepat.
