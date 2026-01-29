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
a = "fakhrel" # x berubah nilai dengan tipe data string
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