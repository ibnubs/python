# belajar iterasi
# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))


# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# # myclass = MyNumbers()
# # myiter = iter(myclass)
# # print(myclass)
# # print(MyNumbers)
# # print(myiter)

# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))
# # print(next(myiter))

# myclass = MyNumbers()
# myiter = iter(myclass)


# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))
# print(next(myclass))


# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#   print(x)

# belajar modul
# import modul
# modul.greeting("Elga purwacaraka")


# a = modul.person1["age"]
# print(a)
# print(modul.person1, len(modul.person1))


# for x in modul.person1:
#     print(x, modul.person1[x])


# import platform

# x = platform.system()
# print(x)
# y = dir(platform)
# print(y)
# import datetime
# from modul import greeting, person1

# print (person1["age"])

# x=datetime.datetime.now()
# print(x)


# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# # use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
# print(json.dumps(x, indent=2 separators=(". ", " = ")))

# belajar regular expression

# def is_phone_number(text):
#     if len(text) != 11:
#         return False
#     for i in range(0, 3):
#         if not text[i].isdecimal():
#             return False
#     if text[3] != ' ':
#         return False
#     for i in range(4, 11):
#         if not text[i].isdecimal():
#             return False
#     return True


# print('021 8229311 adalah nomor telepon:')
# print(is_phone_number('021 8229311'))
# print('Hello Hello adalah nomor telepon:')
# print(is_phone_number('Hello Hello'))



# import re

# #Replace all white-space characters with the digit "9":

# str = " The rain in Spain"
# x = re.sub("\s","", str, 1)
# print(x)


# import camelcase

# c = camelcase.CamelCase()

# txt = "lorem ipsum dolor sit amet"

# print(c.hump(txt))

#This method capitalizes the first letter of each word.


print("Enter your name:")
x = input()
print("Hello ", x)