TanStack Vue Query — Konsep Dasar

🌐 Server State

Server State adalah data yang tidak kamu miliki — data itu tinggal di server, bukan di memori aplikasi kamu.

Karakteristiknya:

- Tersimpan di tempat yang tidak kamu kontrol (database, API)
- Bisa berubah kapan saja tanpa sepengetahuan UI kamu
- Perlu di-fetch, cache, sync, dan update secara asinkron
- Berbeda dari UI state (modal buka/tutup, tab aktif) yang hidup di client

Contoh: daftar user dari GET /api/users, data profil, list produk — semua itu Server State.


TanStack Query hadir justru untuk mengelola kerumitan server state ini (loading, error, caching, refetch, stale, dll).


