## Atomic Operation

**Atomic operation** adalah operasi yang berjalan sebagai satu unit yang tidak bisa dibagi (*indivisible*) — artinya operasi tersebut **selesai sepenuhnya atau tidak sama sekali**, tanpa ada state perantara yang terlihat oleh thread/proses lain.

### Analogi Sederhana

Bayangkan transfer uang dari rekening A ke B:
1. Kurangi saldo A
2. Tambah saldo B

Jika langkah 1 selesai tapi langkah 2 gagal, uang "hilang". Dengan atomic operation, kedua langkah dianggap satu unit — jika salah satu gagal, semuanya dibatalkan.

---

### Masalah yang Diselesaikan

**Race condition** terjadi ketika dua thread mengakses data yang sama secara bersamaan:

```
Thread 1: baca counter (nilai = 5)
Thread 2: baca counter (nilai = 5)   ← baca sebelum Thread 1 menulis
Thread 1: tulis counter = 6
Thread 2: tulis counter = 6          ← harusnya 7!
```

Dengan atomic operation, operasi `baca-ubah-tulis` tidak bisa diinterupsi di tengah jalan.

---

### Properti Utama (ACID-like untuk operasi tunggal)

| Properti | Penjelasan |
|---|---|
| **Indivisible** | Tidak bisa dipotong di tengah eksekusi |
| **Isolated** | Thread lain tidak bisa melihat state perantara |
| **Consistent** | Data selalu dalam state yang valid |

---

### Contoh di Berbagai Bahasa

**Go:**
```go
import "sync/atomic"

var counter int64
atomic.AddInt64(&counter, 1)  // aman untuk concurrent access
```

**Java:**
```java
AtomicInteger counter = new AtomicInteger(0);
counter.incrementAndGet();  // atomic, thread-safe
```

**C++ (std::atomic):**
```cpp
std::atomic<int> counter(0);
counter++;  // atomic increment
```

**Python:**
```python
import threading
lock = threading.Lock()
with lock:
    counter += 1  # lock membuat operasi menjadi atomic
```

---

### Operasi yang Umum Bersifat Atomic

- **Compare-And-Swap (CAS)** — bandingkan nilai, tukar jika sesuai
- **Fetch-And-Add** — ambil nilai lama, tambahkan nilai baru
- **Test-And-Set** — set bit dan kembalikan nilai lama
- **Load/Store** — pada beberapa arsitektur, untuk tipe data tertentu

---

### Implementasi di Level Hardware

CPU modern menyediakan instruksi atomic seperti:
- `LOCK CMPXCHG` (x86) — Compare and Exchange
- `LDREX/STREX` (ARM) — Load/Store Exclusive

Ini adalah fondasi dari semua mekanisme sinkronisasi di level tinggi (mutex, semaphore, dll).

---

### Atomic vs Lock

| | **Atomic Operation** | **Lock (Mutex)** |
|---|---|---|
| Performa | Lebih cepat | Lebih lambat |
| Kompleksitas | Sederhana | Lebih kompleks |
| Granularitas | Per-operasi | Per-blok kode |
| Blocking | Non-blocking | Bisa blocking |

---

### Kapan Menggunakan?

- **Gunakan atomic** untuk operasi sederhana: counter, flag, pointer swap
- **Gunakan lock/mutex** untuk operasi kompleks yang melibatkan banyak variabel atau logika panjang

Atomic operation adalah fondasi dari *lock-free* dan *wait-free* programming yang digunakan dalam sistem berperforma tinggi.