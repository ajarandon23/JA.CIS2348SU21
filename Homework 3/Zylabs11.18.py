# Jarandon Adams - 1812590
# Zylabs 10.18

numbers = input().split()
result = []

for num in numbers:
    num = int(num)
    if num >= 0:
        result.append(num)

result.sort()
for num in result:
    print(num, end=' ')
