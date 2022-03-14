Input & Output

Ada beberapa cara untuk menampilkan output dari suatu program; data dapat dicetak dalam bentuk yang dapat dibaca manusia, atau ditulis ke file untuk digunakan di masa mendatang. Bab ini akan membahas beberapa kemungkinan

#Fancier Output Formatting

Untuk menggunakan literal string yang diformat, mulailah string dengan f atau F sebelum tanda kutip pembuka atau tanda kutip tiga. Di dalam string ini, Anda dapat menulis ekspresi Python antara karakter { dan } yang dapat merujuk ke variabel atau nilai literal. Metode str.format()string membutuhkan lebih banyak upaya manual. Kita masih akan menggunakan {dan }untuk menandai di mana variabel akan diganti dan dapat memberikan arahan pemformatan terperinci, tetapi kita juga harus memberikan informasi yang akan diformat.Kita dapat melakukan semua penanganan string sendiri dengan menggunakan operasi pengirisan string dan penggabungan untuk membuat tata letak apa pun yang dapat dibayangkan. Tipe string memiliki beberapa metode yang melakukan operasi yang berguna untuk mengisi string ke lebar kolom tertentu. Fungsi str() dimaksudkan untuk mengembalikan representasi nilai yang cukup dapat dibaca manusia, sedangkan repr() dimaksudkan untuk menghasilkan representasi yang dapat dibaca oleh penerjemah (atau akan memaksa SyntaxError jika tidak ada sintaks yang setara)

Berikut ini macam-macam formatting :

*   Formatted String Literals

    Literal string terformat (disingkat juga disebut f-string) memungkinkan kita memasukkan nilai ekspresi Python di dalam string dengan mengawali string denganforFdan menulis ekspresi sebagai {expression}

*   The String format() Method
   
    Tanda kurung dan karakter di dalamnya (disebut bidang format) diganti dengan objek yang diteruskan ke str.format()metode. Angka dalam kurung dapat digunakan untuk merujuk ke posisi objek yang dilewatkan ke dalam str.format()metode

*   Manual String Formatting
    
    Metode str.rjust()objek string membenarkan string di bidang dengan lebar tertentu dengan mengisinya dengan spasi di sebelah kiri. Ada metode serupa str.ljust()dan str.center(). Metode ini tidak menulis apa pun, mereka hanya mengembalikan string baru. Jika string input terlalu panjang, mereka tidak memotongnya, tetapi mengembalikannya tidak berubah; ini akan mengacaukan tata letak kolom, tetapi itu biasanya lebih baik daripada alternatifnya, yang berbohong tentang nilai. (Jika kita benar-benar menginginkan pemotongan, maka selalu dapat menambahkan operasi irisan, seperti pada x.ljust(n)[:n].)

*   Old string formatting

    Operator % (modulo) juga dapat digunakan untuk pemformatan string. Mengingat , contoh di diganti dengan nol atau lebih elemen dari . Operasi ini biasa disebut dengan interpolasi string. Sebagai contoh:'string' % values%stringvalues

#Reading and Writing Files

Argumen pertama adalah string yang berisi nama file. Argumen kedua adalah string lain yang berisi beberapa karakter yang menjelaskan cara file akan digunakan. mode bisa 'r'ketika file hanya akan dibaca, 'w' untuk hanya menulis (file yang ada dengan nama yang sama akan dihapus), dan 'a'membuka file untuk ditambahkan; setiap data yang ditulis ke file secara otomatis ditambahkan ke akhir. 'r+'membuka file untuk membaca dan menulis. Argumen mode adalah opsional; 'r'akan diasumsikan jika dihilangkan. Biasanya, file dibuka dalam mode teks , artinya, Anda membaca dan menulis string dari dan ke file, yang dikodekan dalam pengkodean tertentu. Jika penyandian tidak ditentukan, defaultnya adalah bergantung pada platform (lihat open()). 'b'ditambahkan ke mode membuka file dalam mode biner : sekarang data dibaca dan ditulis dalam bentuk objek byte. Mode ini harus digunakan untuk semua file yang tidak berisi teks. Dalam mode teks, default saat membaca adalah mengonversi akhiran baris khusus platform ( \npada Unix, \r\npada Windows) menjadi hanya \n. Saat menulis dalam mode teks, defaultnya adalah mengonversi kemunculan \nkembali ke akhir baris khusus platform. Modifikasi di balik layar untuk file data ini baik untuk file teks, tetapi akan merusak data biner seperti itu di JPEGatau EXEfile. Berhati-hatilah untuk menggunakan mode biner saat membaca dan menulis file tersebut.

*   Methods of File Objects

    Untuk membaca konten file, panggil f.read(size), yang membaca sejumlah data dan mengembalikannya sebagai string (dalam mode teks) atau objek byte (dalam mode biner). size adalah argumen numerik opsional. Ketika ukuran dihilangkan atau negatif, seluruh isi file akan dibaca dan dikembalikan; itu masalah Anda jika file dua kali lebih besar dari memori mesin Anda. Jika tidak, paling banyak karakter ukuran (dalam mode teks) atau ukuran byte (dalam mode biner) dibaca dan dikembalikan. Jika akhir file telah tercapai, f.read()akan mengembalikan string kosong ( ''). f.readline()membaca satu baris dari file; karakter baris baru ( \n) ditinggalkan di akhir string, dan hanya dihilangkan pada baris terakhir file jika file tidak diakhiri dengan baris baru. Ini membuat nilai pengembalian tidak ambigu; jika f.readline()mengembalikan string kosong, akhir file telah tercapai, sedangkan baris kosong diwakili oleh '\n', string yang hanya berisi satu baris baru. f.write(string)menulis isi string ke file, mengembalikan jumlah karakter yang ditulis. f.tell()mengembalikan bilangan bulat yang memberikan posisi objek file saat ini dalam file yang direpresentasikan sebagai jumlah byte dari awal file saat dalam mode biner dan angka buram saat dalam mode teks.

*   Saving structured data with json

    String dapat dengan mudah ditulis dan dibaca dari sebuah file. Angka membutuhkan sedikit lebih banyak usaha, karena read()metode ini hanya mengembalikan string, yang harus diteruskan ke fungsi seperti int(), yang mengambil seperti string '123' dan mengembalikan nilai numeriknya 123. Saat Anda ingin menyimpan tipe data yang lebih kompleks seperti daftar bersarang dan kamus, parsing dan serialisasi dengan tangan menjadi rumit. 
    Daripada membuat pengguna terus-menerus menulis dan men-debug kode untuk menyimpan tipe data yang rumit ke file, Python memungkinkan Anda untuk menggunakan format pertukaran data populer yang disebut JSON (JavaScript Object Notation) . Modul standar yang dipanggil jsondapat mengambil hierarki data Python, dan mengubahnya menjadi representasi string; proses ini disebut serialisasi . Merekonstruksi data dari representasi string disebut deserializing . Antara serialisasi dan deserializing, string yang mewakili objek mungkin telah disimpan dalam file atau data, atau dikirim melalui koneksi jaringan ke beberapa mesin yang jauh.