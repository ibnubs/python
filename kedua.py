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

a = int(input("Input Perkalian:"))

for b in range(1,11):

  print("{} x {} = {}". format(b,a,b*a))

