"""
print("Hello World")


a=1;
b=2;
c=a+b;
print(c);

if 5>2:
  print("Five is greater than two!")


# test komen

# test komen banyakan pakai kutip tiga kali

x = "awesome";
print("Python is " + x);


x=1;
y=2.8;
z=1j;

print(type(x));
print(type(y));
print(type(z));


x=2;
y=2.8;
z=1j;

a=float(x);
b=int(y);
c=complex(x);

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#belajar casting
#contoh integer
x=int(1);
y=int(2.8);
z=int("3");

print(x,y,z)

#contoh float
x=float(1);
y=float(2.8);
z=float("3");
w=float("4.2");

print(x,y,z,w);

#contoh string
x = str("s1");
y = str(2);
z = str(3.0);

print(x,y,z)


z="2 orang";

print(z[0]);

a="Lorem Ipsum
print(a)



a="hello world"
print(a[2:5]);


a="hello, world"
print(a.replace("o","0"))
print(a.split("w"))


age = 36
txt = "My name is John, I am " + str(age)
print(txt)



age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

age = 36
txt = "My name is John, and I am {}"
print(txt)


quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))





thislist = ["apple", "banana", "cherry"]
# print(thislist) #menghasilkan semuanya
# print(thislist[2]) #menampilkan satu saja
# thislist[0] = "jeruk"
# print(thislist)

# for x in thislist:
#   print(x)

# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")


mylist = thislist.copy()
print(mylist)

# bedanya thislist bisa di declare dan di add atau diubah2, tapi kalau thistuple tidak bisa diubah2,,


thistuple = ("apple", "banana", "cherry")
print(thistuple)

tambah sendiri contoh2nya



thisset = {"apple", "banana", "cherry"}
print(thisset)




thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict["model"]
print(x)




a=330;
b=200;
if b>a:
  print("true")
else:
  print("false")


i = 1
while i < 6:
  i += 1 
  print(i)


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

for x in "banana":
  print(x)


adj = ["red", "big", "tasty", "jeruk"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
harga = [5000,2000,1500]

for x in adj:
  for y in fruits:
    for z in harga:
      print(x, y, z)


def my_function():
  print("Hello from a function")

my_function()


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


print("hello world")



def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(0)

"""


sum = 0
start = 10
end = 30
for i in range(start, end+1):
    sum += i
 
print("Sum is", sum)