<link rel="stylesheet" href="../stylesheet.css">

# NumPy
> **[Numpy (Numerical Python)](https://www.w3schools.com/python/numpy/default.asp)**: *NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices.*

<u-b>IMPORT</u-b>

```py
import numpy as np
```

## Data Types
| Representation | Type               |
|----------------|--------------------|
| `i`            | *Integer*          |
| `b`            | *Boolean*          |
| `u`            | *Unsigned Integer* |
| `f`            | *Float*            |
| `c`            | *Complex*          |
| `m`            | *Time-delta*       |
| `M`            | *Date-Time*        |
| `O`            | *Object*           |
| `S`            | *String*           |
| `U`            | *Unicode String*   |
| `V`            | *Void*             |

## Arrays

<u-b>N-D CREATION</u-b>

```py
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
```

<u-b>INDEXING</u-b>

```py
a = np.array([0, 1, 2, 3, 4])
print(a[0]) # 0

b = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(b[0, 1]) # 1
```

<u-b>SLICING</u-b>

```py
a = np.array([0, 1, 2, 3, 4, 5, 6])
print(a[1:5]) # [1, 2, 3, 4]

b = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]])
print(b[1, 1:4]) # [6, 7, 8]
```

- **Slicing Step**

```py
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2]) # [1, 3]
```

<u-b>ARRAYS WITH DEFINED DATA TYPE</u-b>

```py
arr = np.array([1, 2, 3, 4], dtype='S')

# For i, u, f, S and U we can define size as well.
arr = np.array([1, 2, 3, 4], dtype='i4')
```

<u-b>CAST EXISTING ARRAY</u-b>
```py
arr = np.array([1.1, 2.1, 3.1])
int_arr = arr.astype('i')
print(int_arr) # [1, 2, 3]
```