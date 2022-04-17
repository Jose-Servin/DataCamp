# Why build packages?
* Allows our code to be easier to reuse. 
* To avoid lots of copying and pasting.
* To keep our functions up to date.
* To collaborate and give our code to others. 

# Understanding scripts, modules and packages
* Script: a python file 
* Package: A directory full of python code to be imported.
  * `mysimplepackage`
* Subpackage: a smaller package inside a package.
* Module: A python file inside a package which stores the package code.
  * `simplemodule.py`
* Library: Either a package or a collection of packages. 
* `__init__.py` marks the directory as a Python package. 


# Documentation
Documentation should be included because it will help users use your code.

## What to document?
* Functions
```python
def count_words(filepath, words_list):
    """Count the total number of times these words appear. """
```
The first sentence in your documentation should read like a summary. "Tell the function what to do."
* Class
* Class methods

## Documentation templates and style translation
Style translation can be achieved using `pyment` which is a python package used to generate docstrings. An important 
note about `pyment` is it must be run from the terminal. 
```shell
pyment -w -o numpydoc textanalysis.py
```
* The `-w` overwrites the file
* `-o numpydoc` outputs in NumPy style

This command produces these results:
```python
def count_words(filepath, words_list):
    """
    Count the total number of times these words appear.

    The count is performed on a text file at a given location

    Parameters
    ----------
    filepath : str
        Path to text file
        
    words_list : list of str
        Count the total number of appearances of these words.

    Returns
    -------

    """
    # Open the text file
    with open(filepath) as file:
        text = file.read()
    # Count number of times these words appear
    n = 0
    for word in text.split():
        if word.lower() in words_list:
            n += 1
    return n

```
### Types of documentation
Package documentation is placed in a string at the top of the package's `__init__.py` file. 
```python
"""
mysimplepackage is a complete package for counting the number of given words in a text file.

"""
```
Subpackage documentation is placed similarly inside the `__init__.py` file of the subpackage. 
Module documentation is written at the top of the module file. 
```python
"""
A module for counting certain words in a text file. 
"""
```

# Structuring Imports
In order to make your packages aware of any sub-packages and or modules, we use internal imports to import the 
modules into the subpackage and subpackages into the package. 

1. In our packages `__init__.py` file we import any sub-packages using absolute or relative imports. 
* Absolute import 
```python
from mysklearn import preprocessing
```
* Relative import
```python
from . import preprocessing
```
The `.` means the current file's parent directory. "From the current directory import preprocessing"

2. In our sub-package `__init__.py` file we import any package module. 
```python
from mysklearn.preprocessing import normalize
from . import normalize
```
Now, when we import the package `mysklearn` we can access all the functions in this module. <br>

`mysklearn.preprocessing.normalize.normalize_data` is the import statement to use the `normalize_data` function BUT 
we can improve this to have better readability for the user. 

## Improving readability by importing functions into subpackages
To decrease the length of the import statement we can directly import the useful functions into the `__init__.py` 
file. <br>

Working in the `mysklearn/preprocessing/__init__.py` we can use either absolute imports `from mysklearn.preprocessing.normalize import normalize_data` to import the `normalize_data` function OR we can use a relative 
import `from .normalize import normalize_data `. <br>

This allows us to `import mysklearn` and to use the `normalize_data` function we use a shorter path 
`mysklearn.preprocessing.normalize_data`.
## Importing between sibling modules
Current structure is as follows:
```text
mysklearn/
    -__init__.py
    _preprocessing
        -__init__.py
        -normalize.py
        -funcs.py    
    -utils.py 
```
The `funcs.py` file contains functions that are used in the `normalize.py` file, so we need to import them. These 
two files are siblings. 
* Absolute Import Statement
```text
from sklearn.preprocessing.funcs import (min, max)
```
* Relative import statement
```text
from .func import min, max 
```
## Importing between modules far apart
Now, let's say in `utils.py` we have a custom exception called `MyException`. To use this custom exception in 
`normalize.py` or `funcs.py` we use the following import statement: 
* Absolute Import 
```text
from mysklearn.utils import MyException
```
* Relative Import <br>
Two `..` are needed because we need to move outside the sub-package and reference at the same level as 
  the `preprocessing`
  package. Starting from the `normalize.py` module, it's parent is `preprocessing` package, and it's parent is 
  `mysklearn`. Then from the `utils` file in this directory (`mysklearn`) we import the custom exception. 
```text
from ..utils import MyException
```

## Relative import cheat sheet
* `from . import module`
  * From current directory import module
* `from .. import module`
  * from one directory up, import module
* `from .module import function`
  * from module in current directory, import function
* `from ..subpackage.module import function`
  * from subpackage one directory up, from module in that subpackage, import function

