# Jarandon Adams - 1812590
# Homework 1

print("Welcome to my Age Calculator")

# Enter current date

print("Please enter the current date below ↓")
current_Month = int(input('Current Month:'))
if current_Month > 12:
    exit()
current_Day = int(input('Current Day:'))
current_Year = int(input('Current year:'))

# Enter birth date

print("Please enter your Birthday ↓")
birth_Month = int(input('Birthday Month:'))
birth_Day = int(input('Birth Day:'))
birth_Year = int(input('Birth year:'))

# Calculate age
# If birthday month/day are greater than current month/day (Birthday passed already), add a year to "years"

years = current_Year - birth_Year - 1
if birth_Month < current_Month:
    years += 1
elif current_Month == birth_Month:
    if birth_Day < current_Day:
        years += 1

# If birthday is today, print Happy Birthday. Else, print current age

if current_Month == birth_Month and current_Day == birth_Day:
    print('Happy Birthday!!')
elif current_Month != birth_Month or current_Day != birth_Day:
    print('You are ' + str(years) + " years old.")


