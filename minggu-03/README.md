BAB 5 STRUKTUR DATA 
Pada bab ini dijelaskan beberapa hal yang telah kita pelajari menjadi lebih rinci, serta menambahkan beberapa hal baru 

Struktur data adalah cara kita dalam menyimpan dan mengambil data. Anda mungkin sudah terbiasa dengan daftar dan kamus Python atau array Javascript dan objek. Jika demikian, Anda tahu bahwa daftar dan array berurutan dengan data yang diakses oleh indeks sementara kamus dan objek menggunakan kunci bernama untuk menyimpan dan mengambil informasi.

#List / Daftar
Berikut ini merupakan method list:

list.append(x) :Tambahkan item ke akhir daftar
list.extend(iterable) : Perluas daftar dengan menambahkan semua item dari iterable
list.insert(i, x) : Masukkan item pada posisi tertentu. Argumen pertama adalah indeks elemen yang akan disisipkan sebelumnya
list.remove(x) : Hapus item pertama dari daftar yang nilainya sama dengan x 
list.pop([i]) : Hapus item pada posisi yang diberikan dalam daftar, dan kembalikan. Jika tidak ada indeks yang ditentukan
list.clear() : Hapus semua item dari daftar
list.index(x[, start[, end]]) : Kembalikan indeks berbasis nol dalam daftar item pertama yang nilainya sama dengan x
list.count(x) : Kembalikan berapa kali x muncul dalam daftar
list.sort(*, key=None, reverse=False) Urutkan item dari daftar di tempat (argumen dapat digunakan untuk penyesuaian pengurutan
list.reverse() : Balikkan elemen daftar di tempatnya
list.copy() : Kembalikan salinan daftar yang dangkal

#Menggunakan Daftar Sebagai Tumpukan

Metode daftar membuatnya sangat mudah untuk menggunakan daftar sebagai tumpukan, di mana elemen terakhir yang ditambahkan adalah elemen pertama yang diambil ("masuk terakhir, keluar pertama"). Untuk menambahkan item ke bagian atas tumpukan, gunakan append(). Untuk mengambil item dari atas tumpukan, gunakan pop()tanpa indeks eksplisit

#Menggunakan Daftar Sebagai Antrian

Dimungkinkan juga untuk menggunakan daftar sebagai antrian, di mana elemen pertama yang ditambahkan adalah elemen pertama yang diambil ("masuk pertama, keluar pertama"); namun, daftar tidak efisien untuk tujuan ini. Sementara menambahkan dan muncul dari akhir daftar cepat, melakukan sisipan atau muncul dari awal daftar lambat (karena semua elemen lain harus digeser satu).

#Pemahaman Daftar

Pemahaman daftar menyediakan cara ringkas untuk membuat daftar. Aplikasi umum adalah untuk membuat daftar baru di mana setiap elemen adalah hasil dari beberapa operasi yang diterapkan ke setiap anggota dari urutan lain atau iterable, atau untuk membuat suburutan dari elemen-elemen yang memenuhi kondisi tertentu

#Pemahaman Daftar Bersarang

Ekspresi awal dalam pemahaman daftar dapat berupa ekspresi arbitrer, termasuk pemahaman daftar lainnya.

#Del Statements

Ada cara untuk menghapus item dari daftar yang diberikan indeksnya alih-alih nilainya: delpernyataan. Ini berbeda dari pop()metode yang mengembalikan nilai. Pernyataan deljuga dapat digunakan untuk menghapus irisan dari daftar atau menghapus seluruh daftar (yang kita lakukan sebelumnya dengan menetapkan daftar kosong ke irisan)

#Tuples & Sequences

Tuple adalah kumpulan objek yang dipesan dan tidak dapat diubah. Tuple adalah urutan, seperti halnya daftar. Perbedaan antara tupel dan daftar adalah, tupel tidak dapat diubah tidak seperti daftar dan tupel menggunakan tanda kurung, sedangkan daftar menggunakan tanda kurung siku

#Sets

Python juga menyertakan tipe data untuk set . Himpunan adalah kumpulan yang tidak berurutan tanpa elemen duplikat. Penggunaan dasar termasuk pengujian keanggotaan dan menghilangkan entri duplikat. Set objek juga mendukung operasi matematika seperti serikat pekerja, persimpangan, perbedaan, dan perbedaan simetris.

#Dictionaries

Kamus kadang-kadang ditemukan dalam bahasa lain sebagai "ingatan asosiatif" atau "array asosiatif". Tidak seperti urutan, yang diindeks oleh rentang angka, kamus diindeks oleh kunci , yang dapat berupa tipe apa pun yang tidak dapat diubah; string dan angka selalu bisa menjadi kunci. Tuple dapat digunakan sebagai kunci jika hanya berisi string, angka, atau tupel; jika sebuah tuple berisi objek yang bisa berubah baik secara langsung maupun tidak langsung, itu tidak dapat digunakan sebagai kunci. Operasi utama pada kamus adalah menyimpan nilai dengan beberapa kunci dan mengekstrak nilai yang diberikan kunci tersebut

#Looping Techniques

Saat mengulang dictionary, kunci dan nilai yang sesuai dapat diambil secara bersamaan menggunakan metode items()

#More on Conditions

Kondisi yang digunakan dalam pernyataan while dan if dapat berisi operator apa saja, bukan hanya perbandingan. Perbandingan dapat digabungkan menggunakan operator Boolean dan dan atau, dan hasil perbandingan (atau ekspresi Boolean lainnya) dapat dinegasikan dengan not.

#Comparing Sequences and Other Types

Objek urutan biasanya dapat dibandingkan dengan objek lain dengan jenis urutan yang sama. Perbandingan menggunakan urutan leksikografis: pertama dua item pertama dibandingkan, dan jika berbeda, ini menentukan hasil perbandingan; jika mereka sama, dua item berikutnya dibandingkan, dan seterusnya, sampai salah satu urutan habis.
