# Python - February 25th

## Basics
### Operators
In Python, arithmetic operators are used to perform basic mathematical operations. Let's take a closer look at the most common ones:

- **Addition (`+`)**: This operator adds two numbers together. For example:
```python
a = 15
b = 20
result = a + b
print(result)  # Output: 35
```

- **Subtraction (`-`)**: It subtracts the right - hand number from the left - hand number.
```python
x = 50
y = 15
diff = x - y
print(diff)  # Output: 35
```

- **Multiplication (`*`)**: Multiplies two numbers.
```python
m = 7
n = 8
product = m * n
print(product)  # Output: 56
```

- **Modulus (`%`)**: Returns the remainder after division.
```python
p = 17
q = 3
remainder = p % q
print(remainder)  # Output: 2
```

- **Division (`/`)**: Performs normal division and gives a floating - point result.
```python
r = 25
s = 4
quotient = r / s
print(quotient)  # Output: 6.25
```

### Strings
#### `str.format()` Method
The `str.format()` method is a handy way to insert values into a string. It also allows you to control how the values are aligned.

- **Left alignment (`<`)**:
```python
print("Number: {:<5}".format(123))  # Output: "Number: 123  "
```

- **Right alignment (`>`)**:
```python
print("Number: {:>5}".format(123))  # Output: "Number:   123"
```

- **Center alignment (`^`)**:
```python
print("Number: {:^5}".format(123))  # Output: "Number:  123 "
```

#### Indexing
- **Positive Indexing**: In Python, string indexing starts at 0.
```python
word = "Python"
print(word[0])  # Output: 'P'
print(word[3])  # Output: 'h'
```

- **Negative Indexing**: You can also use negative numbers to index from the end of the string.
```python
print(word[-1])  # Output: 'n'
print(word[-3])  # Output: 'h'
```

- **Length**: You can find the length of a string using the `len()` function.
```python
print(len(word))  # Output: 6
```

#### String Concatenation and Conversion
- **String Concatenation (`+`)**:
```python
greeting = "Hello"
name = "Alice"
message = greeting + ", " + name
print(message)  # Output: "Hello, Alice"
```

- **`str()` Function**: Converts a non - string value to a string.
```python
age = 25
age_str = str(age)
print("I am " + age_str + " years old.")  # Output: "I am 25 years old."
```

- **`repr()` Function**: Creates a string representation of an object.
```python
text = "Python is fun!"
repr_text = repr(text)
print(repr_text)  # Output: "'Python is fun!'"
```

#### String Case Conversion
- **`title()` Method**: Converts the first letter of each word to uppercase.
```python
sentence = "python programming is great"
print(sentence.title())  # Output: "Python Programming Is Great"
```

- **`upper()` Method**: Converts all characters to uppercase.
```python
print(sentence.upper())  # Output: "PYTHON PROGRAMMING IS GREAT"
```

- **`lower()` Method**: Converts all characters to lowercase.
```python
shout = "HELLO WORLD"
print(shout.lower())  # Output: "hello world"
```

#### Splitting and Joining Strings
- **`split()` Method**: Splits a string into a list of substrings.
```python
phrase = "apple banana cherry"
fruits = phrase.split()
print(fruits)  # Output: ['apple', 'banana', 'cherry']

csv = "red,green,blue"
colors = csv.split(",")
print(colors)  # Output: ['red', 'green', 'blue']
```

- **`join()` Method**: Joins a list of strings into a single string.
```python
words = ["I", "love", "Python"]
sentence = " ".join(words)
print(sentence)  # Output: "I love Python"

numbers = ["1", "2", "3"]
number_str = "-".join(numbers)
print(number_str)  # Output: "1-2-3"
```

#### Searching for Substrings
- **`count(sub[, start[, end]])` Method**: Counts the number of times a substring appears.
```python
text = "banana is a fruit, banana is yellow"
print(text.count("banana"))  # Output: 2
print(text.count("banana", 0, 10))  # Output: 1
```

- **`find(sub[, start[, end]])` Method**: Finds the first occurrence of a substring.
```python
text = "The quick brown fox"
print(text.find("fox"))  # Output: 16
print(text.find("cat"))  # Output: -1
```

- **`index(sub[, start[, end]])` Method**: Similar to `find()`, but raises an error if the substring is not found.
```python
try:
    print(text.index("fox"))  # Output: 16
    print(text.index("cat"))
except ValueError:
    print("Substring not found.")
```

- **`startswith(prefix[, start[, end]])` Method**: Checks if a string starts with a given prefix.
```python
text = "Hello, world!"
print(text.startswith("Hello"))  # Output: True
print(text.startswith("world", 7))  # Output: True
```

- **`endswith(suffix[, start[, end]])` Method**: Checks if a string ends with a given suffix.
```python
print(text.endswith("world!"))  # Output: True
print(text.endswith("Hello", 0, 5))  # Output: True
```

#### Replacing Substrings
The `replace()` method replaces occurrences of a substring.
```python
original = "The old car is red. The old house is big."
new = original.replace("old", "new")
print(new)  # Output: "The new car is red. The new house is big."

# Replace only the first occurrence
first_replace = original.replace("old", "new", 1)
print(first_replace)  # Output: "The new car is red. The old house is big."
```

#### Removing Whitespace
- **`strip()`**: Removes leading and trailing whitespace.
```python
whitespace_str = "   Python is awesome   "
stripped = whitespace_str.strip()
print(stripped)  # Output: "Python is awesome"
```

- **`lstrip()`**: Removes only leading whitespace.
```python
left_whitespace = "   Leading spaces"
left_stripped =