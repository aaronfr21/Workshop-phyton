# 10 Brief Tour of the Standard Library

* 10.1. Operating System Interface

Modul os menyediakan banyak fungsi untuk berinteraksi dengan sistem operasi

Fungsi built-in dir() dan help() berguna sebagai bantuan interaktif untuk bekerja dengan modul besar seperti os

Untuk tugas manajemen file dan direktori harian, modul shutil menyediakan antarmuka tingkat tinggi yang lebih mudah digunakan

* 10.2. File Wildcards 

Modul glob menyediakan fungsi untuk membuat daftar file dari pencarian wildcard direktori :

* 10.3. Command Line Arguments

Skrip utilitas umum sering kali perlu memproses argumen baris perintah. Argumen ini disimpan dalam atribut argvsys modul sebagai daftar. Misalnya hasil keluaran berikut dari menjalankan di baris perintah:

Modul argparse menyediakan mekanisme yang lebih canggih untuk memproses argumen baris perintah. Skrip berikut mengekstrak satu atau lebih nama file dan sejumlah baris opsional yang akan ditampilkan

* 10.4. Error Output Redirection and Program Termination

Modul sysini juga memiliki atribut untuk stdin , stdout , dan stderr . Yang terakhir ini berguna untuk memancarkan peringatan dan pesan kesalahan agar terlihat bahkan ketika stdout telah dialihkan:


* 10.5. String Pattern Matching

Modul ini remenyediakan alat ekspresi reguler untuk pemrosesan string tingkat lanjut. Untuk pencocokan dan manipulasi yang kompleks, ekspresi reguler menawarkan solusi yang ringkas dan dioptimalkan:

Ketika hanya kemampuan sederhana yang diperlukan, metode string lebih disukai karena lebih mudah dibaca dan di-debug:

* 10.6. Mathematics

Modul math memberikan akses ke fungsi pustaka C yang mendasari untuk matematika floating point:

Modul acak menyediakan alat untuk membuat pilihan acak

Modul statistic menghitung properti statistik dasar (rata-rata, median, varians, dll.) dari data numerik:

* 10.7. Internet Access

Ada sejumlah modul untuk mengakses internet dan memproses protokol internet. Dua yang paling sederhana adalah urllib.request untuk mengambil data dari URL dan smtplib untuk mengirim email:

* 10.8. Dates and Times 

Modul datetime menyediakan kelas untuk memanipulasi tanggal dan waktu dengan cara yang sederhana dan kompleks. Sementara aritmatika tanggal dan waktu didukung, fokus implementasinya adalah pada ekstraksi anggota yang efisien untuk pemformatan dan manipulasi keluaran. Modul ini juga mendukung objek yang sadar zona waktu. 

* 10.9 Data Compression 

Pengarsipan data umum dan format kompresi secara langsung didukung oleh modul termasuk: zlib, gzip, bz2, lzma, zipfile dan tarfile 

* 10.10. Performance Measurement 

Beberapa pengguna Python mengembangkan minat yang mendalam untuk mengetahui kinerja relatif dari pendekatan yang berbeda untuk masalah yang sama. Python menyediakan alat pengukuran yang menjawab pertanyaan-pertanyaan itu dengan segera.

Misalnya, mungkin tergoda untuk menggunakan fitur pengepakan dan pembongkaran Tuple alih-alih pendekatan tradisional untuk bertukar argumen. Modul timeit dengan cepat menunjukkan keunggulan kinerja sederhana

* 10.11 Quality Control 

Modul doctest menyediakan alat untuk memindai modul dan memvalidasi tes yang tertanam dalam docstrings program. Konstruksi pengujian sesederhana memotong dan menempelkan panggilan biasa beserta hasilnya ke dalam docstring. Ini meningkatkan dokumentasi dengan memberikan contoh kepada pengguna dan memungkinkan modul doctest untuk memastikan kode tetap sesuai dengan dokumentasi


Modul unittest tidak semudah modul doctest, tetapi memungkinkan serangkaian tes yang lebih komprehensif untuk dipertahankan dalam file terpisah


# 11 Brief Tour of the Standard LIbrary - Part II

* 11.1. Output Formatting 

Modul  reprlib menyediakan versi yang repr()disesuaikan untuk tampilan singkat wadah besar atau bersarang dalam

Modul pprint menawarkan kontrol yang lebih canggih atas pencetakan objek bawaan dan objek yang ditentukan pengguna dengan cara yang dapat dibaca oleh penerjemah. Ketika hasilnya lebih panjang dari satu baris, "printer cantik" menambahkan jeda baris dan lekukan untuk mengungkapkan struktur data dengan lebih jelas:

Modul textwrap memformat paragraf teks agar sesuai dengan lebar layar yang diberikan

Modul lokal mengakses database format data spesifik budaya. Atribut pengelompokan fungsi format lokal menyediakan cara langsung untuk memformat angka dengan pemisah grup

*11.2. Templating

Modul string menyertakan kelas Template serbaguna dengan sintaks yang disederhanakan yang cocok untuk diedit oleh pengguna akhir. Hal ini memungkinkan pengguna untuk menyesuaikan aplikasi mereka tanpa harus mengubah aplikasi.

Formatnya menggunakan nama placeholder yang dibentuk oleh $ dengan pengidentifikasi Python yang valid (karakter alfanumerik dan garis bawah). Mengelilingi placeholder dengan kurung memungkinkan untuk diikuti oleh lebih banyak huruf alfanumerik tanpa spasi. Menulis $$ membuat satu pelarian $

Metode substitute() memunculkan KeyError ketika placeholder tidak disediakan dalam kamus atau argumen kata kunci. Untuk aplikasi gaya gabungan surat, data yang diberikan pengguna mungkin tidak lengkap dan metode safe_substitute() mungkin lebih tepat — ini akan membuat placeholder tidak berubah jika data hilang:

