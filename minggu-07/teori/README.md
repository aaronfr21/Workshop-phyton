# 9. Classes

Classes atau kelas - kelas menyediakan sarana untuk menggabungkan data dan fungsionalitas bersama. Setiap instance dari class dapat memiliki atribut yang melekat padanya untuk mempertahankan kondisinya. Instance dari sebuah class juga memiliki metode untuk memodifikasi kondisinya. Dibandingkan dengan bahasa pemrograman lain, mekanisme kelas Python menambah kelas dengan minimum sintaksis dan semantik baru.

Ini adalah campuran dari mekanisme kelas yang ditemukan dalam C++ dan modula-3. Objek dapat berisi jumlah dan jenis data yang berubah - ubah. Dalam termologi C++, biasanya anggota kelas adalah public, dan semua fungsi anggota adalah virtual. Seperti dalam Smalltalk, kelas itu sendiri adalah objek .

Ini memberikan semantik untuk mengimport dan mengganti nama. Tidak seperti C++ dan modula-3, tipe bawaan dapat digunakan sebagai kelas dasar untuk ekstensi oleh pengguna. Juga, seperti di C++, sebagai besar operator bawaan dengan sintaks khusus dapat didefinisikan ulang untuk instance kelas.

# 9.1. A Word About Names and Objects

Objek memiliki individualitas, dan banyak nama dapat terikat ke objek yang sama. Ini biasanya tidak dihargai pada pandangan pertama pada Python, dan dapat diabaikan dengan nama ketika berhadapan dengan tipe dasar yang tidak dapat diubah. Namun, aliasing memiliki efek yang mungkin mengejutkan pada semantik code Python yang melibatkan objek yang bisa berubah seperti daftar list, kamus dictionary, dan sebagian besar jenis lainnya.

# 9.2. Python Scopes and Namespaces

Sebelum memperkenalkan kelas, pertama-tama saya harus memberi tahu Anda tentang aturan ruang lingkup scope Python. Definisi kelas memainkan beberapa trik rapi dengan ruang nama namespaces, dan Anda perlu tahu bagaimana ruang lingkup dan ruang nama namespaces bekerja untuk sepenuhnya memahami apa yang terjadi. Kebetulan, pengetahuan tentang subjek ini berguna untuk programmer Python tingkat lanjut.

Sebuah namespace adalah pemetaan dari nama ke objek. Sebagian besar ruang nama namespace saat ini diimplementasikan sebagai kamus dictionary Python, tetapi itu biasanya tidak terlihat dengan cara apa pun , dan itu mungkin berubah di masa depan. Contoh ruang nama namespace adalah: himpunan nama bawaan (berisi fungsi seperti abs()). Dalam arti himpunan atribut suatu objek juga membentuk namespace.

Ngomong-ngomong, saya menggunakan kata attribute untuk nama apa pun yang mengikuti titik --- misalnya, dalam ekspresi z.real, real adalah atribut dari objek z .

Dalam kasus terakhir, pemberian nilai ke atribut dimungkinkan. Atribut yang dapat ditulis modname.the_answer = 42, juga dapat dihapus dengan pernyataan del. Sebagai contoh, del modname.the_answer akan menghapus atribut the_answer dari objek yang dinamai oleh modname.

Namespace dibuat pada saat yang berbeda dan memiliki masa hidup yang berbeda. Namespace yang berisi nama-nama bawaan dibuat ketika interpreter Python dimulai, dan tidak pernah dihapus. Pernyataan yang dieksekusi oleh pemanggilan interpreter tingkat atas, baik membaca dari file skrip atau secara interaktif, dianggap sebagai bagian dari modul yang disebut main sehingga mereka memiliki namespace global sendiri.

Namespace lokal untuk suatu fungsi dibuat ketika fungsi dipanggil, dan dihapus ketika fungsi kembali returns atau memunculkan pengecualian yang tidak ditangani dalam fungsi tersebut. Tentu saja, pemanggilan rekursif masing-masing memiliki ruang-nama namespace lokal mereka sendiri.

Suatu scope adalah wilayah tekstual dari program Python di mana namespace dapat diakses secara langsung. "Directly accessible" di sini berarti bahwa referensi yang tidak memenuhi syarat untuk suatu nama berusaha menemukan nama tersebut di namespace.

Meskipun cakupan scopes ditentukan secara statis, mereka digunakan secara dinamis.

    * Ruang lingkup scope terdalam, yang dicari pertama kali, berisi nama - nama lokal.
    * Lingkup scope dari setiap fungsi penutup, yang dicari dimulai dengan lingkup penutup terdekat, berisi nama - nama non - lokal, tetapi juga non - global.
    * Lingkup berikutnya next-to-lash berisi nama global modul saat ini.
    * Ruang lingkup scope terluar (dicari terakhir) adalah namespace yang mengandung nama bawaan.

Jika sebuah nama dinyatakan global, maka semua referensi dan penugasan langsung ke lingkup scope tengah yang berisi nama global modul. Untuk mengembalikan variabel yang ditemukan di laur cakupan terdalam, pernyataan nonlocal dapat digunakan; jika tidak dideklarasikan nonlokal, variabel-variabel itu hanya baca-saja (upaya untuk menulis ke variabel seperti itu hanya akan membuat variabel lokal baru dalam cakupan terdalam, membiarkan variabel luar yang dinamai identik tidak berubah).

Biasanya, cakupan lokal merujuk nama lokal dari fungsi saat ini. Definisi kelas menempatkan namespace lain dalam lingkup lokal. Sebuah kekhasan khusus dari Python adalah bahwa -- jika tidak ada pernyataan global atau pernyataan nonlocal yang berlaku -- pemberian nilai untuk nama selalu masuk ke ruang lingkup terdalam. Pemberian nilai tidak menyalin data --- mereka hanya mengikat nama ke objek.