# Installing your own packages
One main reason you should install your own package has to do with your working directory structure. 
```text
project_folder
    - mysimplepackage
        -__init__.py
        -simplemodule.py
   - run.py
```
With this structure the `run.py` script and the `mysimplepackage` package directory are in the same folder. In other 
words, they are both children of the `PP-_Developing_Python_Packages` folder. <br>

However, if you move your script and package apart you will no longer be able to import your package. This is 
because the scripts searched for packages in its parent directory but won't search outside that. <br>

This is why we need to install our package. 
```text
project_folder
    -mypackages
        -mysimplepackage
            -__init__.py
            - simplemodule.py
    - myscripts
        - run.py
```
## How to make a package installable
To make a package installable, you must set up a `setup.py` script.
* is used to install the package
* contains metadata on the package

By convention, the `setup.py` file is placed outside the source code for the package. For our example, the outer 
directory is called `PP_Developing_Python_Packages`.  <br>

Notes on `setup` version number: The version number has three parts to it. (major number).(minor number).(patch number)
* patch number is increased for bug fixes and improvement to functions that already exists. 
* minor number is increased for new features
* major number is increased for huge changes

Our final `setup.py` file contains the following:
```python
from setuptools import setup, find_packages

# find_packages is used to find the paths of your packages and subpackages

setup(

    author='Jose Servin',
    description='A complete package to count number of word occurrences in a txt file.',
    name='mysimplepackage',
    version='0.1.0',  # version number (major number).(minor number).(patch)
    packages=find_packages(include=['mysimplepackage', 'mysimplepackage.*'])
)
```
## Editable Installation
In order to `pip` install your package, navigate to the directory containing the `setup.py` file and use
`pip3 install -e .` The `.` means install the package in the current directory and `-e` means install in an editable 
mode so any changes or bug fixes to the package source code are also included when you import the package. 

# Dealing with dependencies
Dependencies are other packages imported inside your package. 

## Adding dependencies to setup.py
```python
from setuptools import setup, find_packages

# find_packages is used to find the paths of your packages and subpackages

setup(

    author='Jose Servin',
    description='A complete package to count number of word occurrences in a txt file.',
    name='mysimplepackage',
    version='0.1.0',  # version number (major number).(minor number).(patch)
    packages=find_packages(include=['mysimplepackage', 'mysimplepackage.*']),
    install_requires=['numpy', 'pandas']
)
```
## Controlling dependency versions
The goal is to allow as many package versions as possible.
```python
from setuptools import setup, find_packages

# find_packages is used to find the paths of your packages and subpackages

setup(

    author='Jose Servin',
    description='A complete package to count number of word occurrences in a txt file.',
    name='mysimplepackage',
    version='0.1.0',  # version number (major number).(minor number).(patch)
    packages=find_packages(include=['mysimplepackage', 'mysimplepackage.*']),
    install_requires=[
      'pandas>=1.0', # this version or later
      'scipy==1.0', # exact version
      'matplotlib>=2.2.1,<3' # at least but not after 
    ]
)
```
## Python versions
```python
from setuptools import setup, find_packages

# find_packages is used to find the paths of your packages and subpackages

setup(

    author='Jose Servin',
    description='A complete package to count number of word occurrences in a txt file.',
    name='mysimplepackage',
    version='0.1.0',  # version number (major number).(minor number).(patch)
    packages=find_packages(include=['mysimplepackage', 'mysimplepackage.*']),
    install_requires=[
      'pandas>=1.0', # this version or later
      'scipy==1.0', # exact version
      'matplotlib>=2.2.1,<3' # at least but not after 
    ],
  python_requires = '>=2.7, !=3.0.*, !3.1.*' #excluding versions must be done with *
)
```
## Making an environment for developers
1. run `pip freeze > requirements.txt` in the terminal in the current project folder level.
2. Install requirements using `pip3 install -r requirements.txt`
```text
project_folder
    - mysimplepackage
        -__init__.py
        -simplemodule.py
   - run.py
   - setup.py
   - requirements.txt
```
# Including licenses and writing README's

## Why do I need a license?
* to give others permission to use your code
* gives permission to modify your code
* gives permission to distribute versions of your package

## What is a README file?
A `README` file acts like a front-page for your package. <br>

A good `README` includes:
* Title
* Description and Features
* Installation
* Usage examples
* Contributing
* License

## What is a MANIFEST.in file?
List all the extra files to include in your package distribution. 
```text
include LICENSE.txt
include README.md
```

So our final Python Package environment looks like this: 
```text
project_folder
    - mysimplepackage
        -__init__.py
        -simplemodule.py
   - run.py
   - setup.py
   - requirements.txt
   - LICENSE.txt
   - README.md
   - MANIFEST.in
```

# Publishing your package
When uploading your package to PyPi, you are actually upload a package distribution which is a bundle version of 
your package which is ready to be installed. <br>

