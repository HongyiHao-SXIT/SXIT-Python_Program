def check_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("29 days")
    else:
        print("28 days")

month = int(input("please enter a month:"))
if month in (4, 6, 9, 11):
    print("30 days")
elif month == 2:
    year = int(input("please enter a year:"))
    check_year(year)
elif month in (1, 3, 5, 7, 8, 10, 12):
    print("31 days")
else:
    print("Invalid month. Please enter a number between 1 and 12.")