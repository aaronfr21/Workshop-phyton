# 12 Virtual Environments and Packages

* 12.1. Introduction

Aplikasi Python akan sering menggunakan paket dan modul yang tidak datang sebagai bagian dari perpustakaan standar. Aplikasi terkadang memerlukan versi pustaka tertentu, karena aplikasi mungkin mengharuskan bug tertentu telah diperbaiki atau aplikasi mungkin ditulis menggunakan versi antarmuka pustaka yang sudah usang.

Ini berarti tidak mungkin satu instalasi Python memenuhi persyaratan setiap aplikasi. Jika aplikasi A membutuhkan versi 1.0 dari modul tertentu tetapi aplikasi B membutuhkan versi 2.0, maka persyaratan tersebut bertentangan dan menginstal versi 1.0 atau 2.0 akan membuat satu aplikasi tidak dapat berjalan.

Solusi untuk masalah ini adalah membuat lingkungan virtual, pohon direktori mandiri yang berisi instalasi Python untuk versi Python tertentu, ditambah sejumlah paket tambahan.

Aplikasi yang berbeda kemudian dapat menggunakan lingkungan virtual yang berbeda. Untuk mengatasi contoh sebelumnya dari persyaratan yang saling bertentangan, aplikasi A dapat memiliki lingkungan virtual sendiri dengan versi 1.0 terinstal sementara aplikasi B memiliki lingkungan virtual lain dengan versi 2.0. Jika aplikasi B memerlukan pustaka yang ditingkatkan ke versi 3.0, ini tidak akan memengaruhi lingkungan aplikasi A.

* 12.2. Creating Virtual Environments

Modul yang digunakan untuk membuat dan mengelola lingkungan virtual disebut venv. venv biasanya akan menginstal versi Python terbaru yang Anda miliki. Jika Anda memiliki beberapa versi Python di sistem Anda, Anda dapat memilih versi Python tertentu dengan menjalankan python3 atau versi mana pun yang Anda inginkan.

Lokasi direktori umum untuk lingkungan virtual adalah .venv. Nama ini membuat direktori biasanya tersembunyi di shell Anda dan dengan demikian menyingkir sambil memberinya nama yang menjelaskan mengapa direktori itu ada. Ini juga mencegah bentrokan dengan file definisi variabel lingkungan .env yang didukung oleh beberapa perkakas.

Setelah Anda membuat lingkungan virtual, Anda dapat mengaktifkannya.

Mengaktifkan lingkungan virtual akan mengubah prompt shell Anda untuk menunjukkan lingkungan virtual apa yang Anda gunakan, dan memodifikasi lingkungan sehingga menjalankan python akan memberi Anda versi tertentu dan instalasi Python

* 12.3. Managing Packages with pip

Anda dapat menginstal, memutakhirkan, dan menghapus paket menggunakan program bernama pip. Secara default pip akan menginstal paket dari Python Package Index, https://pypi.org. Anda dapat menelusuri Indeks Paket Python dengan membukanya di browser web Anda.

pip memiliki sejumlah sub-perintah: “install”, “uninstall”, “freeze”, dll. (Lihat panduan Instalasi Modul Python untuk dokumentasi lengkap untuk pip.)

