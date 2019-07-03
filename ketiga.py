#day3 learn python

# class Person:
#   def say_hi(self):
#     print("Hello, How are you")

# p = Person()
# p.say_hi()
# p1 = Person() #bisa dibuat sebanyak2nya
# p1.say_hi()

#method init
# class Person:
#     def __init__(self, name):
#       self.name = name

#     def say_hi(self):
#       print('Hello, my name is', self.name)

# p = Person('Swaroop')
# p.say_hi()

#Modifikasi lebih kompleks
# class Person:
#     def __init__(self, name, age):
#       self.name = name
#       self.age = age

#     def say_hi(self):
#       print('Hello, my name is', self.name, 'and iam', self.age, ' years old')

# p = Person('Swaroop','19')
# p.say_hi()

#Modifikasi lebih kompleks dengan format
# class Person:
#     def __init__(self, name, age):
#       self.name = name
#       self.age = age
#       self.address = address

#     def say_hi(self):
#       print(f'Hello, my name is {self.name} and iam {self.age} years old')

# p = Person('Swaroop','19', 'Sheldon Extension' )
# p2 = Person('Johson','20', '180 Darrel Row')
# p.say_hi()
# p2.say_hi()


#Class

# class Robot:
#     """Represents a robot, with a name."""

#     # A class variable, counting the number of robots
#     population = 0

#     def __init__(self, name):
#         """Initializes the data."""
#         self.name = name
#         print("(Initializing {})".format(self.name))

#         # When this person is created, the robot
#         # adds to the population
#         Robot.population += 1

#     def die(self):
#         """I am dying."""
#         print("{} is being destroyed!".format(self.name))

#         Robot.population -= 1

#         if Robot.population == 0:
#             print("{} was the last one.".format(self.name))
#         else:
#             print("There are still {:d} robots working.".format(
#                 Robot.population))

#     def say_hi(self):
#         """Greeting by the robot.

#         Yeah, they can do that."""
#         print("Greetings, my masters call me {}.".format(self.name))

#     @classmethod
#     def how_many(cls):
#         """Prints the current population."""
#         print("We have {:d} robots.".format(cls.population))


# droid1 = Robot("R2-D2")
# droid1.say_hi()
# Robot.how_many()

# droid2 = Robot("C-3PO")
# droid2.say_hi()
# Robot.how_many()

# print("\nRobots can do some work here.\n")

# print("Robots have finished their work. So let's destroy them.")
# droid1.die()
# droid2.die()

# Robot.how_many()



# class SchoolMember:
#     '''Represents any school member.'''
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print('(Initialized SchoolMember: {})'.format(self.name))

#     def tell(self):
#         '''Tell my details.'''
#         print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


# class Teacher(SchoolMember):
#     '''Represents a teacher.'''
#     def __init__(self, name, age, salary):
#         SchoolMember.__init__(self, name, age)
#         self.salary = salary
#         print('(Initialized Teacher: {})'.format(self.name))

#     def tell(self):
#         SchoolMember.tell(self)
#         print('Salary: "{:d}"'.format(self.salary))


# class Student(SchoolMember):
#     '''Represents a student.'''
#     def __init__(self, name, age, marks):
#         SchoolMember.__init__(self, name, age)
#         self.marks = marks
#         print('(Initialized Student: {})'.format(self.name))

#     def tell(self):
#         SchoolMember.tell(self)
#         print('Marks: "{:d}"'.format(self.marks))

# t = Teacher('Mrs. Shrividya', 40, 30000)
# s = Student('Swaroop', 25, 75)

# # prints a blank line
# print()

# members = [t, s]
# for member in members:
#     # Works for both Teachers and Students
#     member.tell()



"""gagalgagal"""
# #object
# class Hero:
#   #class variabel
#   jumlah_hero = 0

# def __init__ (inputName, inputHealth):
#   name = inputName
#   health = inputHealth

# def siapa (hero):
#   print("Namaku adalah " + name)

# hero1 = hero('sniper',100)
# hero2 = hero('mario bros',90)

# print(hero1.siapa())


