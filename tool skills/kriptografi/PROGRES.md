# PROGRES — Kriptografi (zero to hero)

## Posisi saat ini
- Tahap: 1 — Fondasi
- Konsep aktif: Prinsip Kerckhoffs (sesi 2 berjalan, menunggu jawaban latihan)
- Status: sesi 1 selesai

## Roadmap

### Tahap 1 — Fondasi
1. Plaintext, Ciphertext, Key, Cipher
2. Prinsip Kerckhoffs
3. Tujuan keamanan: Confidentiality, Integrity, Authentication, Non-repudiation
4. Classical cipher: Caesar, Vigenère (dan kenapa mudah dipecahkan)
5. Entropy dan Randomness (CSPRNG)

### Tahap 2 — Symmetric Encryption
1. XOR dan One-Time Pad
2. Stream cipher
3. Block cipher dan AES
4. Mode operasi: ECB, CBC, CTR, GCM
5. Padding dan IV/Nonce
6. Authenticated Encryption (AEAD)

### Tahap 3 — Hashing dan Integritas
1. Cryptographic Hash (SHA-2, SHA-3), sifat-sifatnya
2. Collision, Preimage resistance
3. MAC dan HMAC
4. Password hashing: salt, bcrypt, scrypt, Argon2
5. KDF (PBKDF2, HKDF)

### Tahap 4 — Asymmetric Cryptography
1. Modular arithmetic (dasar matematika)
2. Diffie-Hellman key exchange
3. RSA
4. Elliptic Curve Cryptography (ECC)
5. Digital Signature (RSA, ECDSA, Ed25519)

### Tahap 5 — Protokol dan PKI
1. Certificate, X.509, Certificate Authority, chain of trust
2. TLS handshake
3. SSH, PGP/GPG
4. Perfect Forward Secrecy
5. Key management (HSM, KMS, rotation)

### Tahap 6 — Serangan dan Praktik Aman
1. Padding oracle, timing attack, side-channel
2. Nonce reuse, weak RNG, kesalahan implementasi umum
3. Prinsip "jangan bikin crypto sendiri"
4. Post-quantum cryptography
5. Proyek akhir (30-Proyek/)

## Konsep selesai
- Plaintext, Ciphertext, Key, Cipher (status: paham) → 20-Konsep/Plaintext-Ciphertext-Key-Cipher.md

## Jawaban latihan
- Latihan 01 (40-Latihan/): no.1 sebagian benar (salah menyebut AES sebagai ciphertext, key/cipher dikosongkan), no.2 benar, no.3 benar (HELLO). Cek cepat ulang: benar semua (HALO/MFQT/5/caesar).

## Topik berikutnya
Prinsip Kerckhoffs (sedang berjalan), lalu Tujuan keamanan (CIA)
