# Komentar dalam Python dimulai dengan karakter hash  dan 
# diperpanjang hingga akhir baris fisik.
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

#kalkulator
2 + 2
50 - 5*6
(50 - 5*6) / 4
8 / 5 # memberikan hasil berupa float

#pembagian
17/3
17 // 3 # menghilangkan nilai pecahan pada hasil pembagian
17%3 # module (sisa bagi)
5 * 3 + 2 # gabungan, akan di eksekusi perkalian / bembagian dahulu

#pangkat
5  ** 2
2 ** 7

#variabel
width = 20
heigh = 5*9
width * height #mengalikan nilai di dalam kedua variabel

n # pemanggilan variabel yang belum ada nilainya akan error

#menghitung campuran tipe data
4 * 3.75 - 1 # integer dengan float

# Dalam mode interaktif, ekspresi tercetak terakhir ditetapkan ke variabel _
tax = 12.5/100
price = 100.50
price * tax
price +_ # prce ditambah dengan ekspresi terakhir, yaitu price * tax
round(_,2) 

# STRING
'spam eggs'  # single quotes
'doesn\'t'  # use \' to escape the single quote...
"doesn't"  # ...or use double quotes instead
'"Yes," they said.'
"\"Yes,\" they said."
'"Isn\'t," they said.'

#print()menghasilkan keluaran yang lebih mudah dibaca
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output
print(s)

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote

#String literal dapat menjangkau beberapa baris. Salah satu caranya adalah menggunakan tanda kutip tiga: """..."""atau '''...'''
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#String dapat digabungkan (direkatkan) dengan +operator, dan diulang dengan *
# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'

# Dua atau lebih literal string di samping satu sama lain secara otomatis digabungkan.
'Py' 'thon'

text = ('Put several strings within parentheses '
    'to have them joined together.')
text

#Ini hanya berfungsi dengan dua literal, tidak dengan variabel atau ekspresi
prefix = 'Py'
prefix 'thon'  # can't concatenate a variable and a string literal
('un' * 3) 'ium'

# menggabungkan variabel atau variabel dan literal, gunakan +
prefix + 'thon

# pengindexan kata
word = 'Python'
word[0]  # character in position 0
word[5]  # character in position 5

# Indeks juga bisa berupa angka negatif, untuk mulai menghitung dari kanan:
word[-1]  # last character
word[-2]  # second-last character
word[-6]

# pengindeksan digunakan untuk mendapatkan karakter individu
word[0:2]  # characters from position 0 (included) to 2 (excluded)
word[2:5]  # characters from position 2 (included) to 5 (excluded)

# indeks pertama yang dihilangkan defaultnya adalah nol, 
# indeks kedua yang dihilangkan defaultnya adalah ukuran string yang diiris.
word[:2]   # character from the beginning to position 2 (excluded)
word[4:]   # characters from position 4 (included) to the end
word[-2:]  # characters from the second-last (included) to the end

word[:2] + word[2:] #menampilkan awal sampai akhir
word[:4] + word[4:]

word[42]  # the word only has 6 characters
#error

#indeks irisan di luar jangkauan
word[4:42]
word[42:]

#String Python tidak dapat diubah
word[0] = 'J' # error karena mengubah menjadi j
word[2:] = 'py'

# Jika membutuhkan string yang berbeda,  harus membuat yang baru:
'J' + word[1:]
word[:2] + 'py'

# mengembalikan panjang string
s = 'supercalifragilisticexpialidocious'
len(s)


# 3.1.3 DAFTAR
squares = [1, 4, 9, 16, 25]
squares

#index daftar
squares[0]  # indexing returns the item
squares[-1]
squares[-3:]  # slicing returns a new list

# operasi irisan mengembalikan daftar baru yang berisi elemen yang diminta
squares[:]

#penggabungan
squares + [36, 49, 64, 81, 100]

# mengubah daftar
 cubes = [1, 8, 27, 65, 125]  # something's wrong here
 cubes[3] = 64
 cubes

 # menambahkan item baru di akhir daftar
 cubes.append(216)  # add the cube of 6
 cubes.append(7 ** 3)  # and the cube of 7
 cubes

 # Penetapan irisan
 letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
 letters
 letters[2:5] = ['C', 'D', 'E']
 letters
 letters[2:5] = []
 letters
 # clear the list by replacing all the elements with an empty list
 letters[:] = []
 letters

 # Fungsi len()bawaan juga berlaku untuk daftar
 letters = ['a', 'b', 'c', 'd']
 len(letters)

# daftar bersarang
 a = ['a', 'b', 'c']
 n = [1, 2, 3]
 x = [a, n]
 x
 x[0]
 x[0][1]

# Langkah Pertama Menuju Pemrograman
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b


i = 256*256
print('The value of i is', i) # menampilkan gabungan string dan variabel

 a, b = 0, 1
  while a < 1000:
    print(a, end=',') # end untuk mengakhiri perulangan
    a, b = b, a+b
