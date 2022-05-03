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
We can customize functionality from Parent classes by using the `Parent.Method` syntax to call the function and 
apply any changes needed. For example:
```python
class CheckingAccount(BankAccount):
    def __init__(self, balance, limit):
        BankAccount.__init__(self, balance)
        self.limit = limit

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount, fee=0):
        if fee <= self.limit:
            # here we use the Parent class function since this functionality already exists
            BankAccount.withdraw(self, amount - fee)
        else:
            BankAccount.withdraw(self, amount - self.limit)
```
Here we call the `BankAccount.withdraw` method in the child `CheckingAccount` class in order to change the methods 
functionality and implementation. We do this to avoid having to create another method or action that does the same 
thing. 

## Operator Overloading: Comparison
When checking object equality in OOP, there are several steps we must take in order to ensure we are correctly 
comparing object. For example, if we create two account with the same balance and for this exercise assume they 
belong to the same person then they must be equal. However, when we compare them we get `False`. 
```python
from BankAccount_OOP import BankAccount, SavingsAccount, CheckingAccount

acct_1 = BankAccount(2000)
acct_2 = BankAccount(2000)

print(acct_1)
print(acct_2)
print(acct_1 == acct_2)
```
```text
<BankAccount_OOP.BankAccount object at 0x7f7aee4e95e0>
<BankAccount_OOP.BankAccount object at 0x7f7af1d69fa0>
False
```
This is because the two separate class instances are stored in a different memory allocations. Essentailly, what we 
are saying is "allocate a chunk of memory for acct_1 and another for acct_2." So, when we compare the two calss 
instances we are truly comparing references not the data. 

### Overloading `__eq__()`
This method is called when 2 objects of a class are compared using `==`. We first add it to the class:
```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def __eq__(self, other):
        print("__eq__() is called ")

        return self.balance == other.balance
```
```text
<BankAccount_OOP.BankAccount object at 0x7fe3f3adc5e0>
<BankAccount_OOP.BankAccount object at 0x7fe3f757a8e0>
__eq__() is called 
True
```
This gives us a `True` boolean when comparing the two accounts since this only attributes we are comparing is the 
account balance. Python always calls the child's `__eq__()` method when comparing a child object to a parent object.

The other comparison operators that exists are:
* `__equ__()` for `==`
* `__ne__()` for `!=`
* `__ge__()` for `>=`
* `__le__()` for `<=`
* `__gt__()` for `>`
* `__lt__()` for `<`

## Operator Overloading: String representation
There are two string representation's we can overload:
1. `__str__()`: represents what will be shows when we `print()` and/or use `str()`. 
   1. informal, for end user
   2. string representation
2. `__repr__()`: represents what will be shown with `repr()` and when we don't use print
   1. formal, for developer
   2. reproducible representation
   3. fallback for `print()` when `__str__()` is not defined
   4. The point of `__repr__()` is to give the exact call to create the object

```python
class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        self.balance -= amount

    def __eq__(self, other):
        print("__eq__() is called ")

        return self.balance == other.balance

    def __repr__(self):
        account_string = f"BankAccount(20000)"
        return account_string
```
```text
BankAccount(20000)
BankAccount(20000)
__eq__() is called 
True
```
## Exceptions
The main purpose of exception handling is to prevent the program from termination when an exception is raised. We do 
this by using a `try - except - finally` block. <br>

We can also raise exceptions using `raise` followed by `error_name('error message')`. For example:
```python
def make_list(length):
    if length <= 0:
        raise ValueError('Invalid Length!')
    return [1]*length
```
### Custom Expecption
Custom exceptions can be created in OOP format by inheriting from the Exception class.
```python
class BalanceError(Exception):
    pass

class Customer:
    def __init__(self, name, balance):
       # here we are using a condition to check the given parameter before attributing it to the class instance. 
        if balance < 0: 
            raise BalanceError('Balance has to be non-negative')
        else:
            self.name, self.balance = name, balance 
```

It is best practice including custom exceptions in OOP projects because this guarantees the object does not get 
created. In other words, the exception interrupts the constructor. The user can bypass our custom try-except blocks 
by using their own:
```python
try:
    instance = Create_Object(param1, param2)
except BalaneError:
    instance = Create_Object(param1, param2)
```

## Designing for Inheritance and Polymorphism