Subkelas template dapat menentukan pembatas kustom. Misalnya, utilitas penggantian nama batch untuk browser foto dapat memilih untuk menggunakan tanda persen untuk placeholder seperti tanggal saat ini, nomor urut gambar, atau format file

* 11.3. Working with Binnary Data Record Layouts 

Modul struct menyediakan fungsi pack() dan unpack() untuk bekerja dengan format record biner dengan panjang variabel. Contoh berikut menunjukkan cara mengulang informasi header dalam file ZIP tanpa menggunakan modul zipfile. Kode paket "H" dan "I" masing-masing mewakili dua dan empat byte angka tidak bertanda. The "<" menunjukkan bahwa mereka adalah ukuran standar dan dalam urutan byte little-endian:

* 11.4. Multi-threading

Threading adalah teknik untuk memisahkan tugas yang tidak bergantung secara berurutan. Utas dapat digunakan untuk meningkatkan daya tanggap aplikasi yang menerima masukan pengguna saat tugas lain berjalan di latar belakang. Kasus penggunaan terkait menjalankan I/O secara paralel dengan perhitungan di utas lain.

Kode berikut menunjukkan bagaimana modul threading tingkat tinggi dapat menjalankan tugas di latar belakang sementara program utama terus berjalan

Tantangan utama aplikasi multi-utas adalah mengoordinasikan utas yang berbagi data atau sumber daya lainnya. Untuk itu, modul threading menyediakan sejumlah primitif sinkronisasi termasuk kunci, peristiwa, variabel kondisi, dan semaphore.

* 11.5. Logging 

Modul logging menawarkan sistem logging berfitur lengkap dan fleksibel. Paling sederhana, pesan log dikirim ke file atau ke sys.stderr

Secara default, pesan informasi dan debugging ditekan dan output dikirim ke kesalahan standar. Opsi keluaran lainnya termasuk perutean pesan melalui email, datagram, soket, atau ke Server HTTP. Filter baru dapat memilih perutean yang berbeda berdasarkan prioritas pesan: DEBUG, INFO, WARNING, ERROR, dan CRITICAL.

Sistem logging dapat dikonfigurasi langsung dari Python atau dapat dimuat dari file konfigurasi yang dapat diedit pengguna untuk logging yang disesuaikan tanpa mengubah aplikasi.

* 11.6. Weak References 

Python melakukan manajemen memori otomatis (penghitungan referensi untuk sebagian besar objek dan pengumpulan sampah untuk menghilangkan siklus). Memori dibebaskan segera setelah referensi terakhir dihilangkan.

Pendekatan ini bekerja dengan baik untuk sebagian besar aplikasi tetapi kadang-kadang ada kebutuhan untuk melacak objek hanya selama mereka digunakan oleh sesuatu yang lain. Sayangnya, hanya melacak mereka membuat referensi yang menjadikannya permanen. Modulweakref menyediakan alat untuk melacak objek tanpa membuat referensi. Ketika objek tidak lagi diperlukan, objek tersebut secara otomatis dihapus dari tabel referensi lemah dan panggilan balik dipicu untuk objek referensi lemah. Aplikasi umum termasuk objek caching yang mahal untuk dibuat:

*11.7. Tools for Working with Lists

Banyak kebutuhan struktur data dapat dipenuhi dengan tipe daftar bawaan. Namun, terkadang ada kebutuhan untuk implementasi alternatif dengan pertukaran kinerja yang berbeda.

Modul array menyediakan objek array() yang seperti daftar yang hanya menyimpan data homogen dan menyimpannya dengan lebih ringkas. Contoh berikut menunjukkan larik angka yang disimpan sebagai dua byte angka biner tidak bertanda (typecode "H") daripada 16 byte biasa per entri untuk daftar reguler objek int Python:

Modul koleksi menyediakan objek deque() yang seperti daftar dengan penambahan lebih cepat dan muncul dari sisi kiri tetapi pencarian lebih lambat di tengah. Objek-objek ini sangat cocok untuk mengimplementasikan antrian dan pencarian pohon pertama yang luas

Selain implementasi daftar alternatif, perpustakaan juga menawarkan alat lain seperti modul bagi dua dengan fungsi untuk memanipulasi daftar yang diurutkan

Modul heapq menyediakan fungsi untuk mengimplementasikan heap berdasarkan daftar reguler. Entri bernilai terendah selalu disimpan di posisi nol. Ini berguna untuk aplikasi yang berulang kali mengakses elemen terkecil tetapi tidak ingin menjalankan pengurutan daftar lengkap

* 11.8. Decimal Floating Point Arithmetic 

Modul desimal menawarkan tipe data Desimal untuk aritmatika titik mengambang desimal. Dibandingkan dengan implementasi float built-in dari floating point biner, kelas ini sangat membantu untuk

    * aplikasi keuangan dan penggunaan lainnya yang membutuhkan representasi desimal yang tepat, kontrol atas presisi,
    * kontrol atas pembulatan untuk memenuhi persyaratan sah legal atau peraturan, pelacakan tempat desimal yang signifikan, atau
    * aplikasi tempat pengguna mengharapkan hasil agar sesuai dengan perhitungan yang dilakukan dengan tangan.

Misalnya, menghitung pajak 5% untuk biaya telepon 70 sen memberikan hasil yang berbeda dalam floating point desimal dan floating point biner. Perbedaan menjadi signifikan jika hasilnya dibulatkan ke sen terdekat

Representasi yang tepat memungkinkan kelas Desimal untuk melakukan perhitungan modulo dan tes kesetaraan yang tidak cocok untuk floating point biner:

Modul desimal menyediakan aritmatika dengan presisi sebanyak yang diperlukan