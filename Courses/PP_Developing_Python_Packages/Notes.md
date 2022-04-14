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
