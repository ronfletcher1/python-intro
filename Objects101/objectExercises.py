#Exercise 1
#Given the following Person class:

# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone

#     def greet(self, other_person):
#         print 'Hello %s, I am %s!' % (other_person.name, self.name)
# # Write code to

# # Instantiate an instance object of Person with 
# # name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
# Sonny = Person ("Sonny", "sunny@hotmail.com", "483-485-4948")
# # Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
# Jordan = another_person('Jordan', 'jordan@aol.com', '495-586-3456')
# # Have sonny greet jordan using the greet method.
# Sonny.greet(Jordan)
# # Have jordan greet sonny using the greet method.
# Jordan.greet(Sonny)
# # Write a print statement to print the contact info (email and phone) of Sonny.
# print Sonny.email, Sonny.phone
# # Write another print statement to print the contact info of Jordan.
# print Jordan.email, Jordan.phone, Sonny.email, Sonny.phone

# Exercise 2
#Make your own class
# Create a class Vehicle. A Vehicle object will have 3 attributes:

# make
# model
# year
# A vehicle is created thus:

# car = Vehicle('Nissan', 'Leaf', 2015)
# And you can access it's attributes individually like so:

# class Vehicle(object):
#     def __init__(self, model, make, year, color):
#         self.model = model
#         self.make = make
#         self.year = year
#         self.color = color
#     def print_info(self):
#         print self.model,self.make,self.year, self.color
# car = Vehicle("Subaru", "Forrester", 2018, "Green")
# car2 = Vehicle("Subaru", "Forrester", 2018, "blue")
# # print car.make, car.model, car.year, car.color
# car.print_info()

# # Exercise 3
# # Add a method (function)
# # Add a print_info method to the Vehicle class. It will print out the vehicle's information like so:
# # def print_info(self): 
# #   print (self.model,self.make,self.year, self.color)
# # The method can only be called locally
# # >>> car.print_info()
# # 2015 Nissan Leaf
# # print_info = car
# # car.print_info(make, model, year, color)
# car.print_info()


# Exercise 4 Add a method 2
# Go back to the Person class. Add a print_contact_info 
# method to the Person class that will print out the contact 
# info for a object instance of Person. You will use it thus:
# >>> sonny.print_contact_info()
# Sonny's email: sonny@hotmail.com, Sonny's phone number: 483-485-4948

# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#     def print_contact_info(self):
#         print "My Name is: %s , %s\'s emal: %s , %s\'s phone number: %s" % (self.name, self.name, self.email, self.name, self.phone)
#     def greet(self, other_person):
#         print 'Hello %s, I am %s!' % (other_person.name, self.name)
# Sonny = Person ("Sonny", "sunny@hotmail.com", "483-485-4948")
# Jordan = another_person('Jordan', 'jordan@aol.com', '495-586-3456')
# Sonny.print_contact_info()

# Exercise 5
# Add an instance variable (attribute)
# Add a friends instance variable (attribute) to the Person class. 
# You will initialize it to an empty list within the constructor (__init__). 
# Once you've done this you should be able to add a friend to a person using 
# list's append method:

# jordan.friends.append(sonny)
# sonny.friends.append(jordan)
# You should also be able to get the number of friends a person has by 
# using the len function on his friends:

# >>> len(jordan.friends)
# 1
# class Person(object):
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = [] #empty list of friends
#     def print_contact_info(self):
#         print "My Name is: %s , %s\'s emal: %s , %s\'s phone number: %s" % (self.name, self.name, self.email, self.name, self.phone)
#     def greet(self, other_person):
#         print 'Hello %s, I am %s!' % (other_person.name, self.name)
#     def add_friend(self, friend):
#         self.friends.append(friend)
# Sonny = Person ("Sonny", "sunny@hotmail.com", "483-485-4948")
# Jordan = Person ('Jordan', 'jordan@aol.com', '495-586-3456')
# Sonny.print_contact_info()
# Jordan.friends.append(Sonny)
# Sonny.friends.append(Jordan)
# print len(Jordan.friends)

# Exercise 6
# Add a num_friends method Similarly, to get the number of friends 
# a person has, we'd like to hide the implementation detail that 
# there is a friends attribute which is a list. Implement a num_friends 
# method which returns the number of friends the person currently has:

# >>> jordan.num_friends()
# 1

