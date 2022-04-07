# Software Engineering Concepts

### 1. Modularity
* Improves readability 
* Improves maintainability 
* Solve problems only once 

<p> To write modular code in python we can leverage packages, classes and methods. </p>

### 2. Documentation
* Shows users how to use your project
* Prevents confusion from your collaborators 
* Prevents frustration from future you 

### 3. Testing
* Save time over manual testing 
* Find and Fix more bugs 
* Run tests anytime/anywhere 

### 4. Version Control & Git 

## Introduction to Packages and Documentation 
Basic package installation comes from `pip`; where package and package dependencies are installed.
We can read documentation with the use of the `help()` function. 

## Conventions and PEP 8 

<mark> PEP 8</mark> is a document that provides guidelines and best practices on how to write Python code. PEP 8 
lets us know how to format our code to be as readable as possible. In basic format, PEP 8 calls for the correct use 
of whitespace and comments in order to provide a visual aid for the codes process. 

### PEP 8 Tools
Most IDE's provide warning labels, so you can reformat your code to follow PEP 8 conventions. Another option is the 
`pycodestyle` package which is a tool to check your python code against some style conventions in PEP 8. 

## Writing your first Python Package
A minimal python package consists of two elements:
1. A directory: name of package 
2. A python file: `__init__.py` 

The directory represents the name of the python package, therefore it should convey the functionality of the 
package and be named as such. The file must be named `__init__.py`. This file lets python know the directory we 
created is a package. 

## Adding Functionality to Packages 
Recreated package example using the following directory structure:
```
└── working_directory
    ├── my_package
    │   ├── __init__.py
    │   └── utils.py
    └── my_script.py
```
To use the functions in our `utils.py` file we `import my_package.utils as utils` and then call the function 
using `message = utils.secret_message(clearance=False)`. 
```python
import my_package.utils as utils

message = utils.secret_message(clearance=False)
```
We can also import functionality using the `__init.py` 
file by placing `from .utils import secret_message` inside the `__init__.py` file.
```python
from .utils import secret_message
``` 
Note the relative import statement used. Now, in our run file we can simply use `import my_package`.
```python
import my_package
message = my_package.secret_message(clearance=False)
```
We do this to make our `utils.py` functions more easily accessible by the user. Ultimately this saves typing. As a 
keynote, the `__init__.py` file should contain relative imports of key functionalities to make them easily 
accessible to the user. 

## Making your packages portable
The two main steps to sharing a python package are creating `setup.py` and `requirements.txt`. The two files provide 
information over how to install our package and recreate it's required environment. These two files should be 
located on the same level as the package directory. <br>

The `requirements.txt` file shows how to recreate the environment needed for our package. This includes any python 
packages needed and their version. 
```text
# needed packages/versions
matplotlib
numpy==1.15.4
pycodestyle >= 2.4.0
```
We can then add a note that states "to ensure you have the required packages please performa a..." 
`pip3 install -r /path/to/requirements.txt`. <br>

`setup.py` is what tells pip how to install our actual package. Additionally, the info will be used my PyPi if we 
decide to publish. 
```python
from setuptools import setup

setup(name='my_package',
      version='0.0.1',
      description='An example package from DataCamp',
      author='Jose Servin',
      author_email='servin@noemail.com',
      packages=['my_package'], # lists location of all __init__.py files in our package 
      install_requires=['matplotlib', 'numpy==1.15.4', 'pycodestyle>=2.4.0']
      )
```
Lastly we can install our package with pip if we are in the same directory as our package. This installs the package 
at an environment level. 
```shell
pip3 install .
```
