# Objects and Classes
# Basics
# Given the following Person class:

class Person(object):
    def __init__(self, name, email, phone, saying):
        self.name = name
        self.email = email
        self.phone = phone
        self.saying = saying

    def greet(self, other_person):
        print "Whats UUUUP!! %s, I'm %s, %s" % (other_person.name, self.name, self.saying)
# Write code to

# Instantiate an instance object of Person with 
# name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948', 
# store it in the variable sonny.
Sonny = Person('Sonny','sonny@hotmail.com', '483-485-4948', "let's get this party started")
# Instantiate another person with the name of 'Jordan', email of 'jordan@aol.com', 
# and phone of '495-586-3456', store it in the variable 'jordan'.
jordan = Person('Jor','jordan@aol.com', '495-586-3456', "I'm all in")
print Sonny.name, Sonny.email, jordan.name, jordan.phone

# Have sonny greet jordan using the greet method.
Sonny.greet(jordan)
# Have jordan greet sonny using the greet method.
jordan.greet(Sonny)
# Write a print statement to print the contact info (email and phone) of Sonny.
# Write another print statement to print the contact info of Jordan.







