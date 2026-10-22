# PROGRES Belajar Reverse Engineering

> Posisi saat ini: **Konsep 2.2 selesai. Berikutnya: 2.3 Stack dan heap (belum dimulai).**

## Roadmap

### Tahap 1 – Fondasi
- [x] 1.1 Apa itu Reverse Engineering (tujuan, jenis, batas legal/etika)
- [x] 1.2 Bit, byte, dan bilangan hexadecimal
- [x] 1.3 Endianness
- [x] 1.4 Encoding teks (ASCII, UTF-8)

### Tahap 2 – Cara program berjalan
- [x] 2.1 Dari source code ke binary (compile, link)
- [x] 2.2 CPU, register, dan memory
- [ ] 2.3 Stack dan heap
- [ ] 2.4 Format executable (Mach-O, ELF, PE)

### Tahap 3 – Assembly dasar
- [ ] 3.1 Instruksi dan operand
- [ ] 3.2 Data movement & aritmetika
- [ ] 3.3 Control flow (jump, compare, loop)
- [ ] 3.4 Function call & calling convention

### Tahap 4 – Static analysis
- [ ] 4.1 `file`, `strings`, `otool`/`objdump`
- [ ] 4.2 Disassembler & Ghidra
- [ ] 4.3 Membaca decompiler output

### Tahap 5 – Dynamic analysis
- [ ] 5.1 Debugger (lldb): breakpoint, step, inspect
- [ ] 5.2 Tracing syscall & library call
- [ ] 5.3 Patching sederhana

### Tahap 6 – Di luar native binary
- [ ] 6.1 Bytecode (Java/.NET) & decompiling
- [ ] 6.2 Aplikasi web/JS & obfuscation
- [ ] 6.3 Protokol jaringan & API (relevan untuk peran arsitek)

### Tahap 7 – Praktik & proyek
- [ ] 7.1 Crackme latihan
- [ ] 7.2 Analisis binary/library nyata untuk proyek kerja

## Jawaban latihan
- **1.1** Situasi: aplikasi lawas tanpa source, tidak kompatibel Windows 11. Ingin tahu flow & logic. Pilih static (alasan: menganalisis file hasil install). Koreksi: static bagus sebagai awal, tapi untuk logic dan diagnosis kegagalan di Win 11 perlu dynamic juga. Detail: [[Latihan 1.1 - Apa itu Reverse Engineering]]
- **1.2** Biner→hex benar (0x3C), tapi konversi hex→desimal salah di soal 1 (15, seharusnya 60) dan 2 (12, seharusnya 42) karena lupa bobot ×16. Soal 3 benar (0xFFFF = 65.535; 3 byte = 0xFFFFFF). Detail: [[Latihan 1.2 - Bit, byte, dan hexadecimal]]
- **1.3** Soal 1 tertukar (little-endian ditulis `AA BB CC DD`, seharusnya `DD CC BB AA`). Soal 2 benar (42, balik byte lalu bobot). Soal 3 benar (0x1F = 31). Detail: [[Latihan 1.3 - Endianness]]
- **1.4** Soal 1 benar (REVERSE). Soal 2 salah (`"Go"` ditulis `0x424342`, seharusnya `47 6F 00`; belum bisa mencari kode ASCII dari huruf). Soal 3 benar (`z`, `5A`, 1 byte). Soal 4 benar, label little/big sudah tidak tertukar (catatan: tulis per byte, bukan `0x...`). Detail: [[Latihan 1.4 - Encoding teks]]
- **2.1** Semua benar: library eksternal masih terlihat, simbol/nama fungsi lokal hilang karena strip, nama variabel lokal hilang saat compile. Ulangan `"Hi"` = `48 69 00` benar (kelemahan ASCII sudah teratasi). Detail: [[Latihan 2.1 - Dari source code ke binary]]
- **2.2** Semua benar: siklus Fetch–Decode–Execute + `rip`/`pc`; `rax` = 16 (little-endian dibalik dengan benar, konversi hex→desimal sudah tepat); beda register vs memory dengan kata "alamat". Detail: [[Latihan 2.2 - CPU, register, dan memory]]

## Topik berikutnya
2.3 Stack dan heap (butuh dasar 2.2: register `rsp`, memory, alamat).
