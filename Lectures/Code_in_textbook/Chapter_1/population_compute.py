population_current = 307357870
year_day = 365

second_total = year_day * 24 * 60 * 60

born_increase = second_total // 7

death_decrease = second_total // 13

immigrant_increase = second_total // 35


population_change_next_year = born_increase - death_decrease + immigrant_increase

year_enter = input("Please enter a year in your mind: ")

sub_year = int(year_enter) - 2009

population_now = population_current + sub_year * population_change_next_year

print(f"In {year_enter}, there are {population_now} people in the USA.")