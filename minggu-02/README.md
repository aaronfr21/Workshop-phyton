# Workshop-phyton

# PENGENDALI ALIRAN PROGRAM

# TUTORIAL BAB 4
Sumber : [tutorial python](https://docs.python.org/3.10/tutorial/controlflow.html)

file source code bab 4 : [minggu-02](https://github.com/aaronfr21/Workshop-phyton/tree/main/minggu-02)

**Macam-macam Control Flow**
Selain menggunakan pernyataan while yang sudah ada pada materi [minggu pertama](MINGGU-1.md) terdapat beberapa pernyataan control flow lainnya yang juga dikenal / digunakan pada bahasa pemrograman lainnya.

#Pernyataan If

Mungkin jenis pernyataan yang paling terkenal adalah pernyataan if.
Mungkin ada nol atau lebih elifbagian, dan elsebagian itu opsional. Kata kunci ' elif' merupakan kependekan dari 'else if', dan berguna untuk menghindari lekukan yang berlebihan. Sebuah if… elif… elif… urutan adalah pengganti switchatau casepernyataan yang ditemukan dalam bahasa lain.

#Pernyataan for

Pernyataan fordalam Python sedikit berbeda dari apa yang mungkin Anda gunakan dalam C atau Pascal. Daripada selalu mengulangi perkembangan aritmatika angka (seperti dalam Pascal), atau memberi pengguna kemampuan untuk menentukan langkah iterasi dan kondisi penghentian (seperti C), forpernyataan Python mengulangi item dari urutan apa pun (daftar atau a string), dalam urutan yang muncul dalam urutan
Kode yang memodifikasi koleksi saat mengulangi koleksi yang sama bisa jadi sulit untuk diperbaiki. Sebagai gantinya, biasanya lebih mudah untuk mengulang salinan koleksi atau membuat koleksi baru

#Fungsi 

Jika Anda perlu mengulangi urutan angka, fungsi range()bawaan sangat berguna. Ini menghasilkan progresi aritmatika
Titik akhir yang diberikan tidak pernah menjadi bagian dari urutan yang dihasilkan; range(10)menghasilkan 10 nilai, indeks hukum untuk item dari urutan panjang 10. Dimungkinkan untuk membiarkan rentang mulai dari nomor lain, atau untuk menentukan kenaikan yang berbeda (bahkan negatif; kadang-kadang ini disebut 'langkah')
Untuk mengulangi indeks urutan, Anda dapat menggabungkan range()dan len()
Namun, dalam kebanyakan kasus seperti itu, akan lebih mudah untuk menggunakan enumerate() fungsi tersebut, lihat Teknik Perulangan .
Hal aneh terjadi jika Anda hanya mencetak rentang

Dalam banyak hal, objek yang dikembalikan oleh range()berperilaku seolah-olah itu adalah daftar, tetapi sebenarnya tidak. Ini adalah objek yang mengembalikan item berurutan dari urutan yang diinginkan ketika Anda mengulanginya, tetapi itu tidak benar-benar membuat daftar, sehingga menghemat ruang
Kami mengatakan objek seperti itu dapat diubah , yaitu, cocok sebagai target untuk fungsi dan konstruksi yang mengharapkan sesuatu dari mana mereka dapat memperoleh item berturut-turut sampai persediaan habis. Kita telah melihat bahwa pernyataan for tersebut adalah konstruk seperti itu, sedangkan contoh fungsi yang mengambil iterable adalah sum()

#Pernyataan break dan continue dan else 

Pernyataan break, seperti di C, keluar dari penutup foratau whileloop terdalam.
Pernyataan loop mungkin memiliki elseklausa; itu dieksekusi ketika loop berakhir melalui habisnya iterable (with for) atau ketika kondisinya menjadi salah (with while), tetapi tidak ketika loop diakhiri oleh sebuah breakpernyataan. Ini dicontohkan oleh loop berikut, yang mencari bilangan prima

Ketika digunakan dengan loopm else memiliki lebih banyak kesamaan dengan pernyataan else daripada pernyataan if. pernyataan else berjalan ketika tidak ada pengecualian, dan else berjalan ketika tidak ada break. 

#Pernyataan pass

Pernyataan pass tidak melakukan apa-apa. ini dapat digunakan ketika pernyataan diperlukan secara sintaksis tetapi program tidak memerlukan tidakan. 
tempat lain pass yang dapat digunakan adalah sebagai tempat unutk fungsi atau badan kondisional ketika kita sedang mengerjakan kode baru, memungkinkan kita terus berpikir pada tigkat yang lebih abstrak. 

#Mendefinisikan 

Kata kunci memperkenalkan definisidef fungsi . Itu harus diikuti dengan nama fungsi dan daftar parameter formal dalam kurung. Pernyataan-pernyataan yang membentuk badan fungsi dimulai dari baris berikutnya, dan harus diindentasi.

Pernyataan pertama dari badan fungsi secara opsional dapat berupa string literal; literal string ini adalah string dokumentasi fungsi, atau docstring . (Lebih lanjut tentang docstrings dapat ditemukan di bagian Documentation Strings .) Ada alat yang menggunakan docstrings untuk secara otomatis menghasilkan dokumentasi online atau tercetak, atau untuk memungkinkan pengguna menelusuri kode secara interaktif; itu praktik yang baik untuk memasukkan docstrings dalam kode yang Anda tulis, jadi biasakan itu

Eksekusi suatu fungsi memperkenalkan tabel simbol baru yang digunakan untuk variabel lokal dari fungsi tersebut. Lebih tepatnya, semua penetapan variabel dalam suatu fungsi menyimpan nilai dalam tabel simbol lokal; sedangkan referensi variabel pertama-tama terlihat di tabel simbol lokal, lalu di tabel simbol lokal dari fungsi terlampir, lalu di tabel simbol global, dan terakhir di tabel nama bawaan. Dengan demikian, variabel global dan variabel fungsi terlampir tidak dapat secara langsung diberi nilai dalam suatu fungsi (kecuali, untuk variabel global, disebutkan dalam pernyataan global, atau, untuk variabel fungsi terlampir, disebutkan dalam pernyataan non local), meskipun mereka dapat direferensikan.

Parameter aktual (argumen) ke pemanggilan fungsi diperkenalkan di tabel simbol lokal dari fungsi yang dipanggil saat dipanggil; dengan demikian, argumen dilewatkan menggunakan call by value (di mana nilainya selalu merupakan referensi objek , bukan nilai objek). 1 Ketika suatu fungsi memanggil fungsi lain, atau memanggil dirinya sendiri secara rekursif, tabel simbol lokal baru dibuat untuk panggilan itu.

Definisi fungsi mengaitkan nama fungsi dengan objek fungsi dalam tabel simbol saat ini. Interpreter mengenali objek yang ditunjuk dengan nama itu sebagai fungsi yang ditentukan pengguna. Nama lain juga dapat menunjuk ke objek fungsi yang sama dan juga dapat digunakan untuk mengakses fungsi

berasal dari bahasa lain, kita mungkin keberatan dengan itu. fib bukanlah fungsi tetapi prosedur karena tidak mengembalikan nilai. faktanya, bahkan fungsi tanpa returm memang mengembalikan nilai, meskipun agak membossankan. nilai ini disebut none. None biasanya ditekan oleh penerjemah jika itu menjadi satu-satunya nilai yang ditulis. Kita dapat melihatnya jika kita benar-benar ingin menggunakan print()

#Nilai Argumen 

Bentuk yang paling berguna adalah untuk menentukan nilai default untuk satu atau lebih argumen. Ini menciptakan fungsi yang dapat dipanggil dengan argumen yang lebih sedikit daripada yang ditentukan untuk diizinkan

Fungsi ini dapat dipanggil dengan beberapa cara:
hanya memberikan argumen wajib: ask_ok('Do you really want to quit?')
memberikan salah satu argumen opsional: ask_ok('OK to overwrite the file?', 2)
atau bahkan memberikan semua argumen: ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

Contoh ini juga memperkenalkan inkata kunci. Ini menguji apakah suatu urutan mengandung nilai tertentu atau tidak.

Nilai default dievaluasi pada titik definisi fungsi dalam ruang lingkup yang ditentukan

#Argumen Kata 

Dalam panggilan fungsi, argumen kata kunci harus mengikuti argumen posisi. Semua argumen kata kunci yang diteruskan harus cocok dengan salah satu argumen yang diterima oleh fungsi (misalnya actorbukan argumen yang valid untuk parrotfungsi tersebut), dan urutannya tidak penting. Ini juga termasuk argumen non-opsional (misalnya parrot(voltage=1000)valid juga). Tidak ada argumen yang dapat menerima nilai lebih dari sekali. Berikut adalah contoh yang gagal karena pembatasan ini

Ketika parameter formal terakhir dari formulir **nameada, ia menerima kamus (lihat Jenis Pemetaan — dict ) yang berisi semua argumen kata kunci kecuali yang terkait dengan parameter formal. Ini dapat digabungkan dengan parameter formal dari formulir *name(dijelaskan dalam subbagian berikutnya) yang menerima tupel yang berisi argumen posisi di luar daftar parameter formal. ( *nameharus terjadi sebelum **name.)

#Parameter 

Secara default, argumen dapat diteruskan ke fungsi Python baik dengan posisi atau secara eksplisit dengan kata kunci. Untuk keterbacaan dan kinerja, masuk akal untuk membatasi cara argumen dapat diteruskan sehingga pengembang hanya perlu melihat definisi fungsi untuk menentukan apakah item dilewatkan berdasarkan posisi, posisi atau kata kunci, atau kata kunci

di mana /dan *adalah opsional. Jika digunakan, simbol-simbol ini menunjukkan jenis parameter melalui bagaimana argumen dapat diteruskan ke fungsi: hanya posisional, posisional atau kata kunci, dan hanya kata kunci. Parameter kata kunci juga disebut sebagai parameter bernama

#Argumen Posisi atau kata 

Jika /dan *tidak ada dalam definisi fungsi, argumen dapat diteruskan ke fungsi berdasarkan posisi atau kata kunci.

#Parameter Hanya 

Melihat ini sedikit lebih detail, dimungkinkan untuk menandai parameter tertentu sebagai positional-only . Jika hanya posisional , urutan parameter penting, dan parameter tidak dapat diteruskan oleh kata kunci. Parameter posisional saja ditempatkan sebelum /(garis miring ke depan). The /digunakan untuk secara logis memisahkan parameter posisional saja dari parameter lainnya. Jika tidak ada /dalam definisi fungsi, tidak ada parameter posisional saja
Parameter yang mengikuti /mungkin berupa posisi-atau-kata kunci atau hanya-kata kunci .

#Argumen Hanya Kata 

Untuk menandai parameter sebagai hanya kata kunci , yang menunjukkan parameter harus diteruskan oleh argumen kata kunci, tempatkan an *di daftar argumen tepat sebelum parameter khusus kata kunci pertama

#Contoh 

Definisi fungsi pertama, standard_arg, bentuk yang paling dikenal, tidak membatasi konvensi pemanggilan dan argumen dapat diteruskan oleh posisi atau kata kunci

Fungsi kedua pos_only_argdibatasi hanya menggunakan parameter posisi karena ada /dalam definisi fungsi
Fungsi ketiga kwd_only_argshanya mengizinkan argumen kata kunci seperti yang ditunjukkan oleh a *dalam definisi fungsi
Dan yang terakhir menggunakan ketiga konvensi pemanggilan dalam definisi fungsi yang sama
Akhirnya, pertimbangkan definisi fungsi ini yang memiliki potensi benturan antara argumen posisi name dan **kwdsyang memiliki namekunci

Tidak ada kemungkinan panggilan yang akan membuatnya kembali Truekarena kata kunci 'name' akan selalu mengikat ke parameter pertama

Tetapi menggunakan /(argumen hanya posisional), dimungkinkan karena memungkinkan namesebagai argumen posisi dan 'name'sebagai kunci dalam argumen kata kunci
Dengan kata lain, nama-nama parameter posisional saja dapat digunakan **kwdstanpa ambiguitas

#Rekap 

Kasus penggunaan akan menentukan parameter mana yang akan digunakan dalam definisi fungsi

Sebagai pedoman:

Gunakan hanya posisi jika Anda ingin nama parameter tidak tersedia untuk pengguna. Ini berguna ketika nama parameter tidak memiliki arti sebenarnya, jika Anda ingin menegakkan urutan argumen saat fungsi dipanggil atau jika Anda perlu mengambil beberapa parameter posisi dan kata kunci arbitrer.
Gunakan hanya kata kunci ketika nama memiliki arti dan definisi fungsi lebih dapat dipahami dengan menjadi eksplisit dengan nama atau Anda ingin mencegah pengguna mengandalkan posisi argumen yang diteruskan.
Untuk API, gunakan hanya posisi untuk mencegah kerusakan perubahan API jika nama parameter diubah di masa mendatang.

#Daftar Argumen Sewenang

Akhirnya, opsi yang paling jarang digunakan adalah menentukan bahwa suatu fungsi dapat dipanggil dengan sejumlah argumen yang berubah-ubah. Argumen-argumen ini akan dibungkus dalam sebuah tuple (lihat Tuples and Sequences ). Sebelum jumlah variabel argumen, nol atau lebih argumen normal dapat terjadi.

Biasanya, variadicargumen ini akan menjadi yang terakhir dalam daftar parameter formal, karena mereka mengambil semua argumen input yang tersisa yang diteruskan ke fungsi. Parameter formal apa pun yang muncul setelah *args parameter adalah argumen 'hanya kata kunci', artinya parameter tersebut hanya dapat digunakan sebagai kata kunci daripada argumen posisi.

#Membongkar Daftar 

Situasi sebaliknya terjadi ketika argumen sudah ada dalam daftar atau tupel tetapi perlu dibongkar untuk pemanggilan fungsi yang memerlukan argumen posisi terpisah. Misalnya, range()fungsi bawaan mengharapkan argumen mulai dan berhenti yang terpisah. Jika tidak tersedia secara terpisah, tulis pemanggilan fungsi dengan *-operator untuk membongkar argumen dari daftar atau tupel

#Ekspresi 

Fungsi anonim kecil dapat dibuat dengan lambdakata kunci. Fungsi ini mengembalikan jumlah dari dua argumennya: . Fungsi Lambda dapat digunakan di mana pun objek fungsi diperlukan. Mereka secara sintaksis terbatas pada satu ekspresi. Secara semantik, mereka hanyalah gula sintaksis untuk definisi fungsi normal. Seperti definisi fungsi bersarang, fungsi lambda dapat mereferensikan variabel dari cakupan yang berisi:lambda a, b: a+b

#String

Berikut adalah beberapa konvensi tentang konten dan pemformatan string dokumentasi.
Baris pertama harus selalu merupakan ringkasan singkat dan ringkas dari tujuan objek. Untuk singkatnya, itu tidak boleh secara eksplisit menyatakan nama atau jenis objek, karena ini tersedia dengan cara lain (kecuali jika nama itu merupakan kata kerja yang menggambarkan operasi suatu fungsi). Baris ini harus dimulai dengan huruf kapital dan diakhiri dengan titik.

Jika ada lebih banyak baris dalam string dokumentasi, baris kedua harus kosong, yang secara visual memisahkan ringkasan dari deskripsi lainnya. Baris berikut harus berupa satu atau lebih paragraf yang menjelaskan konvensi pemanggilan objek, efek sampingnya, dll.

Parser Python tidak menghapus lekukan dari literal string multi-baris di Python, jadi alat yang memproses dokumentasi harus menghapus lekukan jika diinginkan. Ini dilakukan dengan menggunakan konvensi berikut. Baris non-kosong pertama setelah baris pertama string menentukan jumlah lekukan untuk seluruh string dokumentasi. (Kita tidak dapat menggunakan baris pertama karena biasanya berdekatan dengan tanda kutip pembuka string sehingga lekukannya tidak terlihat dalam literal string.) Spasi "setara" dengan lekukan ini kemudian dihilangkan dari awal semua baris string . Garis yang lebih sedikit menjorok tidak boleh muncul, tetapi jika muncul, semua spasi di depannya harus dihilangkan. Kesetaraan spasi putih harus diuji setelah perluasan tab (biasanya menjadi 8 spasi).

#Fungsi 

Anotasi fungsi sepenuhnya merupakan informasi metadata opsional tentang jenis yang digunakan oleh fungsi yang ditentukan pengguna (lihatPEP 3107 dan PEP 484 untuk informasi lebih lanjut).

Anotasi disimpan dalam__annotations__ atribut fungsi sebagai kamus dan tidak berpengaruh pada bagian lain dari fungsi tersebut. Anotasi parameter ditentukan oleh titik dua setelah nama parameter, diikuti dengan ekspresi yang mengevaluasi nilai anotasi. Anotasi pengembalian ditentukan oleh literal->, diikuti oleh ekspresi, antara daftar parameter dan titik dua yang menunjukkan akhirpernyataan
