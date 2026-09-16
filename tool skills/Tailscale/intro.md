# Tailscale — Penjelasan Lengkap

## Apa itu Tailscale?

Tailscale adalah **VPN mesh berbasis WireGuard** yang menghubungkan perangkat-perangkat kamu secara langsung (peer-to-peer), tanpa perlu konfigurasi router atau port forwarding.

Analoginya: semua perangkat yang join Tailscale seolah-olah berada dalam **satu jaringan LAN yang sama**, padahal fisiknya beda kota/negara.

---

## Cara Kerja Teknis

```
Laptop Kamu ──── Tailscale Network (mesh) ──── Laptop Teman
                        │                            │
                   Koordinasi via                 Konek VPN
                  Tailscale Server               Kantor/dll
                  (hanya signaling,
                  data tidak lewat sini)
```

- **Control plane** (koordinasi/autentikasi) → lewat server Tailscale
- **Data plane** (trafik aktual) → **langsung peer-to-peer** via WireGuard
- Kalau P2P tidak bisa (double NAT dll) → relay lewat **DERP server** Tailscale

---

## Konsep Penting

### 1. Tailnet
Jaringan private kamu di Tailscale. Semua device yang login ke akun yang sama otomatis masuk tailnet yang sama.

### 2. MagicDNS
Setiap device dapat nama DNS otomatis, misal:
- `laptop-teman.tail1234.ts.net`
- Bisa ping/SSH pakai nama, tidak perlu hafal IP

### 3. IP Tailscale (100.x.x.x)
Setiap device dapat IP di range `100.64.0.0/10`, misal:
- Laptop kamu: `100.64.0.1`
- Laptop teman: `100.64.0.2`

### 4. Exit Node ⭐ *(ini yang kamu butuhkan)*
Device tertentu bisa dijadikan "pintu keluar" internet untuk device lain di tailnet. Trafik kamu → lewat laptop teman → keluar via VPN teman.

### 5. Subnet Router
Device bisa mengekspos subnet lokal (misal `192.168.1.0/24`) ke seluruh tailnet. Berguna untuk akses resource jaringan kantor.

---

## Setup untuk Kasus Kamu

### Di laptop teman:
```bash
# Install Tailscale, login
# Lalu aktifkan sebagai exit node:
tailscale up --advertise-exit-node
```
Atau via GUI: **Tailscale tray icon → Exit Node → Allow as Exit Node**

### Di laptop kamu:
```bash
# Install Tailscale, login akun yang sama
# Pilih laptop teman sebagai exit node:
tailscale up --exit-node=100.64.0.2  # IP tailscale laptop teman
```
Atau via GUI: **Tailscale tray icon → Use Exit Node → pilih laptop teman**

---

## Fitur Unggulan Lainnya

| Fitur | Keterangan |
|---|---|
| **Works behind NAT** | Tidak perlu buka port di router |
| **Multi-platform** | Windows, Mac, Linux, iOS, Android |
| **ACL / Policy** | Bisa atur siapa bisa akses apa |
| **Taildrop** | Transfer file antar device |
| **Funnel** | Expose service lokal ke internet |
| **SSH via Tailscale** | SSH tanpa konfigurasi tambahan |

---

## Gratis atau Berbayar?

| Plan | Harga | Device | User |
|---|---|---|---|
| **Personal** | Gratis | 100 device | 1 user |
| **Plus** | ~$6/bulan | 100 device | 1 user + lebih banyak fitur |
| **Business** | ~$6/user/bulan | Unlimited | Multi-user + ACL advanced |

> Untuk kasus kamu dan teman → **Personal (Gratis) sudah lebih dari cukup**

---

## Keamanan

- Enkripsi **WireGuard** (state-of-the-art, lebih cepat dari OpenVPN)
- Autentikasi via **SSO** (Google, GitHub, Microsoft, dll)
- Tailscale server **tidak bisa baca trafik** kamu (hanya koordinasi)
- Setiap device harus di-approve secara eksplisit

---

## Alternatif Tailscale

| Produk | Keterangan |
|---|---|
| **ZeroTier** | Mirip, tapi lebih kompleks konfigurasinya |
| **Headscale** | Self-hosted versi open source dari Tailscale |
| **Netbird** | Open source, self-hostable |

Tailscale tetap yang paling mudah untuk setup cepat.

---

Mau langkah instalasi step-by-step untuk Windows/Mac/Linux?