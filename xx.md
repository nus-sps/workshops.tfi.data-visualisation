```
Use `#` to write comments.

print('One')
print('Two')
print('Three')

print('One')              # This is a comment
print('Two')              # The intepreter ignores this line
print('Three')
```

```
Python is case sensitive.

print('Hello World')     

```


```
`x` is not the same as `‘x’`.

print(x)


```


```
`=` is not the same as `==`.


```


```
Be careful about indentaions at the start of a line.

x = 10
print(x)
```


```
Add functionalit by using packages.

sqrt(4) 
math.sqrt(4)
```

```
. indicates ownership.


```




```
You can store data as list or numpy arrays.

py_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]                  # A Python list
np_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10] )      # a numpy array


np_array[np_array > 4]    # Show me (subset) numbers more than 4



```


```
Access elements of a list using `[2:3]`.

```


```
Get help by using `?`.

```



# Pandas




| How to locate certain rows and columns?         | Columns: `df[[column_names]]`<br />By number: `df.iloc[row_number,column_number]<br />`By name: `df.loc[row_index,column_name]` |
| D                                               |                                                              |
| Replace missing numbers                         |                 `df.fillna(0,inplace=True)`                  |



## Housekeeping

1. Are there any unnecessary columns? Lets drop them!
2. Change column names?
3. Change values to be nicer?
4. How many numbers are missing? What are we going to do with them?
   1. Who missed the tests?
   2. Fill missing numbers
   3. Drop missing numbers
5. Questions (subsetting)
   1. How many major, distributio?
   2. How many females, gender?
   3. How many females taking chemistry?
6. What are the max, min, median of the test columns?
7. Is a particualr student in my class?
8. Sort the class by ascendin total
