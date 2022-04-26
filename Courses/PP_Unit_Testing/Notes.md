# All about Unit Testing

## The Life Cycle of a function
<img src="images/Screen Shot 2022-04-19 at 1.46.16 PM.png" alt="Life Cycle of a function">

## Real world testing environment 
* CI: continuous integration runs all unit tests when any code is pushed. If any tests fail, it will reject the 
  change to reduce downtime. 

<img src="images/Screen Shot 2022-04-19 at 6.03.09 PM.png" alt="how testing works in real-life development">

## Intro to Unit Testing
Unit tests automate the repetitive testing process and saves times. We can view the assert statements in a test 
module by using the command `!cat <path to test module>` in the terminal. 

## Unit Test Review

### Mastering assert statements
We can add a message which will only print when the assert statement raises an assertion error. This message should 
contain information as to why the assertion was raised.
```python
from mysimplepackage.simplemodule import count_words


def test_count_words():
    actual = count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words'])
    expected = 6
    message = f"""
        count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words']) returned {actual} instead of 
        {expected}.
    """
    assert actual is expected, message

```
### Float assert statements
When it comes to comparing floats, you cannot simply use an assertion statement because there are trailing digits at the 
end of floats that will cause the assertion statement to fail.  <br>

Instead, use the `pytest.approx()` function to wrap expected return value. If we have a function that adds floats 
like the following: 
```python
def add_floats(float_1, float_2):
    return float_1 + float_2
```
When we run `pytest` it will return:
```text
=================================== FAILURES ===================================
_______________________________ test_add_floats ________________________________

    def test_add_floats():
        actual = add_floats(0.1, 0.2)
        expected = 0.3
        message = f"""
            add_floats(0.1, 0.2) returns {actual} instead of {expected}
        """
    
>       assert actual == expected, message
E       AssertionError: 
E                 add_floats(0.1, 0.2) returns 0.30000000000000004 instead of 0.3 
E             
E       assert 0.30000000000000004 == 0.3


```
So we must use `pytest.approx()` to ignore the digits on the right:
```python
def test_add_floats():
    actual = add_floats(0.1, 0.2)
    expected = pytest.approx(0.3)
    message = f"""
        add_floats(0.1, 0.2) returns {actual} instead of {expected} 
    """
    
    assert actual == expected, message
```
Which gives us a passing test. 
```text
collected 2 items                                                              

DataCamp/Courses/PP_Developing_Python_Packages/tests/test_simplemodule.py . [ 50%]
.                                                                        [100%]

============================== 2 passed in 0.22s ===============================
```
## Testing for exceptions instead of return values
First we defined a simple function that returns the square root of a given argument. 
```python
def simple_sqrt(num):
    answer = math.sqrt(num)
    return answer
```
Next, we will test if `raise_value_error()` raises `ValueError` with negative arguments. 

<img src="images/Screen Shot 2022-04-22 at 2.28.24 PM.png" alt="raising errors">

If the function raises expected Error, it will be silenced by the context manager and the test will pass. If the 
function is buggy and does not raise a `ValueError` as expected, the test will fail. <br>

We can unit test details of the raised Exception as well. For example, we can check the `ValueError` that is raised 
contains the message "math domain error". To do this, we store the exception. 
```python
def test_valueerror_simple_sqrt():
    example_argument = -10
    with pytest.raises(ValueError) as exception_info:
        simple_sqrt(example_argument)
    # Check if ValueError contains the correct message
    assert exception_info.match("math domain error")
```
This results in a passed test case:
```text
collected 3 items                                                              

DataCamp/Courses/PP_Developing_Python_Packages/tests/test_simplemodule.py . [ 33%]
..                                                                       [100%]

============================== 3 passed in 0.33s ===============================
```

## The well tested Function
It can become quite noisy when a function contains lots and lots of tests. Instead, test for these type of arguments 
if present in the function usage:
1. Bad arguments
   1. When passed bad arguments, function raises an exception. 
2. Special arguments
   1. Boundary values
      1. 1 will be our Boundary value 
      2. -1 will also be a boundary value because 0 requires special logic. 
   2. Argument values, which are values for which the function uses special logic. 
      1. 0 will be our argument value that requires special logic. 
3. Normal arguments
   1. Recommended testing for two or three normal arguments. 

