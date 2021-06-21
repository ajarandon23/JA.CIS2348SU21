# Jarandon Adams - 1812590
# Zylabs 6.22

value1 = int(input('Enter value 1:'))
value2 = int(input('Enter value 2:'))
value3 = int(input('Enter value 3:'))
value4 = int(input('Enter value 4:'))
value5 = int(input('Enter value 5:'))
value6 = int(input('Enter value 6:'))

solution_found = False

for x_value in range(-10, 11):
    for y_value in range(-10, 11):
        if value1 * x_value + value2 * y_value == value3 and value4 * x_value + value5 * y_value == value6:
            print(x_value, y_value)
            solution_found = True

if not solution_found:
    print("No solution")

