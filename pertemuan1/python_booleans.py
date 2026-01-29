#Boolean memiliki dua nilai True atau False

#menentukan nilai dari suatu kondisi dengan menggunakan operator perbandingan
print(20 > 9) #True
print(20 == 9) #False
print(20 < 9) #False

#menentukan apakah suatu kondisi bernilai true atau false
a = 200
b = 33

if b > a:
  print("b lebih besar dari a")
else:
  print("b lebih kecil dari a")

print(bool("Hello")) #mengubah nilai menjadi boolean
print(bool(15))

#nilai yang di aggap False
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

#function bisa return boolean
def myFunction() :
  return True

if myFunction(): #if ini akan dijalankan jika function me return nilai true
  print("YES!")
else:
  print("NO!")