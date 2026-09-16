## Latar Belakang TanStack Query

---

### 😤 Masalah yang Ada Sebelumnya

Sebelum TanStack Query lahir, developer mengelola **server state secara manual** — dan ini menyakitkan.

**Kode yang umum ditulis sebelum ada Vue Query:**

```js
// ❌ Pola manual yang berulang di SETIAP komponen
const users   = ref([])
const loading = ref(false)
const error   = ref(null)

onMounted(async () => {
  loading.value = true
  try {
    const res  = await fetch('/api/users')
    users.value = await res.json()
  } catch (err) {
    error.value = err
  } finally {
    loading.value = false
  }
})
```

Masalahnya — kode ini **ditulis ulang di ratusan komponen**, dengan variasi yang tidak konsisten.

---

### 🧠 Insight Inti — Dua Jenis State

**Tanner Linsley** (pembuat library ini) menyadari sesuatu yang sering diabaikan:

```
State dalam aplikasi sebenarnya ada DUA jenis yang SANGAT berbeda:

┌─────────────────────────────────────────────────────────┐
│  CLIENT STATE                   SERVER STATE            │
│  ─────────────                  ─────────────           │
│  • Modal buka/tutup             • Data dari API         │
│  • Tab aktif                    • List produk           │
│  • Form input                   • Profil user           │
│  • Theme (dark/light)           • Notifikasi            │
│                                                         │
│  Kamu yang kontrol penuh        Kamu TIDAK kontrol      │
│  Hidup di memori browser        Hidup di server/DB      │
│  Sinkron                        Asinkron                │
│  Tidak expired                  Bisa berubah kapan saja │
└─────────────────────────────────────────────────────────┘
```

> **Masalahnya:** Developer selama ini mengelola keduanya dengan cara yang **sama** — padahal karakteristiknya sangat berbeda.

---

### 💥 Pain Points Nyata yang Mendorong Lahirnya Library Ini

**1. Tidak ada caching — fetch berulang terus**

```
User buka halaman /users     → fetch /api/users  ✅
User pindah ke /profile      → (data users buang)
User balik ke /users         → fetch /api/users LAGI 😤
User pindah ke /profile      → (data users buang lagi)
...terus berulang
```

**2. Race condition tidak tertangani**

```js
// ❌ User ketik cepat di search box
// Request 1: "a"    → lambat  → response datang BELAKANGAN
// Request 2: "ab"   → cepat   → response datang duluan
// Request 3: "abu"  → cepat   → response datang duluan

// UI tampil hasil "a" padahal user sudah ketik "abu" 💥
// Tidak ada yang handle ini secara otomatis
```

**3. Data tidak pernah sinkron dengan server**

```
User buka tab browser jam 09:00  → data loaded
User pergi meeting sampai jam 11:00
User balik, lihat halaman        → data MASIH sama dari jam 09:00
                                    padahal data di server sudah berubah
                                    tidak ada yang trigger refresh 😤
```

**4. Loading state yang inkonsisten**

```js
// Komponen A
const isLoading = ref(false)    // naming berbeda-beda

// Komponen B
const fetching  = ref(false)    // tidak ada standar

// Komponen C
const pending   = ref(false)    // tiap developer beda gaya
```

**5. Tidak ada deduplication**

```
Komponen Header     → fetch /api/profile  ─┐
Komponen Sidebar    → fetch /api/profile  ─┼─ 3 request ke server
Komponen Dashboard  → fetch /api/profile  ─┘   padahal data SAMA
                                               cukup 1 request! 😤
```

**6. Manajemen state yang membengkak**

```js
// Vuex / Pinia store penuh dengan boilerplate server state
const store = {
  state: {
    users:        [],
    usersLoading: false,
    usersError:   null,
    user:         null,
    userLoading:  false,
    userError:    null,
    posts:        [],
    postsLoading: false,
    postsError:   null,
    // ... bisa ratusan baris hanya untuk loading/error state
  },
  actions: {
    async fetchUsers({ commit }) {
      commit('SET_USERS_LOADING', true)
      try {
        const data = await api.get('/users')
        commit('SET_USERS', data)
      } catch (e) {
        commit('SET_USERS_ERROR', e)
      } finally {
        commit('SET_USERS_LOADING', false)
      }
    },
    // ... action yang sama berulang untuk setiap entitas
  }
}
```

---

### 💡 Solusi yang Ditawarkan

Tanner Linsley merilis **React Query v1 di 2019**, dengan filosofi:

> *"Server state punya kebutuhan yang unik — biarkan library yang mengurus kompleksitasnya, bukan developer."*

```
Yang diotomasi library ini:

  ✅ Caching otomatis          → tidak perlu fetch ulang data yang sama
  ✅ Background sync           → data selalu fresh tanpa user refresh manual
  ✅ Deduplication             → 100 komponen request sama = 1 network call
  ✅ Loading & error state     → tidak perlu ref(false) manual lagi
  ✅ Race condition handling   → request lama otomatis dibatalkan
  ✅ Retry otomatis            → network blip? coba lagi sendiri
  ✅ Pagination & infinite     → pola kompleks jadi sederhana
  ✅ Optimistic updates        → UI terasa instan
```

---

### 📅 Timeline Perjalanannya

```
2019  →  Tanner Linsley rilis React Query v1
          mulai viral di komunitas React

2020  →  React Query v2 & v3
          adopsi masif, jadi standar de facto

2022  →  Rebranding jadi "TanStack Query v4"
          alasan: tidak lagi React-only

          Hadir untuk:
          ├── React    (react-query)
          ├── Vue      (vue-query)      ← yang kita pelajari
          ├── Svelte   (svelte-query)
          └── Solid    (solid-query)

2023  →  TanStack Query v5
          TypeScript-first, API lebih konsisten,
          bundle size lebih kecil
```

---

### 🎯 Filosofi Akhirnya

```
Sebelum TanStack Query:          Sesudah TanStack Query:

Vuex/Pinia                       Vuex/Pinia
  └── client state ✅              └── client state ✅
  └── server state 😤                  (tidak perlu simpan
      (loading, error,                  server state di sini)
       cache, sync — manual)
                                   TanStack Query
                                    └── server state ✅
                                        (otomatis semua)
```

> **Intinya** — library ini lahir karena komunitas sadar bahwa **server state bukan sekadar data yang disimpan di Vuex/Redux**, tapi sesuatu yang punya siklus hidup sendiri: *asinkron, bisa expired, bisa berubah di server kapan saja* — dan butuh tool khusus untuk mengelolanya dengan benar.

---

Mau dibuatkan **cheatsheet visual** semua konsep yang sudah dipelajari?