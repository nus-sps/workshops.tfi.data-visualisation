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



| Are there any missing numbers?                  | Dataframe :`df.isna()`<br />Row-wise :`df.isna().any(axis = 1)`<br />Column-wise :`df.isna(axis = 0)` |


| How to locate certain rows and columns?         | Columns: `df[[column_names]]`<br />By number: `df.iloc[row_number,column_number]<br />`By name: `df.loc[row_index,column_name]` |
| D                                               |                                                              |
| Replace missing numbers                         |                 `df.fillna(0,inplace=True)`                  |

If we want to see specific rows or columns in the dateframe, we have two options.





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

Topic: GEH1033 | Lectures n Such
Start Time : Sep 9, 2021 11:57 AM

Meeting Recording:


Access Passcode: anthropogenic_21



Topic: TFI e-Workshop 1 : Using Python to Tell Stories with Data
Start Time : Sep 11, 2021 09:30 AM

Meeting Recording:
https://nus-sg.zoom.us/rec/share/Lr_RbQlLJUBkSoAD1UWrQVOVWLOBwdeeyrKBWG_O6EPGb6tlyWVc13KcjE5_Qx5M.4qvbiOivsy_WdaN-

Access Passcode: 1-mirror-on-the-head