Once we have tested for these arguments types, our function can be considered well tested. 

## Test Driven Development (TDD)
More research needs to be done over this topic. 

## How to organize tests
<img src="images/Screen Shot 2022-04-23 at 10.59.43 AM.png" alt="test suite organization">

General Rules:
* For each `my_module.py` there should be a `test_my_module.py` file. 
* Test classes serve as a container for a single unit's test function. In other words, a test class is a container for 
all the tests of a specific function. 

Before implementing Test Classes our code looks like the following:
```python
import math
import pytest
from mysimplepackage.simplemodule import count_words, add_floats, simple_sqrt

def test_count_words():
    actual = count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words'])
    expected = 6
    message = f"""
        count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words']) returned {actual} instead of 
        {expected}.
    """
    assert actual is expected, message

def test_add_floats():
    actual = add_floats(0.1, 0.2)
    expected = pytest.approx(0.3)
    message = f"""
        add_floats(0.1, 0.2) returns {actual} instead of {expected} 
    """

    assert actual == expected, message
    # here we will add a test for the return value type
    assert isinstance(actual, float)
    # here we will add a test for the expected value
    assert expected == 0.3

def test_valueerror_simple_sqrt():
    example_argument = -10
    with pytest.raises(ValueError) as exception_info:
        simple_sqrt(example_argument)
    # Check if ValueError contains the correct message
    assert exception_info.match("math domain error")
```

After implementing Test Classes to better organize individual function tests our code looks like the following: 
```python
import math
import pytest
from mysimplepackage.simplemodule import count_words, add_floats, simple_sqrt


class TestCountWords(object):
    def test_correct_file(self):
        self.actual = count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words'])
        self.expected = 6
        self.message = f"""
                count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words']) returned {self.actual} instead of 
                {self.expected}.
            """
        assert self.actual is self.expected, self.message

```
## Mastering Test Execution 
Pytest makes it easy to run all test in the test folder. To do this, `cd` into the `tests` folder and run the 
`pytest` command. <br>

How does Pytest run the test?
1. Recurses into directory subtree of `tests/`
2. Finds all `.py` files starting with `test` (test module)
3. In these files, it finds all Classnames starting with `Test` (test class)
4. Runs all functions that start with `test_` (unit test)

When running the `pytest` command once inside the `tests` subdirectory, you can add the `pytest -x` flag which stops 
pytest running session after the first failure. And, to mention again, we can run a specific module by using the 
command `pytest <path to test module>` like we've always done before. 
### Running a particular test class
In order to run particular test class, we must introduce Node ID's. <br>
* Node ID of a test class: `<path to test module>`::`<test class name>`
* Node ID of a unit test: `<path to test moduel>`::`<test class name>`::`<unit test name>`

To use Node ID's in a pytest command use `pytest data/test_processing.py::TestRowInt`

### Running test using keyword expressions
To use a keyword expression with your pytest command use the `-k` flag followed by a text pattern. So if you only 
want to run the class named `TestSomeFunction` you will use the command `pytest -k "TestSomeFunction"` <br>

We can also use Python's logical operators when running test. For example, if we want to run all the test inside the 
test class `TestSomeFunctino` but not the unit test called `test_find_pattern` we can use the following command with 
pytest `pytest -k "TestSomeFunction and not test_find_patter"`. 

## Expected failures and conditional skipping 
Sometimes we want unit test to fail but do not want to give a false alarm. To flag a unit test as an expected fail 
we use the `xfail` mark to mark the test as "expected to fail." First we make the following changes to our 
`test_simplemodule.py` file:
```python
import math
import pytest
from mysimplepackage.simplemodule import count_words, add_floats, simple_sqrt


class TestCountWords(object):
    def test_correct_file(self):
        self.actual = count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words'])
        self.expected = 6
        self.message = f"""
                count_words('/Users/joseservin/Desktop/user_info.txt', ['key', 'words']) returned {self.actual} instead of 
                {self.expected}.
            """
        assert self.actual is self.expected, self.message

    # Add test that returns exception when word counts do not match

    # Add test that is expected to fail
    @pytest.mark.xfail(reason="testing an expected fail")
    def test_expected_failure(self):
        self.actual = None

        assert self.actual is not None
```
After adding this decorator and running `pytest` we get the following results back:
```text
collected 2 items                                                              

DataCamp/Courses/PP_Developing_Python_Packages/tests/test_simplemodule.py . [ 50%]
x                                                                        [100%]

========================= 1 passed, 1 xfailed in 0.28s =========================
```
We can also add a reason to the xfail test and view the reasons in the terminal pytest command using the `pytest -rx`
flag. 
```text
collected 3 items                                                              

DataCamp/Courses/PP_Developing_Python_Packages/tests/test_simplemodule.py . [ 33%]
xs                                                                       [100%]

=========================== short test summary info ============================
XFAIL DataCamp/Courses/PP_Developing_Python_Packages/tests/test_simplemodule.py::TestCountWords::test_expected_failure
  Testing an expected fail
=================== 1 passed, 1 skipped, 1 xfailed in 0.27s ====================
```

