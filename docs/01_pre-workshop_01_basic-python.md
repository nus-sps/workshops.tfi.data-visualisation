# (PART) Pre Workshop Material



# Some Python Basics

##  Python is Case Sensitive  {}

This will work.


```python
print('Hello World')
#> Hello World
```

This will **not**.


```python
Print('Hello World')
#> Error in py_call_impl(callable, dots$args, dots$keywords): NameError: name 'Print' is not defined
#> 
#> Detailed traceback:
#>   File "<string>", line 1, in <module>
```

##  <code>x</code> is a variable. 'x' is an English letter  {}

We asking Python to print the English letter 'x'.

```python
print('x')
#> x
```

We asking Python to print the value related to the **variable** `x`.

```python
x = 10
print(x)
#> 10
```

##  We can use f'letters{x}' to combine English with variables  {}


```python
x = 10
text = 'My age is {x}.'
print(text)
#> My age is {x}.
```

##  Be mindful of spaces(indentation) at the start of a line  {}

This will work.


```python
x = 10
y = 20
```

This will **not**.


```python
x = 10
  y = 20
```


##  Python has functions  {}

`print()` is a good example of a function in Python. For this function to work it needs something (which we call an argument) to print. We need supply this argument within the function's brackets `()`.


```python
print('Hello World')
#> Hello World
```

A typical function usually can accept additional arguments to do more things. For example the `print()` function allows us to add something to the end.


```python
print('Hello World', end = '******')
#> Hello World******
```

You can find out all about a function my looking at its help file as follows


```python
print?
```
```
print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

##  Python uses these brackets: ( ), [ ], { }  {}


```python
print('Hello World')
#> Hello World
```


##  Python sometimes act like a prima donna when you make an error  {}


```python
print('Hello World')
#> Hello World
```


##  Python has many (many) cool packages  {}


```python
print('Hello World')
#> Hello World
```



##  You can think of the dot('.') as indicating ownership  {}


```python
print('Hello World')
#> Hello World
```


-   Example: `math.sqrt()` means `sqrt()` belonging to `math`
