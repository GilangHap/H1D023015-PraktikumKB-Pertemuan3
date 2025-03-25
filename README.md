**Konverter Suhu**
Program ini mengonversi nilai suhu antara satuan Celsius, Fahrenheit, dan Kelvin melalui terminal.

**🛠 Fitur**
Konversi antara 3 satuan suhu: Celsius (°C), Fahrenheit (°F), dan Kelvin (K).
Validasi input:
-> Nilai suhu harus angka (bisa desimal/negatif).
-> Satuan suhu harus valid (Celsius, Fahrenheit, atau Kelvin).
Tampilan hasil konversi dengan 2 digit desimal.

**📁 Struktur Program**
Struktur Data
-> SATUAN_SUHU (tuple):
Menyimpan daftar satuan yang valid: ("Celsius", "Fahrenheit", "Kelvin").
-> VALID_SATUAN (set):
Digunakan untuk pengecekan cepat keanggotaan satuan.

Alur Program
-> Pengguna memasukkan:
    Nilai suhu (contoh: 100).
    Satuan asal (contoh: Celsius).
    Satuan tujuan (contoh: Fahrenheit).
-> Program memvalidasi input dan menampilkan hasil konversi.
-> Pengguna bisa mengulang atau keluar.

**🖥️ Cara Menjalankan**
-> Clone repositori atau salin kode ke file konverter_suhu.py.
-> Jalankan di terminal: **python konverter_suhu.py**

**📚 Library Digunakan**
-> re: Untuk validasi input nilai suhu dengan regex.
-> Built-in Python: set, tuple, dan fungsi dasar.
