# Python List Notes
## I. Definition and Creation
### 1. Basic Concepts
A list in Python is an ordered and mutable collection of data that can hold elements of different types, represented by square brackets `[]`.

### 2. Creation Methods
- **Direct Assignment**:
```python
# Create a list containing integers
my_list = [1, 2, 3]
print(my_list)
```
- **Using the `list()` Function**:
```python
# Convert a tuple to a list
my_list = list((1, 2, 3))
print(my_list)

# Convert a string to a list
str_list = list("hello")
print(str_list)
```

## II. Access and Indexing
### 1. Positive Indexing
Indexing starts from 0. For example:
```python
my_list = [10, 20, 30]
print(my_list[0])  # Output: 10
```

### 2. Negative Indexing
Indexing starts from -1. For example:
```python
my_list = [10, 20, 30]
print(my_list[-1])  # Output: 30
print(my_list[-2])  # Output: 20
```

### 3. Slicing Operation
Use the `[start:stop:step]` format. For example:
```python
my_list = [10, 20, 30, 40, 50]
print(my_list[1:3])  # Output: [20, 30]
print(my_list[::2])  # Output: [10, 30, 50]
```

## III. Common Operations
### 1. Adding Elements
- **`append()`**: Adds an element to the end of the list.
```python
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
```
- **`insert()`**: Inserts an element at the specified position.
```python
my_list = [1, 2, 3]
my_list.insert(1, 15)
print(my_list)  # Output: [1, 15, 2, 3]
```

### 2. Deleting Elements
- **`remove()`**: Removes an element based on its value.
```python
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]
```
- **`pop()`**: Removes the element at the specified position, and defaults to removing the last element.
```python
my_list = [1, 2, 3]
removed = my_list.pop(1)
print(removed)  # Output: 2
print(my_list)  # Output: [1, 3]
```
- **`del` Statement**: Deletes the element at the specified index or the entire list.
```python
my_list = [1, 2, 3]
del my_list[0]
print(my_list)  # Output: [2, 3]

del my_list
# Accessing my_list at this point will result in an error
```

### 3. Modifying Elements
Modify elements directly by assigning values to their indices. For example:
```python
my_list = [10, 20, 30]
my_list[1] = 25
print(my_list)  # Output: [10, 25, 30]
```

### 4. Finding Elements
- **`in` Keyword**: Checks if an element is in the list.
```python
my_list = [10, 20, 30]
print(20 in my_list)  # Output: True
```
- **`index()`**: Returns the index of an element.
```python
my_list = [10, 20, 30]
print(my_list.index(30))  # Output: 2
```

## IV. List Operations
### 1. Concatenation
Use the `+` operator. For example:
```python
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)  # Output: [1, 2, 3, 4]
```

### 2. Repetition
Use the `*` operator. For example:
```python
print([10, 20] * 3)  # Output: [10, 20, 10, 20, 10, 20]
```

## V. Common Methods
### 1. Sorting
- **`sort()`**: Sorts the list in - place.
```python
my_list = [3, 1, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3]

my_list = [3, 1, 2]
my_list.sort(reverse=True)
print(my_list)  # Output: [3, 2, 1]
```
- **`sorted()`**: Returns a new sorted list, leaving the original list unchanged.
```python
my_list = [3, 1, 2]
new_list = sorted(my_list)
print(new_list)  # Output: [1, 2, 3]
print(my_list)  # Output: [3, 1, 2]
```

### 2. Counting Elements
The `count()` method. For example:
```python
my_list = [1, 2, 2, 3, 2]
print(my_list.count(2))  # Output: 3
```

### 3. Getting the List Length
The `len()` function. For example:
```python
my_list = [1, 2, 3]
print(len(my_list))  # Output: 3
```

## VI. Traversing Lists
### 1. Traversing with a `for` Loop
```python
my_list = [1, 2, 3]
for item in my_list:
    print(item)
```

### 2. Getting Both Index and Element
Use the `enumerate()` function. For example:
```python
my_list = [1, 2, 3]
for index, item in enumerate(my_list):
    print(index, item)
```

## VII. Nested Lists
### 1. Concept
Elements in a list can be lists themselves. For example:
```python
nested_list = [[1, 2], [3, 4]]
print(nested_list)
```

### 2. Accessing Nested Elements
Access elements through multiple - level indexing. For example:
```python
nested_list = [[1, 2], [3, 4]]
print(nested_list[0][1])  # Output: 2
``` 