There are two types of distributions in Python:
1. Source distribution - a distribution package which is mostly your source code. 
   1. Installed via `setup` script
2. Wheel distributions - a distribution package which has been processed to make it faste to install.
   1. Faster for user to install due to it being smaller size. 
   2. Preferred Python distribution

When uploading packages to PyPi, it's good practice uploading both the source distribution and wheel distribution. 

## How to build distributions
Navigate to project folder in the terminal and run `python3 setup.py sdist bdist_wheel`. This will create a `dist` 
directory and add wheel and source distributions inside. It will also include `build` and `egg-info` but these can 
be ignored.

## Upload your package
There are two options when it comes to uploading. First step is to set up accounts, next navigate to project folder in 
the terminal and run one of the commands. 

1. Upload to PyPi 
   1. `twine upload dist/*`
2. Upload to TestPyPi
   1. `twine upload -r testpypi dist/*`

# Testing your packages
Testing should be done in order to increase code coverage. The fundamental blocks of testing are asserting that the 
code returns a value or performs the action you coded. Tests should be kept in their own directory and should be 
children of the main project folder. In other words, test folder should be siblings with the package. 
```text
PP_Developing_Python_Packages
├── Notes.md
├── mysimplepackage
│   ├── __init__.py
│   └── simplemodule.py
├── run.py
├── setup.py
└── tests
```
## How to structure a test module
First, we set up a `__init__.py` file in our test directory and for each module in our package we set up 
`test_<module_name>.py` file. In these files, we import each method that is in that `<module_name>` and test. <br>

Example, our `simplemodule.py` file has one function called `count_words` so, we go into our `test_simplemodule.py` 
file and set up the following file. Note, we use an absolute import statement.  
```python
from mysimplepackage.simplemodule import count_words


def test_count_words():
    assert count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words']) == 6

```
To run our test, we go into the terminal, navigate to the project folder (top of the directory) and run `pytest`. 

<mark> <strong> IMPORTANT NOTE: </strong> </mark> <Br>

You must `Sources Root` your project folder in PyCharm in order to 
use your package modules in your `tests` directory. 

## Understanding Pytest output
Pytest will look inside the test directory and run any `.py` files that being with "test." 
* looks for modules that begin with "test"
* looks for functions that being with "test"

<img  src="images/Screen Shot 2022-04-16 at 2.10.09 PM.png" alt="Pytest output from DataCamp course"/> 

# Testing your package with different environments
If we wanted to test our packages using different versions of Python, we would have to download each version plus 
our packages and dependencies and run pytest. <br>

A better alternative is `tox`. What is tox?
* designed to run tests with multiple versions of python. 


Tox runs from the terminal, but before you run it you must create a configuration file called `tox.ini` located at 
the top of your directory. This file tells tox what to run in each environment and which Python version to use. 

## What to include in the tox.ini file?

1. First we create the tox heading 
```text
[tox]
```
2. Specify which versions of Python we want to test by defining the `envlist` parameter. 
    1. <mark> These version must already be installed in your computer </mark>
```text
envlist = py27, py35, py36, py37
```

3. define `[testenv]` heading and tell tox what you want it to do once it installs your dependencies by using the 
   `commands` parameter. Here you list the terminal commands tox will run.
   1. You must first define any tox dependencies using the `deps` parameter. Basically, this is what tox needs in 
      order to test which will most likely be pytest. 
   2. more commands can be added besides just "pytest" but they must be shell commands. 
```text
[testenv]
deps = pytest 
commands =
    pytest
```
## How to run tox
Navigate to the top of the directory and run the `tox` command. <br>

The `tox` output will look like this: <br>

- First it confirms python version x environment was created and installed the package and it's dependencies. 


<img src="images/Screen Shot 2022-04-16 at 2.41.42 PM.png" alt='tox output sc from DataCamp' />

- Next it runs the `commands` defined and repeats for each version in the `envlist` parameter. 

<img src="images/Screen Shot 2022-04-16 at 2.45.11 PM.png" alt="tox output">

- Finally, it shows us a summary of each `envlist` run. 

<img src="images/Screen Shot 2022-04-16 at 2.47.43 PM.png" alt="tox output">

# Keeping your package stylish
The same way `pytest` is used to find bugs. `flake8` is used to find styling mistakes. Normally, these are 
under-lined by PyCharm but some can still go un-noticed. <br>