# 9.2.1. Scopes and Namespaces Example

Contoh yang menunjukkan cara mereferensikan lingkup scopes dan ruang nama namespaces yang berbeda, dan bagaimana global dan nonlocal memengaruhi pengikatan variabel :

# 9.3. A First Look at Classes

Kelas memperkenalkan sedikit sintaks baru, tiga tipe objek baru, dan beberapa semantik baru.

# 9.3.1 Class Definition Syntax

Definisi kelas, seperti definisi fungsi (pernyataan def) harus dieksekusi sebelum mereka memiliki efek.

# 9.3.2 class Object

Objek kelas mendukung dua jenis operasi: referensi atribut dan instansiasi. Attribute references menggunakan sintaks standar yang digunakan untuk semua referensi atribut dalam Python: obj.name. Nama atribut yang valid adalah semua nama yang ada di namespace kelas saat objek kelas dibuat.

MyClass.i dan MyClass.f adalah referensi atribut yang valid, masing - masing mengembalikan integer dna objek fungsi. doc juga merupakan atribut yang valid, mengembalikan docstring milik kelas: "A simple example class".

# 9.3.3. Instance Objects

Data attributes sesuai dengan "variabel instan" di Smalltalk, dan "data members" di C++. Atribut data tidak perlu dinyatakan; seperti variabel lokal, mereka muncul ketika mereka pertama kali ditugaskan.

# 9.3.4. Method Objects

Dalam contoh MyClass, ini akan mengembalikan string 'hello world'. Namun, tidak perlu memanggil metode segera: x.f adalah metode objek, dan dapat disimpan dan dipanggil di lain waktu

# 9.3.5. Class and Instance Variables

Variabel instance adalah untuk data unik untuk setiap instance dan variabel kelas adalah utnuk atribut dan metode yang dibagikan oleh semua instance kelas

# 9.4. Random Remarks 

Jika nama atribut yang sama muncul di kedua instance dan di kelas, maka pencarian atribut memprioritaskan instance

Seringkali, argument pertama dari suatu metode disebut self

Sekarang f, g, dan h adalah semau atribut class C yang merujuk ke objek - objek fungsi, dan akibatnya semaunya adalah metode instance dari C -- h sama persis dengan g.

# 9.5 Inheritance

Nama BaseClassName harus didefinisikan dalam lingkup yang berisi definisi kelas turunan. Di tempat nama kelas dasar, ekspresi berubah-ubah arbitrary lainnya juga diperbolehkan.

Eksekusi definisi kelas turunan menghasilkan sama seperti untuk kelas dasar. Tidak ada yang istimewa tentang instance kelas turunan: DerivedClassName() membuat instance baru di kelas.

Python memiliki dua fungsi bawaan yang bekerja dengan warisan:

    * Gunakan ininstance() untuk memeriksa jenis instance: isintance(obj, int) akan menjadi True hanya jika obj.__class__ adalah init atau beberapa kelas yang diturunkan dari init.
    * Gunakan issubclass() untuk memeriksa warisn kelas: issubclass(bool, int) ``adalah ``True karena bool adalah subkelas dari int. Namun, issubclass(float, int) adalah False karena float bukan subkelas dari int.

# 9.5.1. Multiple Inheritance

Python mendukung bentuk pewarisan berganda

# 9.6. Private Variables

Variabel instance "Private" yang tidak dapat diakses kecuali dari dalam suatu objek tidak ada dalam Python. Setiap pengidentifikasi dari bentuk __spam (setidaknya dua garis bawah utama, paling banyak satu garis bawah garis bawah) secara teks diganti dengan _classname__spam, di mana classnameadalah nama kelas saat ini dengan garis(-garis) bawah utama dilucuti. Mangling ini dilakukan tanpa memperhatikan posisi sintaksis pengidentifikasi, asalkan terjadi dalam definisi kelas.

Name mangling sangat membantu untuk membiarkan subclass menimpa metode tanpa memutus panggilan metode intraclass.

# 9.7. Odds and Ends

Kita dapat mendefinisikan kelas dengan metode read() dan readline() yang mendapatkan data dari buffer string sebagai gantinya, dan meneruskan itu sebagai argumen. metode instance memiliki atribut, juga: m.__self__ adalah objek instan dengan metode m(), dan m.__func__adalah objek fungsi yang sesuai dengan metode tersebut.

# 9.8. Iterators 

Sekarang kita mungkin telah memperhatikan bahwa sebagian besar objek penampungan container dapat dibuat perulangan menggunakan pernyataan for 

# 9.9. Generators

Generators adalah sebuah tool yang sederhana dan simpel untuk membuat sebuah iterasi. Itu ditulis seperti fungsi biasa tapi menggunakan pernyataan yield setiap kali ingin mengembalikan sebuah data. Tiap kali next() itu dipanggil, generators tersebut akan melanjutkan di mana hal itu berhenti (itu akan mengingat semua nilai dan pernyataan mana yang terakhir dieksekusi).

# 9.10. Generator Expressions

Beberapa pembangkit generators sederhana dapat dikodekan secara ringkas sebagai ekspresi menggunakan sintaksis yang mirip dengan pemahaman daftar list comprehensions tetapi dengan tanda kurung bukan dengan tanda kurung siku. Ungkapan-ungkapan ini dirancang untuk situasi di mana generator digunakan segera oleh fungsi penutup. Ekspresi generator lebih kompak tetapi kurang fleksibel daripada definisi generator penuh dan cenderung lebih ramah memori daripada pemahaman daftar list comprehensions setara.

