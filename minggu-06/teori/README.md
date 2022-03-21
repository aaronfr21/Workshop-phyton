# Penanganan Error dan Exception

Sampai sekarang pesan kesalahan belum lebih dari yang disebutkan, tetapi jika kita telah mencoba contoh mungkin telah melihat beberapa. Berikut ini adlah bebarapa error dalam pyhton

# Syntax Errors

Kesalahan sintaks, juga dikenal sebagai kesalahan penguraian, mungkin merupakan jenis keluhan paling umum yang Anda dapatkan saat Anda masih belajar Python.

# Exceptions

Bahkan jika suatu pernyataan atau ekspresi secara sintaksis benar, hal itu dapat menyebabkan kesalahan ketika dilakukan upaya untuk mengeksekusinya. Kesalahan yang terdeteksi selama eksekusi disebut pengecualian dan tidak fatal tanpa syarat: Anda akan segera mempelajari cara menanganinya dalam program Python. Namun, sebagian besar pengecualian tidak ditangani oleh program, dan menghasilkan pesan kesalahan

# Handling Exceptions

Dimungkinkan untuk menulis program yang menangani pengecualian yang dipilih. Klausa kecuali dapat menentukan variabel setelah nama pengecualian. Variabel terikat ke instance pengecualian dengan argumen yang disimpan di instance.args. Untuk kenyamanan, instance pengecualian mendefinisikan __str__()sehingga argumen dapat dicetak secara langsung tanpa harus reference .args. Seseorang juga dapat membuat instance pengecualian terlebih dahulu sebelum menaikkannya dan menambahkan atribut apa pun ke dalamnya seperti yang diinginkan. Jika pengecualian memiliki argumen, mereka akan dicetak sebagai bagian terakhir ('detail') dari pesan untuk pengecualian yang tidak ditangani

# Raising Exceptions

Pernyataan raise tersebut memungkinkan programmer untuk memaksa pengecualian tertentu terjadi. Satu-satunya argumen untuk raisemenunjukkan pengecualian yang akan diajukan. Ini harus berupa instance pengecualian atau kelas pengecualian (kelas yang berasal dari Exception). Jika kelas pengecualian dilewatkan, itu akan secara implisit dipakai dengan memanggil konstruktornya tanpa argumen

# Exception Chaining

Pernyataan raisi memungkinkan opsional yang memungkinkan pengecualian rantai. Rantai pengecualian terjadi secara otomatis ketika pengecualian dinaikkan di dalam bagian kecuali atau akhirnya. Ini dapat dinonaktifkan dengan menggunakan dari None idiom

# User-defined Exceptions

Exceptions biasanya harus diturunkan dari kelas Exceptions, baik secara langsung maupun tidak langsung. Kelas Kelas pengecualian dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya dibuat sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk Kelas pengecualian dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya dibuat sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk Kelas pengecualian dapat didefinisikan yang melakukan apa pun yang dapat dilakukan kelas lain, tetapi biasanya dibuat sederhana, seringkali hanya menawarkan sejumlah atribut yang memungkinkan informasi tentang kesalahan diekstraksi oleh penangan untuk Exceptions

# Defining Clean-up Actions

Pernyataan try memiliki klausa opsional lain yang dimaksudkan untuk mendefinisikan tindakan pembersihan yang harus dilakukan dalam semua keadaan. Dalam aplikasi dunia nyata, klausa last berguna untuk melepaskan sumber daya eksternal (seperti file atau koneksi jaringan), terlepas dari apakah penggunaan sumber daya itu berhasil.

# Predefined Clean-up Actions

Beberapa objek menentukan tindakan pembersihan standar yang harus dilakukan ketika objek tidak lagi diperlukan, terlepas dari apakah operasi menggunakan objek berhasil atau gagal.