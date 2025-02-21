def add(a, b):
    print("add function have been used")
    return a + b

n1 = input("Please enter the first number:")
n2 = input("Please enter the second number:")

num1 = int(n1)
num2 = int(n2)
sum = add(num1, num2)
print(sum)