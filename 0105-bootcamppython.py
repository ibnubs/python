"""tugas1. Tulis program untuk menghitung jumlah hari senin yang bertepatan tanggal 1 di setiap bulan , dari tahun 2015 s.d. 2016"""

from datetime import datetime

date1 = datetime.date(2015,1,1)
date2 = datetime.date(2016,12,31)
day = datetime.timedelta(days=1)


while date1 <= date2:
            print (date1.strftime('%Y.%m.%d'))
            date1 = date1 + day



"""solusi bang arno"""
# import datetime
# from datetime import datetime
# monday1=0
# months= range(1,13)
# for year in range(2015,2017):
#     for month in months:
#         if datetime (year, month, 1).weekday() == 0:
#             monday1 +=1
# print(monday1)






"""Tugas2. Buatlah kelas yang memiliki setidaknya dua method:"""
"""getString: untuk mendapatkan string dari inputan konsol"""
"""printString: untuk mencetak string dalam huruf besar."""

"""Jawaban Soal"""
# class capitalWord:

#     print ("Silahkan masukan sembarang kata = ")
# geStringt=input()
# printString=geStringt.upper()
# print(printString)


"""solusi dari mas Arno"""
# class InputOutputString(object):
#     def __init__ (self):
#         self.s=""
#     def getString(self):
#         self.s = input()
#     def printString (self):
#         print(self.s.upper())

# strObj = InputOutputString()
# strObj.getString()
# strObj.printString()
