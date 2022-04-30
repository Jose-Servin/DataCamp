# All about OOP

## What is OOP?
OOP is a principle in which code is seen as interactions of objects. OOP is great for building frameworks and tools. 
A fundamental concept of OOP is the representation of objects as data structures. An object is a data structure 
incorporating information about state and behavior:
```text
Object = state + behavior
```

* <mark> Encapsulation </mark>: bundling data with code operating on it. 
* <mark> Inheritance  </mark>: extending functionally of existing code
* <mark> Polymorphism </mark> : creating a unified interface 


In OOP, classes are the blueprint for objects outlining possible states and behaviors. In Python everything is an 
Object which is a representation of a class. We can use the `type()` function to see the Class of an object. <br>

When we say "state and behavior" we mean "attributes and methods". If we dig deeper, attributes are the variables we 
define and methods are the functions uses on/with class objects. We can view all the attributes and methods an 
object has by using `dir(object)`.

## Class Anatomy: attributes and methods
Attributes are defined using `=` for example:
```python
class Customer:
    def set_name(self, new_name):
        self.name = new_name
    
    def identify(self):
        return f"My name is {self.name}"
```

## The `__init__` constructor
The main purpose of the constructor is to define the object attributes. This specific method runs as soon as a Class 
Object is created which means any attributes needed must be given UNLESS there are default values. It is best 
practice to create all object attributes in the constructor. <br>

In the constructor we don't always have to provide the attributes. We can also construct them using other functions 
for example, creating a `hire_date` attribute to be today:
```python
# Import datetime from datetime
from datetime import datetime

class Employee:
    
    def __init__(self, name, salary=0):
        self.name = name
        if salary > 0:
          self.salary = salary
        else:
          self.salary = 0
          print("Invalid salary!")
          
        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()
```


Best Practice:
* Initialize attributes in the constructor
* Classes should be CamelCase while function should follow lower_snake_case
* Keep self as self
* Use docstrings in both Classes and Methods

## Instance and Class Data
For our example, `instance data` are the attributes our class object has. For example, name and salary. This data is 
assigned via the `self` keyword. <br>

Class data is data shared among all instances of a class. In other words, these attributes do not change no matter 
the instance created. When defining a class attribute, it will become available as a `Global Variable` within the 
class. 
```python
class MyClass:
    CLASS_ATTR_NAME = attr_name
```
For our example this can be build with:
```python
# Import datetime from datetime
from datetime import datetime

class Employee:
    
    MIN_SALARY = 30000
    
    def __init__(self, name, salary=0):
        self.name = name
        if salary > Employee.MIN_SALARY:
          self.salary = salary
        else:
          self.salary = Employee.MIN_SALARY
          
        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()
```

### Why use class attributes?
* Global constants related to the class
* min and max values for attributes
* ex: pi 

### Class Methods
Class methods are methods for every instance however, a key difference here is that class methods CANNOT use 
instance level data. 
```python
class MyClass:
    @classmethod
    def my_awesome_class(cls, args):
        pass
```
To call this class method we use `MyClass.my_awesome_class(args...)`

The main use case for class methods is `Alternative Constructors`! 

Example: creating employee object from data stored in a file. 
```python
# Import datetime from datetime
from datetime import datetime

class Employee:
    
    MIN_SALARY = 30000
    
    def __init__(self, name, salary=0):
        self.name = name
        if salary > Employee.MIN_SALARY:
          self.salary = salary
        else:
          self.salary = Employee.MIN_SALARY
          
        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()

    # here we are using a class method to create objects
    @classmethod
    def from_file(cls, filename):
        with open(filename, 'r') as file:
            name = file.readlines()
        return cls(name) # here we return an object and cls will call the __init__() constructor
```
To create an employee without using the `class Employee()` we use `emp = Employee.from_file('data.txt')`. 

## Class Inheritance
Class inheritance is a way in which we can define `New Class functionality = Old class functionality + extra`. We 
can achieve this by:
```python

class MyChild(MyParent):
    pass
```

* `MyParent`: class whose functionality is being extended/inherited.
* `MyChild`: class that will inherit the functionality and add more.
* Child class will inherit all the Parent class attributes. 

Lastly, we can think of "inheritance" as "is a". "The savings account is a Bank account." We can check this with:
```python
isinstance(savings_acct, SavingsAccount)
isinstance(savings_acct, BankAccount)
```
SavingsAccount is a BankAccount BUT BankAccount IS NOT a SavingsAccount. 

## Customizing functionality via inheritance
