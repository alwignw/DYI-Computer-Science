Oke, saya akan buatkan roadmap belajar load balancer yang terstruktur!

---

## Roadmap Belajar Load Balancer

---

### 🟢 Fase 1 — Fondasi (Apa & Kenapa)
*Tujuan: paham konsep dasar sebelum masuk ke teknis*

1. **Apa itu load balancer** — definisi, analogi, masalah yang dipecahkan
2. **High Availability vs Scalability** — bedanya dan kenapa LB mendukung keduanya
3. **Horizontal vs Vertical Scaling** — konteks kenapa LB dibutuhkan
4. **Komponen dasar** — client, load balancer, backend server, health check

---

### 🔵 Fase 2 — Cara Kerja (Mekanisme)
*Tujuan: paham bagaimana LB mendistribusikan traffic*

1. **Algoritma load balancing:**
   - Round Robin
   - Weighted Round Robin
   - Least Connections
   - IP Hash / Sticky Session
   - Random
2. **Health Check** — bagaimana LB mendeteksi server mati dan mengalihkan traffic
3. **Session Persistence (Sticky Sessions)** — kapan diperlukan dan risikonya

---

### 🟡 Fase 3 — Level Operasi (Layer 4 vs Layer 7)
*Tujuan: paham LB bekerja di level mana dalam jaringan*

1. **Layer 4 Load Balancer** — bekerja di transport layer (TCP/UDP), cepat, terbatas
2. **Layer 7 Load Balancer** — bekerja di application layer (HTTP/HTTPS), lebih cerdas
3. **Kapan pakai L4 vs L7** — trade-off performa vs fleksibilitas
4. **Content-based routing** — L7 bisa route berdasarkan URL, header, cookie

---

### 🟠 Fase 4 — Jenis & Implementasi
*Tujuan: tahu pilihan LB di dunia nyata*

1. **Hardware LB** — F5, Citrix (mahal, performa tinggi)
2. **Software LB** — Nginx, HAProxy, Envoy (fleksibel, open source)
3. **Cloud-managed LB** — AWS ALB/NLB, GCP Load Balancer, Azure LB
4. **DNS Load Balancing** — cara paling sederhana via DNS round robin

---

### 🔴 Fase 5 — Topik Lanjutan (Architect Level)
*Tujuan: paham desain LB di sistem skala besar*

1. **Global Load Balancing (GSLB)** — distribusi traffic antar region/datacenter
2. **Load Balancer itu sendiri bisa jadi SPOF** — solusi: active-passive, active-active
3. **Anycast routing** — dipakai Cloudflare, Google untuk routing global
4. **Service Mesh** — LB di level microservices (Istio, Linkerd)
5. **Connection draining** — graceful shutdown tanpa putus koneksi aktif

---

Satu fase per sesi, atau mau langsung terjun ke **Fase 1** sekarang?