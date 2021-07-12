# Jarandon Adams - 1812590
# Zylabs 12.9

program = input().split()
first_name = program[0]

while first_name != '-1':
    try:
        age = int(program[1]) + 1
    except ValueError:
        age = 0

    print('{} {}'.format(first_name, age))

    program = input().split()
    first_name = program[0]
