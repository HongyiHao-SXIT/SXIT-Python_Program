def check_narcissistic_number(num):
    num_str = str(num)
    n = len(num_str)
    total = 0
    for digit in num_str:
        total += int(digit) ** n
    return total == num
def is_palindrome_number_string(num):
    num_str = str(num)
    return num_str == num_str[::-1]

for num in range(100, 999):
    if check_narcissistic_number(num) and is_palindrome_number_string(num):
        print(f"{num}is a Narcissistic number and palindrome number")
    elif check_narcissistic_number(num):
        print(f"{num} is a Narcissistic number but not palindrome number")
    elif is_palindrome_number_string(num):
        print(f"{num} is palindrome number but not Narcissistic number")