First, we install `flake8` using `pip3 install flake8`. Flake8 is a static code checker that does not run your code. 
In our terminal we run `python3 -m pip install flake8` and run the following command: 
```shell
flake8 simplemodule.py
```
Output:
```text
Last login: Sat Apr 16 15:24:39 on ttys001
joseservin@Joses-MBP ~ % flake8 /Users/joseservin/DataCamp/Courses/PP_Developing_Python_Packages/mysimplepackage/simplemodule.py
/Users/joseservin/DataCamp/Courses/PP_Developing_Python_Packages/mysimplepackage/simplemodule.py:4:1: F401 'numpy as np' imported but unused
/Users/joseservin/DataCamp/Courses/PP_Developing_Python_Packages/mysimplepackage/simplemodule.py:5:1: F401 'pandas as pd' imported but unused
joseservin@Joses-MBP ~ % 
```
## Bending the rules of flake8
We set up a `.py` file called `formatting_vars.py` where we commit a flake8 violation (E222). 
```python
var_1 =     6 ** 4 + 1
var_3 = 10 ** 4 + 1
```
Running `flake8 <path to file> `:
```text
/formatting_vars.py:1:8: E222 multiple spaces after operator
```
We can place a `#noqa` after this line which stands for "no quality assurance". 
```python
var_1 =     6 ** 4 + 1 #noqa
var_3 = 10 ** 4 + 1
```
We can also place a `# noqa: E222` to specify specific flake8 violations.
```python
var_1 =     6 ** 4 + 1;  #noqa: E222
var_3 = 10 ** 4 + 1
```
which returns: 
```text
/formatting_vars.py:1:23: E703 statement ends with a semicolon
```
## Flake8 flags

A better alternative is to use flake8 flags in the terminal command.  <br>

* To ignore a violation use the `--ignore` flag: 

```python
var_1 =     6 ** 4 + 1
var_3 = 10 ** 4 + 1
```
So, for the instance where there are multiple spaces after the operator we can use `flake8 --ignore E222 <path to file>`

* To only see certain violations use the `--select` flag:
```python
var_1 =     6 ** 4 + 1
var_3 = 10 ** 4 + 1;
```
First we see all violations:
```text
/Users/joseservin/DataCamp/Courses/PP_Developing_Python_Packages/mysimplepackage/formatting_vars.py:1:8: E222 multiple spaces after operator
/Users/joseservin/DataCamp/Courses/PP_Developing_Python_Packages/mysimplepackage/formatting_vars.py:2:20: E703 statement ends with a semicolon
```
Now we are only interested in E703 violations:
```text
flake8 --select E703 <path to file>
```
```text
/formatting_vars.py:2:20: E703 statement ends with a semicolon
```
## Creating a setup.cfg file
We can store the setting for flake8 by setting up a `setup.cfg` file at the top of your directory. Here, any 
`ignore` violations defined will be ignored in all modules. 
```text
[flake8]

ignore = E222
exclude = setup.py

per-file-ignores = 
    <path to file>: <violation code> 
```
Now, you run `flake8 <path to top of directory>`. 

# Package development with templates 
Package developments contains lots of files which can become confusing. In order to make this developement faster, 
we can use `cookiecutter` and streamline the package/file creation process. <br>

In your terminal run `cookiecutter https://github.com/audreyr/cookiecutter-pypackage` and fill in the information. <br>
Note that some info is not needed so refer back to DataCamp's course 
[video](https://campus.datacamp.com/courses/developing-python-packages/rapid-package-development?ex=1).

# Version numbers and history

* `CONTRIBUTING.md` 
  * Invites other developers to work on your package
  * Tells them how to get started; by convention this is your contact info, so they can get in touch with you
* `HISTORY.md`
  * also knows as "history, changelog or release notes"
  * tells users what has changed between versions 

```markdown
# History

## 0.3.0
### Changed
- some function was changed
### Deprecated 
- support for 0.2.7 has ended 
- module.function has been removed
### Fixed
- fixed bug causing error
### Added 
- function name now available 

## 0.2.7

```

## Version Numbers
You should increase version number when your package is ready for a new release. <br>

The two places the version number need to be updated at is:
1. `setup.py` file 
2. package `__init__.py` file 
   1. `__version__ = 0.1.0` is added at the top of the `__init__.py` file after the comment section

<img src="images/Screen Shot 2022-04-17 at 4.25.11 PM.png" alt="version number updates">

A tool to help increase versions is the `bumpversion` tool from Python. This command runs at the top of your package 
directory. All you have to do is specify if it's `major`, `minor` or `patch`. 
```text
pip install --upgrade bumpversion
```

# Makefiles and Classifiers 

## Classifiers
Inside the `setup.py` file `cookiecutter` sets up classifiers which is a list of categories for each release of your 
package. Users on PyPi can filter based on classifiers and find packages. <br>

<img src="images/Screen Shot 2022-04-17 at 4.38.22 PM.png" alt="classifiers image">

## Makefile
This is where all the terminal commands are kept. <br>

To run a `makefile` command you use `make <function name>` in the terminal. To see all the commands in the makefile 
you use the `make help` command.  

<img src="images/Screen Shot 2022-04-17 at 4.40.41 PM.png" alt="makefile content">

