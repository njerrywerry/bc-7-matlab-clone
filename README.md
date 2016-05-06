# Mini Matlab Clone

## Features

* Array and matrix creation using variables:
```python
a = [1, 2, 3, 4]
b = [1, 2, 3; 4, 5, 6]
c = [45, 67, 34; 32, 1, 6]
```

* Creating zero matrices using the 'zeros' method:
```MATLAB
z = zeros(5,1)
```

* Matrix and array operations:
  * Addition of a matrix and a number:
  ```python
  a + 10
  ```
  * Transposing a matrix using an apostrophe operator ('):
  ```python
  a'
  ```
  * Inverse of a matrix:
  ```python
  inv(a)
  ```

* Concatenation, i.e. joining two arrays to form a larger one:
  * Horizontal concatenation:
  ```python
  A = [a,b]
  ```
  * Vertical concatenation:
  ```python
  B = [a;b]
  ```
