Siap Bos 🔥
Sekarang kita masuk ke **mode latihan + thinking seperti interview**.
Gue kasih beberapa **study case bertahap (dari easy → harder)** + cara kamu harus jawab.

---

# 🧪 LEVEL 1 — Basic (Fundamental Thinking)

## 📌 Case 1: URL Shortener

> Design sistem seperti Bitly

### 🎯 Tujuan:

User input URL panjang → output URL pendek

---

### 🧠 Yang harus kamu jawab:

Coba jawab ini satu per satu:

1. **Understand Problem**

   * Apakah URL expire?
   * Apakah perlu analytics (klik count)?

2. **Scope**

   * Fokus hanya:

     * shorten URL
     * redirect

3. **High-Level Design**

   * Komponen apa saja?

     * API?
     * Database?
     * Cache?

4. **Detail**

   * Bagaimana generate short URL?

     * random?
     * hash?
   * Bagaimana handle collision?

5. **Scaling**

   * Kalau 10 juta request per hari gimana?

---

👉 **Tugas kamu:**
Coba jawab step 1–5 (ringkas aja), nanti gue review.

---

# 🧪 LEVEL 2 — Intermediate

## 📌 Case 2: Chat System

> Design sistem seperti WhatsApp (basic version)

---

### 🎯 Fitur:

* Kirim pesan 1-1
* Real-time
* Online / offline

---

### 🧠 Yang harus kamu pikirkan:

#### 1. Requirement

* Real-time? (yes)
* Message disimpan? (yes)

#### 2. Scope

❌ Jangan bahas:

* Video call
* Story

✅ Fokus:

* send & receive message

---

#### 3. High-Level Design

Minimal ada:

* Client
* API / WebSocket server
* Message service
* Database

---

#### 4. Deep Thinking

* Real-time pakai apa?

  * Polling?
  * WebSocket?

* Kalau user offline?

  * Disimpan di mana?

* Message delivery:

  * at least once?
  * exactly once?

---

#### 5. Scaling

* Kalau 1 juta user online bersamaan?

---

👉 **Tugas kamu:**
Coba jelaskan:

* arsitektur
* flow kirim pesan

---

# 🧪 LEVEL 3 — Advanced (Mendekati Real World)

## 📌 Case 3: Notification System

> Design sistem notifikasi seperti:

* Gojek
* Tokopedia

---

### 🎯 Fitur:

* Push notification
* Email
* SMS
* Bisa broadcast

---

### 🧠 Yang harus kamu pikirkan:

#### 1. Problem

* Kirim notif ke jutaan user
* Tidak boleh lambat

---

#### 2. High-Level Design

Biasanya ada:

* Notification API
* Queue (WAJIB)
* Worker
* Provider (FCM, Email, SMS)

---

#### 3. Critical Thinking

* Kenapa harus pakai queue?
* Bagaimana retry kalau gagal?
* Bagaimana handle spam?

---

#### 4. Scaling

* Kirim 1 juta notif dalam 1 menit?

---

👉 **Tugas kamu:**
Jelaskan:

* Kenapa butuh queue
* Flow kirim notif

---

# 💡 Cara Jawab (Framework Wajib)

Setiap kamu jawab, pakai struktur ini:

```
1. Requirement
2. Scope
3. High-Level Design
4. Detail (opsional)
5. Scaling / Trade-off
```

---

# 🔥 Tips Penting (biar naik level cepat)

* Jangan langsung solusi → mulai dari **clarify problem**
* Selalu ngomongin:

  * scale
  * bottleneck
* Gambar di kepala:

  * “data mengalir ke mana?”

---

# 🚀 Challenge dari Gue (Rekomendasi)

👉 Mulai dari ini dulu:

**Jawab Case 1 (URL Shortener)**
Dengan format:

```
Requirement:
Scope:
Design:
Scaling:
```

Nanti gue akan:
✅ Review seperti interviewer
✅ Kasih improvement
✅ Naikin level kamu ke architect mindset

Gas Bos 💪
