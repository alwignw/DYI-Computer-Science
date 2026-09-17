## Thread

**Thread** (atau *thread of execution*) adalah unit terkecil dari eksekusi yang bisa dijalankan oleh CPU. Dalam satu program, bisa ada banyak thread yang berjalan **secara bersamaan** (concurrent).

---

### Analogi

Bayangkan sebuah **restoran**:

- **Program** = restoran
- **Proses** = dapur restoran
- **Thread** = masing-masing koki di dapur

Semua koki berbagi dapur yang sama (memori, alat), tapi masing-masing mengerjakan tugasnya sendiri secara paralel.

---

### Thread vs Proses

| | **Proses** | **Thread** |
|---|---|---|
| Memori | Memori sendiri (isolated) | Berbagi memori dengan thread lain |
| Komunikasi | Lebih sulit (IPC) | Mudah (shared memory) |
| Overhead | Berat | Ringan |
| Crash | Tidak mempengaruhi proses lain | Bisa crash seluruh program |
| Contoh | Tab browser berbeda | Tab loading + UI tetap responsif |

---

### Cara Kerja Thread

```
Program berjalan
       │
       ▼
   Main Thread
       │
       ├──── Thread 1 → download file
       ├──── Thread 2 → update UI
       └──── Thread 3 → proses data
```

Semua thread berbagi:
- **Heap** (memori dinamis)
- **Global variables**
- **File descriptors**

Setiap thread punya sendiri:
- **Stack** (variabel lokal)
- **Program Counter** (posisi eksekusi)
- **Register CPU**

---

### Contoh Kode

**Python:**
```python
import threading

def download_file(url):
    print(f"Downloading {url}...")
    # ... proses download

# Tanpa thread — sequential
download_file("file1.zip")  # tunggu selesai dulu
download_file("file2.zip")  # baru jalan

# Dengan thread — parallel
t1 = threading.Thread(target=download_file, args=("file1.zip",))
t2 = threading.Thread(target=download_file, args=("file2.zip",))

t1.start()
t2.start()

t1.join()  # tunggu t1 selesai
t2.join()  # tunggu t2 selesai
```

**Go (Goroutine — thread ringan):**
```go
go downloadFile("file1.zip")  // jalankan di goroutine
go downloadFile("file2.zip")
```

**Java:**
```java
Thread t1 = new Thread(() -> downloadFile("file1.zip"));
Thread t2 = new Thread(() -> downloadFile("file2.zip"));
t1.start();
t2.start();
```

---

### Jenis Thread

**1. User-level Thread**
- Dikelola oleh program/library, bukan OS
- Lebih cepat dibuat
- Contoh: goroutine (Go), green thread

**2. Kernel-level Thread**
- Dikelola langsung oleh OS
- Bisa berjalan di CPU core berbeda
- Contoh: thread di Java, Python, C++

---

### Masalah Umum dengan Thread

**1. Race Condition** — dua thread mengubah data bersamaan
```
Thread 1 dan Thread 2 sama-sama baca counter = 5
Keduanya tambah 1
Keduanya tulis 6  ← harusnya 7!
```

**2. Deadlock** — dua thread saling menunggu satu sama lain
```
Thread 1 pegang Lock A, tunggu Lock B
Thread 2 pegang Lock B, tunggu Lock A
→ keduanya stuck selamanya
```

**3. Starvation** — satu thread tidak pernah dapat giliran CPU

---

### Solusi Masalah Thread

| Masalah | Solusi |
|---|---|
| Race condition | Mutex, atomic operation, lock |
| Deadlock | Urutan lock yang konsisten, timeout |
| Overhead banyak thread | Thread pool |

---

### Thread Pool

Daripada membuat thread baru setiap ada tugas (mahal), gunakan **pool of threads** yang siap pakai:

```
[Task Queue] → | Thread 1 |
               | Thread 2 | → hasil
               | Thread 3 |
```

Contoh di Python:
```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=4) as executor:
    executor.submit(download_file, "file1.zip")
    executor.submit(download_file, "file2.zip")
    executor.submit(download_file, "file3.zip")
```

---

### Kapan Pakai Thread?

- ✅ **I/O bound** — download, baca file, query database (thread sangat efektif)
- ✅ **UI tetap responsif** — proses berat di background thread
- ⚠️ **CPU bound** — untuk kalkulasi berat, pertimbangkan **multiprocessing** (terutama di Python karena GIL)

Thread adalah fondasi dari program modern yang responsif dan efisien — dari aplikasi mobile, web server, hingga game engine.