class Person(object):    
    def __init__(self, name, email, phone):  #this is a constructor (only initial init)
        self.name = name # object attribute
        self.email = email # object attribute
        self.phone = phone # object attribute
        self.friends = [] # object attribute
    def __repr__(self):

    def print_contact_info(self): #methods are functions within classes
        print "My Name is: %s , %s\'s emal: %s , %s\'s phone number: %s" % (self.name, self.name, self.email, self.name, self.phone)
    def greet(self, other_person): #methods are functions within classes
        print 'Hello %s, I am %s!' % (other_person.name, self.name)
    def add_friend(self, friend): #methods are functions within classes
        self.friends.append(friend)
    def num_friend(self, friend):
        print len(self.friends)
Sonny = Person ("Sonny", "sunny@hotmail.com", "483-485-4948")
Jordan = Person ('Jordan', 'jordan@aol.com', '495-586-3456')
Sonny.print_contact_info()
Jordan.friends.append(Sonny)
Sonny.friends.append(Jordan)
print len(Jordan.friends)
print Sonny.friends[]
# 3 abstact data types
# # dictionary:  sonny['name']
# diction = {
#     "key": "value"
#     "name": "joe"
#     "phone": "222"
# }
# # lists:  sonny[0]
# alist = [
#     "value"
#     "joe"
#     "222"
# ]
# # object: sonny.name
# we define with the class keyword
# and then we Instantiate an object by calling the class.
# classes have constructor functions (__init__), it's run
# on creation, and sets self variables
# objects use . notation
# the really big difference between classes and dictionary:
# 1. classes have a schema
# 2. classes have methods


# Exercise 7
# Count number of greetings
# We want to count the number of times a person has greeted someone. To do this, we'll add another attribute, call it say greeting_count, and initialize it to 0. Then each time the greet method is called, we'll increment greeting_count by 1.

# >>> sonny.greeting_count
# 0
# >>> sonny.greet(jordan)
# >>> sonny.greeting_count
# 1
# >>> sonny.greet(jordan)
# >>> sonny.greeting_count
# 2


# # Rob's Code'
# class Person(object):
#     def __init__(self, name, email, phone): # this is a constructor
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = [] #empty list of friends :(
#         self.greeting_count = 0

#     def greet(self, other_person):
#         self.greeting_count += 1
#         print 'Hello %s, I am %s!' % (other_person.name, self.name)
#     def print_contact_info(self):
#         print '%s\'s email: %s, %s\'s phone: %s' % (self.name, self.email, self.name, self.phone)
#     def add_friend(self,friend):
#         self.friends.append(friend)
#     def num_friends(self):
#         return len(self.friends)

# # Instantiate an instance object of Person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', store it in the variable sonny.
# sonny = Person('Sonny','sonny@hotmail.com','483-485-4948')
# # Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', and phone of '495-586-3456', store it in the variable 'jordan'.
# jordan = Person('Jordan','jordan@aol.com','495-586-3456')
# # Have sonny greet jordan using the greet method.
# sonny.greet(jordan)
# # Have jordan greet sonny using the greet method.
# jordan.greet(sonny)
# # Write a print statement to print the contact info (email and phone) of Sonny.
# print sonny.email, sonny.phone
# # sonny.print_info()
# # Write another print statement to print the contact info of Jordan.
# sonny.print_contact_info()
# jordan.print_contact_info()

# sonny.friends.append(jordan)
# sonny.friends.append(jordan)
# sonny.friends.append(sonny)
# sonny.add_friend(sonny)

# sonnysNumFriends = sonny.num_friends()
# print sonny.num_friends()
# print sonny.num_friends
# sonny.num_friends()
# print len(sonny.friends)

# # primitives: integer, float, string, boolean
# # 3 abstract data types:
# # dictionary: diction['key']
# diction = {
#     "key":"value",
#     "name":"joe",
#     "phone":"222"
# }
# # list: aList[0]
# aList = [
#     "value",
#     "joe",
#     "222"
# ]
# # object: sonny.name
# # we define with the class keyword
# # and then we Instantiate an object by calling the class
# # classes have constructor functions (__init__), it's run
# # on creation, and sets self variables
# # objects use . notation
# # the really big differeces between classes and dictionary:
# # 1. classes have a schema
# # 2. classes have methods


# class Vehicle(object):
#     # python will call this one when its supposed
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def print_info(self):
#         print self.year, self.make, self.model
#     def __repr__(self):
#         return "The make is: %s, the model is: %s %s" % (self.make,self.model,self.year)


# car = Vehicle('Nissan', 'Leaf', 2015)
# car2 = Vehicle('Ford', 'Focus', 2015)
# # print car.make, car.model, car.year
# car.print_info()
# car2.print_info()

# print car