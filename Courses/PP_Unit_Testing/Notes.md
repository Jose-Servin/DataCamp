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