Sometimes we have expected failures due to certain conditions such as 
* code only works on certain Python versions 
* code does not work on Windows

To achieve this we use the `@pytest.mark.skipif(boolean_expression, reason)`. 
```python
# Hypothetically adding a function that only works with Python 2.7 or lower
    @pytest.mark.skipif(sys.version_info > (2, 7), reason="requires Python 2.7")
    def test_conditional_skip(self):
        """Only runs on Python 2.7 or lower"""
        self.actual = True

        assert self.actual
```
When we run these test we get:
```text
collected 3 items                                                              

DataCamp/Courses/PP_Developing_Python_Packages/tests/test_simplemodule.py . [ 33%]
xs                                                                       [100%]

=================== 1 passed, 1 skipped, 1 xfailed in 0.27s ====================
```
We can see the reason for these skips using the `pytest -rs` flag:
```text
collected 3 items                                                              

DataCamp/Courses/PP_Developing_Python_Packages/tests/test_simplemodule.py . [ 33%]
xs                                                                       [100%]

=========================== short test summary info ============================
SKIPPED [1] DataCamp/Courses/PP_Developing_Python_Packages/tests/test_simplemodule.py:27: requires Python 2.7
=================== 1 passed, 1 skipped, 1 xfailed in 0.27s ====================
```

To view both `xfail` and `skipif` reason message we use the `pytest -rsx` command. 

We are also able to appy these expected failures and conditional skipping to Test Classes as seen below:
<img src="images/Screen Shot 2022-04-23 at 6.23.43 PM.png" alt="skipping test classes">

## Continuous integration and code coverage 
###Build Status Badge: 
Uses a continuous integration server to run all tests automatically whenever we push a commit 
to GitHub. The badge itself shows whether tests are currently passing or failing. 

