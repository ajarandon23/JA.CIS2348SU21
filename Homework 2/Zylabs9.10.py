# Jarandon Adams - 1812590
# Zylabs 9.10

import csv
file_name = input()
word_frequency = {}

with open(file_name, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        for word in line:
            if word not in word_frequency.keys():
                word_frequency[word] = 1
            else:
                word_frequency[word] += 1

for key in word_frequency.keys():
    print(key + " " + str(word_frequency[key]))
