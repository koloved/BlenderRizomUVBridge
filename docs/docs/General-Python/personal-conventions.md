---
layout: default
title: Personal Convention
parent: General Python
nav_order: 1
---

# Personal Convention
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Line Breaks

### Functions

If a function call or definition exceeds the 80 character limit I split the arguments onto separate lines with a hanging bracket. When defining a function arguments should be proceeded by two tabs instead of one to distinguish it from the body of the function. I try to keep the length of each broken line as uniform as possible while still keeping it fairly compact.

```python
def example_function(
        argument1, argument2, argument3, argument4,
        argument5, argument6, argument7, argument8):
    
    # function code
```

When calling a function I only use a single tab indent.

```python
example_function(
    argument1=1, argument2=2, argument3=3,
    argument4=4, argument5=5, argument6=6,
    argument7=7, argument8=8)
```

---

### Strings

To break up long string I use string concatenation, again trying to keep lines uniform in length and all lines should have matching indentation. The line should always be broken before a space but before punctuation, I find this to have the best readability.

```python
my_string = ("This is a very long string that I will need to break up" 
                    " in order to conform to pep8 convention."
                    " To do this I am going to use string concatenation.")

print(my_string)
```

This would result in: `This is a very long string that I will need to break up in order to conform to pep8 convention. To do this I am going to use string concatenation.`.

---

### Operators

When breaking lines with operators, the line should be broken before the operator.

```python
addition = 5
                + 5
                * 3
```

## Docstrings

My preference is to use google style docstrings, each argument should have its data type specified. For a multiline docstring the closing quotation marks should be on their own line aligned in the same column as the opening marks. This does not apply for a single line docstring.

```python
def example_function(arg1, arg2)
    """This is an example function.

    Args:
        arg1 (str): The first parameter
        arg2 (int): The second parameter
    
    returns:
        str: example message

    """
```
