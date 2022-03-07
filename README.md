BAB 6 Modul

Jika kita keluar dari interpreter Python dan memasukkannya lagi, definisi yang telah dibuat (fungsi dan variabel) akan hilang. Oleh karena itu, jika kita ingin menulis program yang lebih panjang, sebaiknya menggunakan editor teks untuk menyiapkan input untuk penerjemah dan menjalankannya dengan file tersebut sebagai input
Saat program semakin panjang, kita mungkin ingin membaginya menjadi beberapa file untuk perawatan yang lebih mudah. Kita mungkin juga ingin menggunakan fungsi praktis yang telah ditulis di beberapa program tanpa menyalin definisinya ke dalam setiap program
Untuk mendukung ini, Python memiliki cara untuk menempatkan definisi dalam file dan menggunakannya dalam skrip atau dalam instance interpreter yang interaktif. File seperti itu disebut modul ; definisi dari sebuah modul dapat diimpor ke modul lain atau ke modul utama (kumpulan variabel yang dapat diakses dalam skrip yang dijalankan di tingkat atas dan dalam mode kalkulator)

#Modul

Modul dapat berisi pernyataan yang dapat dieksekusi serta definisi fungsi. Pernyataan ini dimaksudkan untuk menginisialisasi modul. Setiap modul memiliki tabel simbol pribadinya sendiri, yang digunakan sebagai tabel simbol global oleh semua fungsi yang didefinisikan dalam modul. Dengan demikian, pembuat modul dapat menggunakan variabel global dalam modul tanpa mengkhawatirkan bentrokan yang tidak disengaja dengan variabel global pengguna. Modul dapat mengimpor modul lain. Merupakan kebiasaan tetapi tidak diharuskan untuk menempatkan semua pernyataan impor di awal modul (atau skrip, dalam hal ini). Ada beberapa varian import untuk mengimport nama dari modul langsung ke tabel simbol modul pengimpor. Sebagai contoh:

Menjalankan modul sebagai skrip
Jalur Pencarian Modul
File Python "Dikompilasi"

#Modul Standar

Python hadir dengan pustaka modul standar, yang dijelaskan dalam dokumen terpisah. Beberapa modul dibangun ke dalam juru bahasa; ini menyediakan akses ke operasi yang bukan bagian dari inti bahasa tetapi tetap dibangun, baik untuk efisiensi atau untuk menyediakan akses ke sistem operasi primitif seperti panggilan sistem

#Fungsi dir()_ 

Fungsi bawaan dir()digunakan untuk mengetahui nama mana yang didefinisikan oleh modul. Ini mengembalikan daftar string yang diurutkan

#Paket

Paket adalah cara menyusun namespace modul Python dengan menggunakan "nama modul bertitik". Misalnya, nama modul A.Bmenunjuk sebuah submodul yang dinamai Bdalam sebuah paket bernama A. Sama seperti penggunaan modul yang menyelamatkan pembuat modul yang berbeda dari keharusan khawatir tentang nama variabel global satu sama lain, penggunaan nama modul bertitik menyelamatkan penulis paket multi-modul seperti NumPy atau Pillow dari keharusan khawatir tentang nama modul masing-masing

Perhatikan bahwa saat menggunakan , item dapat berupa submodul (atau subpaket) paket, atau nama lain yang ditentukan dalam paket, seperti fungsi, kelas, atau variabel. Pernyataan pertama menguji apakah item didefinisikan dalam paket; jika tidak, ia menganggapnya sebagai modul dan mencoba memuatnya. Jika gagal menemukannya, pengecualian dimunculkan.from package import itemimportImportError

Sebaliknya, saat menggunakan sintaks seperti , setiap item kecuali yang terakhir harus berupa paket; item terakhir dapat berupa modul atau paket tetapi tidak dapat berupa kelas atau fungsi atau variabel yang ditentukan dalam item sebelumnya.import item.subitem.subsubitem

Yang termasuk dalam packages/paket adalah:

Importing * From a Package
Intra-package References
Packages in Multiple Directories
