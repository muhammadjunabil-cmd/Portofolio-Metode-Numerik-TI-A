# PORTOFOLIO METODE NUMERIK

## Metode Newton-Raphson untuk Menyelesaikan Persamaan Nonlinier

### Identitas Mahasiswa

**Nama:** Muhammad Junabil

**NIM:** C2455201027

**Program Studi:** Teknik Informatika

**Mata Kuliah:** Metode Numerik


# Deskripsi Proyek

Proyek ini merupakan tugas Portofolio Akhir Semester Mata Kuliah Metode Numerik.

Pada proyek ini digunakan Metode Newton-Raphson untuk mencari akar dari persamaan nonlinier:

f(x) = x³ − 2x − 5

Metode Newton-Raphson dipilih karena memiliki tingkat konvergensi yang cepat dan mampu menghasilkan solusi yang akurat dengan jumlah iterasi yang relatif sedikit.


# Model Matematika

Fungsi yang digunakan:

f(x) = x³ − 2x − 5

Turunan fungsi:

f'(x) = 3x² − 2

Tujuan perhitungan adalah mencari nilai x yang memenuhi:

f(x) = 0


# Metode Newton-Raphson

Rumus Newton-Raphson:

x(n+1) = x(n) − f(x(n)) / f'(x(n))

Keterangan:

* x(n) = nilai iterasi saat ini
* x(n+1) = nilai iterasi berikutnya
* f(x) = fungsi
* f'(x) = turunan fungsi

Langkah-langkah metode:

1. Menentukan nilai awal (x₀)
2. Menghitung f(x)
3. Menghitung f'(x)
4. Menghitung nilai x baru
5. Mengulangi proses hingga error mendekati nol


# Iterasi Manual

Tebakan awal:

x₀ = 2

## Iterasi 1

f(2) = 2³ − 2(2) − 5

f(2) = 8 − 4 − 5

f(2) = −1

f'(2) = 3(2)² − 2

f'(2) = 12 − 2

f'(2) = 10

x₁ = 2 − (−1 / 10)

x₁ = 2.100000


## Iterasi 2

f(2.1) = (2.1)³ − 2(2.1) − 5

f(2.1) = 9.261 − 4.2 − 5

f(2.1) = 0.061

f'(2.1) = 3(2.1)² − 2

f'(2.1) = 11.23

x₂ = 2.1 − (0.061 / 11.23)

x₂ = 2.094568


## Iterasi 3

x₃ = 2.094551

Karena perubahan nilai sudah sangat kecil, iterasi dihentikan.



# Hasil

Hasil perhitungan menggunakan Metode Newton-Raphson menghasilkan akar persamaan:

x = 2.0945514815

Nilai tersebut merupakan solusi dari persamaan:

x³ − 2x − 5 = 0

Program berhasil menemukan solusi dalam beberapa iterasi dengan tingkat akurasi yang tinggi.



# Analisis Error

Rumus error relatif:

Error = |(xₙ − xₙ₋₁) / xₙ| × 100%

Perhitungan:

Error = |(2.094551 − 2.094568) / 2.094551| × 100%

Error = 0.00081%

Nilai error yang sangat kecil menunjukkan bahwa metode telah mencapai konvergensi dan menghasilkan solusi yang akurat.



# Kesimpulan

Metode Newton-Raphson berhasil digunakan untuk menyelesaikan persamaan nonlinier:

f(x) = x³ − 2x − 5

Hasil akar persamaan yang diperoleh adalah:

x = 2.0945514815

Dengan error sebesar 0.00081%, metode Newton-Raphson terbukti mampu memberikan hasil yang akurat dan efisien dalam menyelesaikan permasalahan pencarian akar persamaan nonlinier.



# File Repository

* newton_raphson.py → Source code program
* hasil_program.png → Screenshot hasil program
* README.md → Dokumentasi proyek



Terima kasih telah mengunjungi repository ini.


