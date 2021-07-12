# Jarandon Adams - 1812590
# Homework 2

month_list = {
    "january": "1", "february": "2", "march": "3",
    "april": "4", "may": "5", "june": "6",
    "july": "7", "august": "8", "september": "9",
    "october": "10", "november": "11", "december": "12"
}

input_file = open('C:\\Users\\Desktop\\inputDates.txt', 'r')
output_file = open('C:\\Users\\Desktop\\parsedDates.txt', 'w')

for each in input_file:
    if each != "-1":
        lis = each.split()
        if len(lis) >= 3:
            month = lis[0]
            day = lis[1]
            year = lis[2]

        if month.lower() in month_list:
            comma = day[-1]
            if comma == ',':
                day = day[:len(day) - 1]
                month_number = month_list[month.lower()]
                parsed_dates = month_number + "/" + day + "/" + year

                print(parsed_dates)
                output_file.write(parsed_dates)
                output_file.write("\n")

output_file.close()
input_file.close()
