"""
berbeda dengan bahasa C, bahasa python dalam mendeklarasikan tipe data 
tidak perlu menuliskan tipe datanya
"""

x = 17 # tipe data int
y = "farel" # string
print(x)
print(y)

#bahkan ketika ingin mengubah nilai yang ada di dalam varibel 
#yang awalnya integer kita bisa langsung mengubah tipe data nya berdasarkan nilai yang diberikan

a = 17        # x int
a = "fakhrelll" # x berubah nilai dengan tipe data string
print(a)

"""
jika ingin mengubah suatu nilai, misal secara default angka 17 itu adalah integer
angka tersebut bisa diubah tipe data selain integer
"""
b = str(17)    # x = '3'
c = int(17)    # y = 3
d = float(17)  # z = 3.0

#cara lihat tipe data dari suatu variabel
print(type(x))
print(type(y))

z = 4
Z = "Sally"
#ini adalah 2 variabel berbeda walaupun dengan huruf yang sama dikarenakan besar kecilnya nama variabel 

#ATURAN PENULISAN NAMA VARIABEL DI PYTHON

"""
nama variabel diawali dengan huruf
tidak boleh angka duluan 
2myvar = "kjcsdbv"
"""
myvar = "rel"
my_var = "rel"
_my_var = "rel"
myVar = "rel"
MYVAR = "rel"
myvar2 = "rel"

#Camel case
myNamaAku = "rel"
#Pascal case
MyNamaAku = "rel"
#snake case
my_nama_aku = "rel"
"""
kebanyakan orang lebih sering pakai Pascal case untuk bahasa pyhton
"""

#MUlTIPLE VALUE & VARIABEL 
""" 
kalau di bahasa C 
int a= 1, b= 2, c = 3;
"""
x, y, z = "Orange", "Banana", "Cherry" #kalau python setiap value akan ditempatkan sesuai urutan dari variabel

x = y = z = "Orange" #satu value untuk setiap/semua variabel, output nya x y z akan memmiliki nilai yang sama

fruits = ["apple", "banana", "cherry"]
a, b, c = fruits #setiap variabel mengesktrak nilai atau list dari variabel fruits
print(a)
print(b)
print(c)


#OUTPUT VARIABLE
x = "Python" #tidak memerlukan spasi tambahan diakhir kata
y = "is"
z = "awesome"
print(x, y, z)

x = "Python " #memerlukan spasi
y = "is "
z = "awesome"
print(x + y + z)
#!!tidak bisa menggabungkan int + string!!
""" x = 17
y = "Rel"
print(x + y)
print(x, y) #dengan koma (,) bisa
"""
#GLOBAL VARIABLE
x = "haloooo" #variabel global adalah varibel yang berada di luar suatu function atau tidak di dalam function

def mykisah():
  x = "fantastic"
  print("Kamu adalah " + x) #output : Kamu adalah fantastic

mykisah()
print("Kamu adalah " + x) #output : Kamu adalah haloooo
#bisa juga menggunakan keyword global
def myfunc():
  global x #variabel x yang berada di dalam fucntion menjadi global(bisa digunakan diluar function)
  x = "fantastic"

myfunc()

print("Python is " + x) #outpur: Python is fantastic