A common CI Servers is 
[Travis CI](https://www.travis-ci.com/?_gl=1%2A1x5ghqo%2A_ga%2AMjE0NDc0NjEwOS4xNjUwODIwODgw%2A_ga_XRYGSZFQ0P%2AMTY1MDgyMDg3OS4xLjAuMTY1MDgyMDg3OS42MA..)

To integrate with Travis CI we must follow these steps:
1. Create a configuration file at the same level as our `src` and `tests` subdirectories.

<img src="images/Screen Shot 2022-04-24 at 12.23.41 PM.png" alt="step 1 of CI integration">

2. Define the contents of your `.travis.yml` file with the following:

<img src="images/Screen Shot 2022-04-24 at 12.25.58 PM.png" alt="contents of travis ci config page">

3. Push file to GitHub
```text
git add .travis.yml
git push origin master
```
4. Go to GitHub, click on Marketplace and install `Travis CI` app. 
5. Allow the `Travis CI` app access to necessary repos and/or organizations. 
6. You will be redirected to Travis CI's login in page and be presented with a dashboard. 
7. From now on, whenever you push a commit to the GitHub repo, we should see a build appearing on the Travis CI 
   dashboard. 
8. Click on Badge, choose `markdown` and paste Markdown in the `README` file on GitHub. 

### Code Coverage Badge
The code coverage badge represents:
```text
(number of lines of code ran during testing /  total number of lines) * 100 
```
High percentages (75% or above) represent well tested code.
 <br>

The badge comes from a service called [Codecov](https://about.codecov.io/).

To install `Codecov` follow the following steps:
1. Modify the Travis CI configuration file

<img src="images/Screen Shot 2022-04-24 at 12.38.17 PM.png" alt="modified config file">

2.Install the Codecov app via GitHub Marketplace.

3. Each new commit will now show up as a code coverage report in Codecov. 

4. In Codecov page, go to Badge --> Settings and paste Markdown in the GitHub `README` file. 

## Beyond assertion: setup and teardown
There will be some functions that require more than simple `assert` statements. For example, image we have a 
function called `preprocess(raw_data_file_path, clean_data_file_path)`. This function introduces us to the two 
concepts of `Enviornment Precondition` and `Enviornment Modification`. 
* Environment Precondition is the presence of a raw data file in the environment in order for this function to run.
* Environment Modification is the new file created after the data is cleaned. 

With these type of functions, the new testing workflow is `setup --> assert --> teardown`. In Pytest, the setup and 
teardown is placed outside the test in a function called `fixture` which has the `@pytest.fixture` decorator. 

* Setup: Setup brings the environment to a state where testing can begin. 
* Teardown brings environment to initial state

Quick help: how to fix [PermissionError: Erron 13](https://itsmycode.com/python-permissionerror-errno-13-permission-denied/)

### preprocess() function
First let's take a look at the `preprocess()` function:
```python
def preprocess(raw_data_file_path, clean_data_file_path):
    """remove the last row of a csv file"""

    raw_data = pd.read_csv(raw_data_file_path, index_col=None)

    clean_data = remove_last_row(raw_data)

    clean_data.to_csv(clean_data_file_path, index=False)
```

This function takes a `raw_data_file_path` and `clean_data_file_path`. Inside the function, we call the 
`remove_last_row` function which is defined as:
```python
def remove_last_row(df):
    new_df = df.drop(df.tail(1).index)
    return new_df
```
This function removed the last row from a dataframe. <br>

Next, we want to test this function.

### my_fixture()
Our `fixture` function looks like this:
```python
@pytest.fixture
def raw_and_clean_data_file():

    #Setup process
    raw_data_path = '/Users/joseservin/DataCamp/Courses/PP_Developing_Python_Packages/raw_data.csv'
    clean_data_path = '/Users/joseservin/DataCamp/Courses/PP_Developing_Python_Packages/clean_data.csv'

    fieldnames = ['A', 'B', 'C']

    rows = [
        {
            'A':'Good',
            'B':'Good',
            'C':'Good'
        },
        {
            'A':'Good',
            'B':'Good',
            'C':'Good'
        },
        {
            'A': 'Good',
            'B': 'Good',
            'C': 'Good'
        },
        {
            'A': 'Bad',
            'B': 'Bad',
            'C': 'Bad'
        },

    ]

    with open(raw_data_path, mode='w', newline='') as raw_csv_file:
        writer = csv.DictWriter(raw_csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # yield data
    yield raw_data_path, clean_data_path

    # Teardown 
    os.remove(raw_data_path)
    os.remove(clean_data_path)
```

This is the `@pytest.fixture` function process:
1. Setup creates the `raw_data_path` and `clean_data_path`.
2. Define the contents of the `raw_data_path` file and create it. 
3. `yield` the data file paths to be used in the unit test. 
4. Teardown the files to return the environment to its original state. 

Now that we have our `fixture` function we can build our `pytest`:
```python
def test_on_data(raw_and_clean_data_file):
    raw_path, clean_path = raw_and_clean_data_file
    preprocess(raw_path, clean_path)

    with open(clean_path) as clean_csv_file:
        last_line = clean_csv_file.readlines()[-1].strip()

    actual = last_line
    expected = 'Good,Good,Good'
    message = f"The actual row data is {actual} and the expected is {expected}"

    assert actual == expected, message
```
Here is this process broken down:
1. we use the `raw_and_clean_data_file` function as a parameter for our `test_` unit test. 
2. Run our `preproess` function. 
3. Open clean file and verify the content of the file using `assert` statements. 

## Built-in tmpdir fixture
We can use the `tmpdir` fixture to follow this process:
1. setup of `tmpdir`
2. setup fixture function 
3. test
4. tear down fixture function 
5. tear down `tmpdir`

More research is needed. Info can be found [here](https://docs.pytest.org/en/6.2.x/tmpdir.html).