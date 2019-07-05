"""this excercise from Mosh Hamedi"""
"""from url https://programmingwithmosh.com/python/python-exercises-and-questions-for-beginners/"""

"""primitive type"""
"""Assuming (name = “John Smith”), what does name[1] return?"""
# name="John Smith"
# print (name[1]) #0
# print (name[-2]) #t
# print (name[1:-1]) #ohn Smit
# print (name.__len__()) #10
# print(f"{2+2}+{10%3}") #4+1
# print(name.title())#John Smith -->J jadi hurus besar
# print(name.strip())#John Smith --> delete spasi di awal kalimat
# print(name.find("Smith"))#5 --> mengeluarkan hasil S ada di urutkan aray ke berapa
# x = name.replace("J","K") # kohn Smith
# x = name.findall("John")#0
# print(x) #

"""control flow"""
"""beda 10/3 dan 10//3"""
# x=10/3
# y=10//3
# z=10**3
# print('ini hasil x=',x) #ini hasil x= 3.3333333333333335
# print('ini hasil y=',y) #ni hasil y= 3
# print (z) #1000

"""Given (x = 1), what will be the value of after we run (x += 2)?"""
# x=1
# print (x) #1
# x+=2
# print ("nilai x setelah di assign nilai baru =", x) #3
# print(float(1)) #1.0
# print(bool("False")) #True
# z = 10 =="10" #False
# x = "bag" > "apple" #True
# x=not(True or False) #false
""" chaining comparion operators"""
# age = 50
# if 18 <= age < 65:
#     print("Lulus")
# else:
#     print("Gagal")

# for nomor in range(1,10,2): #range (batas bawah, batas atas, interval)
#     print ("belajar range-" + str(nomor))


"""coding exercise"""
"""Write a function that returns the maximum of two numbers."""
# def retMax (a,b):
#     if a>b:
#         return a
#     return b
# print(retMax(6,5))



# def fizz_buzz(x):
#     if x % 3 ==0 and x % 5 == 0: 
#         return "FizzBuzz"
#     elif x % 5 == 0 :
#         return "Buzz"
#     elif x % 3 == 0: 
#         return "Fizz"
#     return x
# j = int(input("masuk: "))

# print (fizz_buzz(j))
# #print (fizz_buzz(5))
# #print (fizz_buzz(15))
# #print (fizz_buzz(50))


# def cekSpeed (speed):
#     intpoint=0
#     limit=70
#     ovSpeed=0
#     maxPoint=12
    
#     if speed <= limit:
#         print ("Ok")
#     elif speed >= limit:
#          ovSpeed= speed - limit
#          point = ovSpeed / 5
#          if point <=12:
#             print (f"Pelanggaran Point Anda sudah {int(point)}")
#          else:
#              print (f"Pelanggaran Point lebih dari {int(point)} dan your License suspend")

# cekSpeed(50)
# cekSpeed(80)
# cekSpeed(150)


