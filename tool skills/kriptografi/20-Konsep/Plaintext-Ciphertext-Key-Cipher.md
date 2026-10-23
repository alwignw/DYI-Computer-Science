---
tags: [kriptografi, fondasi, terminologi]
tahap: 1
status: paham
---

# Plaintext, Ciphertext, Key, Cipher

Empat komponen dasar enkripsi: **plaintext** (pesan asli) diubah oleh **cipher** (algoritma) memakai **key** (rahasia) menjadi **ciphertext** (pesan teracak). Cipher bersifat publik, key bersifat rahasia (lihat [[Prinsip Kerckhoffs]]).

```
Plaintext --[Encrypt(cipher + key)]--> Ciphertext --[Decrypt(cipher + key)]--> Plaintext
```

| Istilah | Arti | Analogi |
|---|---|---|
| Plaintext | Pesan asli yang bisa dibaca | Isi surat |
| Ciphertext | Hasil pengacakan | Surat dalam kotak terkunci |
| Key | Rahasia kecil pengendali proses | Kunci gembok |
| Cipher | Algoritma enkripsi/dekripsi | Mekanisme gembok |

Contoh mini ([[Caesar Cipher]]): `HALO` dengan key 3 menjadi `KDOR`.

> [!example] Contoh industri
> - Chat (WhatsApp): pesan = plaintext, AES = cipher, key hanya di perangkat pengirim dan penerima, server hanya melihat ciphertext.
> - Database KTP pelanggan: disimpan sebagai ciphertext, key disimpan terpisah di KMS/HSM.

> [!warning] Miskonsepsi
> - Cipher ≠ key. Cipher adalah metode, key adalah parameter rahasianya.
> - Algoritma rahasia tidak otomatis lebih aman.
> - Ciphertext yang tampak acak belum tentu aman jika key lemah atau cipher buruk.
> - AES adalah **cipher**, bukan ciphertext.

> [!question] Latihan
> Lihat [[Latihan-01-Plaintext-Ciphertext-Key-Cipher]].

MOC: [[MOC-Tahap-1-Fondasi]]
