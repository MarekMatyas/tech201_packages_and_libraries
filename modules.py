# Modules is a piece of software that delivers some sort of functionality
# When you are building a program. it's really important to think whether you need to make a class/object or simply a function. you may not even  need to make a function yourself, if there is a module that does what you are looking for already



import os
import math , datetime, sys

working_directory = os.getcwd() # get current working directory ( this prints out where we are locally)

print(working_directory)

def return_user_id():
    print(os.getpid())

def return_user_name():
    print(os.uname())

print(datetime.date.today()) # This prints out todays date

print(sys.path) # Shows the current path ( sys module, allows us to interact with files)

print(math.remainder(1, 5)) #1.0


# Built-in functions

# print()
# len()
# type()


