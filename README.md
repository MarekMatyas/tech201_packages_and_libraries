# tech201_packages_and_libraries


# Packages, modules and libraries

### 1. Libraries

Libraries are a chunk of code that you want to re-use (mostly methods and functions).
A library is a set of related **modules or packages bundled together**.

Let's look at a quick example: 

``` python
from random import random
```
This imports library called random and the way we can test it is as follows:

``` 
print(random())
```

This prints out random float numbers.

We can also import another library called `math`:
```
import math
```
And use this library creating a variable called `num_float` and using following print statements:
``` python
num_float = 23.66
print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
```
1. print statement rounds up the `num_float`
2. print statement rounds down the `num_float`
3. print statement shows us the value of pi

---
### 2.Modules

Modules is a piece of software that delivers some sort of functionality.
Module is a collection of code or functions that uses the `.py` extension allowing you to use that **code/function** in your program.

When you are building a program, it's really important to think whether you need to make a class/object or simply a function. you may not even need to make a function yourself, if there is a module that does what you are looking for already.

---
***The difference between modules and libraries***:

**Modules** are smaller, just the code that you can use.

**Libraries** are larger or more complex compilations of resources.

### Quick example:

We can `import` modules called `math`, `datetime`, `os`, and `sys`
``` python
import os
import math , datetime, sys
```
First we can test the `os` module by creating a variable called `working_directory`:

``` 
working_directory = os.getcwd()
print(working_directory)
```

This command shows us the current working directory (Where we are locally).

``` python
print(datetime.date.today())
print(sys.path)
```

1. The first print statement prints out today's date
2. Prints out shows the current path ( sys module, allows us to interact with files)

### The way we can use modules:

We need to create a couple functions:

Let's say we have created a file called `module` storing these functions

``` python
def return_user_id():
    print(os.getpid())

def return_user_name():
    print(os.uname())
```

Then in another file called `use_module`:

`from modules import *`

Notice we used `*` to specify we want to import everything. 

---

### Packages and `pip`

`pip` is Python's package manager and installer (for anything external we have to use `pip`).

To install `pip`, here are the steps:

First we check the version




