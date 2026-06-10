# PORTOFOLIO METODE NUMERIK

## Metode Newton-Raphson untuk Menyelesaikan Persamaan Nonlinier

### Identitas Mahasiswa

Nama : Muhammad Junabil

NIM : C2455201027

Program Studi : Teknik Informatika

---

## Deskripsi Proyek

Proyek ini merupakan tugas Portofolio Akhir Semester Mata Kuliah Metode Numerik.

Metode yang digunakan adalah Newton-Raphson untuk mencari akar persamaan:

f(x) = x³ - 2x - 5

---

## Model Matematika

Fungsi:

f(x) = x³ - 2x - 5

Turunan:

f'(x) = 3x² - 2

---

## Hasil

Akar Persamaan:

x = 2.0945514815

---

## File Repository

- newton_raphson.py
- hasil_program.png
- README.md

---

## Kesimpulan

Metode Newton-Raphson berhasil menentukan akar persamaan nonlinier dengan tingkat akurasi yang tinggi.

## Iterasi Manual Newton-Raphson

Persamaan:

f(x) = x³ - 2x - 5

Turunan:

f'(x) = 3x² - 2

Tebakan awal:

x₀ = 2

### Iterasi 1

Hitung nilai fungsi:

f(2) = 2³ - 2(2) - 5

f(2) = 8 - 4 - 5

f(2) = -1

Hitung turunan:

f'(2) = 3(2)² - 2

f'(2) = 12 - 2

f'(2) = 10

Gunakan rumus Newton-Raphson:

x₁ = x₀ - f(x₀)/f'(x₀)

x₁ = 2 - (-1/10)

x₁ = 2.100000

### Iterasi 2

Hitung nilai fungsi:

f(2.1) = (2.1)³ - 2(2.1) - 5

f(2.1) = 9.261 - 4.2 - 5

f(2.1) = 0.061

Hitung turunan:

f'(2.1) = 3(2.1)² - 2

f'(2.1) = 11.23

Hitung nilai berikutnya:

x₂ = 2.1 - (0.061 / 11.23)

x₂ = 2.094568

### Iterasi 3

Hitung nilai berikutnya:

x₃ = 2.094551

Karena perubahan nilai sudah sangat kecil, iterasi dihentikan.

### Hasil Akhir

Akar persamaan yang diperoleh:

x = 2.094551

## Analisis Error

Error relatif dihitung menggunakan:

Error = |(xₙ - xₙ₋₁) / xₙ| × 100%

Dari hasil iterasi diperoleh nilai error yang sangat kecil dan mendekati nol.

Hal ini menunjukkan bahwa metode Newton-Raphson telah mencapai konvergensi dan menghasilkan solusi yang akurat.

### Kesimpulan

Metode Newton-Raphson berhasil digunakan untuk menyelesaikan persamaan nonlinier:

f(x) = x³ - 2x - 5

Hasil akar persamaan yang diperoleh adalah:

x = 2.094551

Dengan error yang sangat kecil, hasil perhitungan dapat dianggap valid dan akurat.


