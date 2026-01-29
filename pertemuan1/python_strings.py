"""
Slicing  mengambil sebagian (substring) dari sebuah string berdasarkan posisi karakter.
bisa ditentukan dari mana mulai dan sampai mana yang ingin diambil karakternya
"""
#string memiliki urutan karakter yang dimulai dari index 0 
"A s s a l a m u a l  a  i  k  u  m"
#0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
b = "Assalamualaikum, Dunia!"
print(b[2:5]) # 2 --> posisi huruf pertama yang ingin diambil : s
              # 5 --> posisi huruf berhenti atau terakhir dan tidak masuk(ke print) atau hilang
print(b[2:])  # mengambil karakter dari indek ke 2 dan tidak ada berhenti, output: salamualaikum, Dunia!
print(b[:5])  # menentukan batas karakter yang ingin di ambil, ouput: Assal

"D  u  n  i  a"
-5 -4 -3 -2 -1
print(b[-5:-2]) # berarti dari huruf ke 5 dari belakang sampai huruf 
                #ke 2 dari belakang, output: Duni

#Modify String
a = "Assalamualaikum, Dunia!"
print(a.upper()) #Upper case method yang mengubah semua huruf menjadi kapital
print(a.lower())
a = "      Assalamualaikum, Dunia!"
print(a.strip()) # menghapus spasi atau tab, output: Assalamualaikum, Dunia!
                 # tanpa method strip, output:       Assalamualaikum, Dunia!
print(a.replace("A", "J")) #method yang menimpa karakter sebelumnya dengan yang baru, outpur: Jass...

#Split string
"""
memecah sebuah string menjadi beberapa bagian 
yang bisa dikatakan menjadi tipe data list
"""

text = "Aku Belajar Python"
print(text.split()) #paramerter kalau tidak disi berarti method ini akan memecah berdasarkan spasi
                    #output : ['Aku', 'Belajar', 'Python'] 
text = "Aku, Belajar Python, ,"
print(text.split(","))#paramerter method ini akan memecah berdasarkan koma
                    #output : ['Aku', ' Belajar Python', ' ', '']

#Concatenate 
a = "Hello"
b = "World"
c = a + b #menggabungkan string dengan menggunakan + dan menyimpan ke variabel c
print(c) #output: HelloWorld

c = a + " " + b #tambahkan string ("") untuk spasi
print(c) #output: Hello World

#Format String
"""
age = 20
txt = "My name is Rel, I am " + age
print(txt) #ini akan error, karena tidak bisa menggabungkan string dengan variabel bertipe integer
"""

"""
tambahkan huruf f sebelum tanda kutip, lalu pakai kurung kurawal {} 
sebagai tempat untuk memasukkan nilai variabel:
"""
age = 20
txt = f"My name is Rel, I am {age}"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt) #Menjalankan operasi matematika

#Escape Characters
"""
digunakan jika terdapat string yang digunakan untuk memperjelas kalimat atau kata 
misal: print("aku adalah seorang yang \"baik\" ") #bisa menggunakan salah satu escape
"""


#String Methods

"""
capitalize(): digunakan mengubah karakter pertama menjadi huruf besar
casefold(): Mmengubah semua karakter string ke huruf kecil (lebih agresif dari lower())
title(): mengubah karakter pertama setiap kata menjadi huruf besar
translate(): mengembalikan string hasil terjemahan
upper(): mengubah semua karakter dalam string menjadi huruf besar
zfill(): mengisi string dengan angka 0 di awal hingga mencapai panjang tertentu
"""