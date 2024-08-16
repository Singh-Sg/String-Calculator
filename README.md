# String Calculator

This project implements a String Calculator in Python, following the principles of Test-Driven Development (TDD). The calculator takes a string of numbers and returns their sum, supporting various delimiters, including custom ones, and handling edge cases such as negative numbers.

## Features

- **Add Method**: Takes a string of comma-separated numbers and returns their sum.
- **Support for Multiple Delimiters**: Handles both commas and newlines as delimiters.
- **Custom Delimiters**: Allows the user to specify a custom delimiter in the format `//[delimiter]\n[numbers...]`.
- **Negative Numbers**: Raises an exception if negative numbers are present in the input string, listing all negative numbers in the exception message.

## Commands to execute the execute the test cases.

```python
python test_string_calculator.py
