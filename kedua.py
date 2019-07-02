# def myFunction(food ):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# myFunction(fruits)

# lambda arguments : expression

# x = lambda a : a + 10
# print(x(5))


# x = lambda a, b : a * b
# print(x(5, 6))


# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(3))


# a = int(input("konversi F to C = "))

# hasil=(a - 32)*(5/9)
# print(float(hasil))


total = 1000
# Variabel global 
# Definisi fungsi 
def sum( arg1, arg2 ): 
    """Menambahkan variabel dan mengembalikan hasilnya."""
    total = arg1 + arg2; 
    # total di sini adalah variabel lokal 
    print ("Di dalam fungsi nilai total : ", total) 
    return total 

# Pemanggilan fungsi sum 
sum( 10, 20 ) 
print ("Di luar fungsi, nilai total : ", total ) 
