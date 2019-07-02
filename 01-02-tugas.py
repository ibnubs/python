#tugas hari kedua

# 1. diberikan string input, hitung masing-masing jumlah huruf, angka dan simbol input dimasukkan manual

# contoh input: abcg123##

# contoh outpunya: huruf:4, angka:3, simbol:2 

# 2.Tulis program untuk membuat tabel perkalian (dari 1 ke 10)dari sebuah number.
# input di masukkan manual

# contoh input : 2
# contoh outpunya :
# 2x1=2
# 2x2=4
# dst.

# Jawaban Soal 1

x = input('Masukan Sembarang Karakter:');

hitungAngka = 0;
hitungHuruf = 0;
hitungSimbol = 0;

for element in x:
  if element.isnumeric() == True:
    hitungAngka = hitungAngka + 1
  elif element.islower() == True or element.isupper () == True:
    hitungHuruf = hitungHuruf +1
  else:
    hitungSimbol = hitungSimbol +1 

print("angka = {}, huruf {}, simbol {}".format(hitungAngka,hitungHuruf,hitungSimbol))


#Jawaban Soal 2

a = int(input("Input Perkalian:"))

for b in range(1,11):

  print("{} x {} = {}". format(b,a,b*a))




