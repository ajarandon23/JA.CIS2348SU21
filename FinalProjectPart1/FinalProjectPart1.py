# Jarandon Adams
# Final Project Part 1

import csv
from operator import itemgetter
from datetime import datetime

# creating empty lists for each given csv data file
manufacturer_list = []
price_list = []
svc_date_list = []

# Add csv file data into to the newly created lists
with open("ManufacturerList.csv") as manufactlist:
    read_mx = csv.reader(manufactlist)
    read_mx = sorted(read_mx, key=itemgetter(0))
    for line in read_mx:
        manufacturer_list.append(line)

with open("PriceList.csv") as priceslist:
    read_px = csv.reader(priceslist)
    read_mx = sorted(read_mx, key=itemgetter(0))
    for line in read_px:
        price_list.append(line)

with open("ServiceDatesList.csv") as servicedlist:
    read_sx = csv.reader(servicedlist)
    read_mx = sorted(read_mx, key=itemgetter(0))
    for line in read_sx:
        svc_date_list.append(line)

# here each list will be sorted in order by ID for better organization
new_manufactlist = (sorted(manufacturer_list, key=itemgetter(0)))
new_priceslist = (sorted(price_list, key=itemgetter(0)))
new_servicedlist = (sorted(svc_date_list, key=itemgetter(0)))

# here we have to append the new remaining service dates and prices to the final list
for x in range(0, len(new_manufactlist)):
    new_manufactlist[x].append(new_priceslist[x][1])

for x in range(0, len(new_manufactlist)):
    new_manufactlist[x].append(new_servicedlist[x][1])

final_list = new_manufactlist
complete_inventory = (sorted(final_list, key=itemgetter(1)))

# here the fullinventory.csv is written with the complete_inventory list in their required order
with open('FullInventory.csv', 'w') as new_file:
    file_write = csv.writer(new_file)
    for phrase in range(0, len(complete_inventory)):
        file_write.writerow([complete_inventory[phrase][0], complete_inventory[phrase][1],
                             complete_inventory[phrase][2], complete_inventory[phrase][4],
                             complete_inventory[phrase][5], complete_inventory[phrase][3]])

# here new lists are created for each of the item types: laptop/phone/tower
items_type = final_list
item_laptop_list = []
item_phone_list = []
item_tower_list = []

# here each list is searched through for specific item types and then appended it to its corresponding list
for word in range(0, len(items_type)):
    if items_type[word][2] == "tower":
        item_tower_list.append(items_type[word])
    elif items_type[word][2] == "phone":
        item_phone_list.append(items_type[word])
    elif items_type[word][2] == "laptop":
        item_laptop_list.append(items_type[word])
    else:
        break

# here files are written for the specific item types: laptop/phone/tower
with open('LaptopInventory.csv', 'w') as new_files:
    write_laptop_inv = csv.writer(new_files)
    for x in range(0, len(item_laptop_list)):
        write_laptop_inv.writerow([item_laptop_list[x][0], item_laptop_list[x][1], item_laptop_list[x][4],
                                   item_laptop_list[x][5], item_laptop_list[x][3]])

with open('PhoneInventory.csv', 'w') as new_files:
    write_phone_inv = csv.writer(new_files)
    for x in range(0, len(item_phone_list)):
        write_phone_inv.writerow([item_phone_list[x][0], item_phone_list[x][1], item_phone_list[x][4],
                                  item_phone_list[x][5], item_phone_list[x][3]])

with open('TowerInventory.csv', 'w') as new_files:
    write_tower_inv = csv.writer(new_files)
    for x in range(0, len(item_tower_list)):
        write_tower_inv.writerow([item_tower_list[x][0], item_tower_list[x][1], item_tower_list[x][4],
                                  item_tower_list[x][5], item_tower_list[x][3]])

# here dates are split by the "/" to be compared to the current date using datetime() function
new_date_list = []
present_dt = datetime.now()


def split_servicedate(svcdate_list):
    for date in svcdate_list:
        y = date[1].split("/")
        item_date = datetime(int(y[2]), int(y[0]), int(y[1]))
        if item_date < present_dt:
            new_date_list.append(date)


split_servicedate(svc_date_list)

# 1. here a new file is written for service dates that occur before today/day code is executed
# 2. then each date from the expired list is compared to all the items in the manufacturing list
# 3. when a id match is found, it writes it onto the csv file
with open('PastServiceDateInventory.csv', 'w') as new_files:
    count = 0
    write_past_sdi = csv.writer(new_files)

    for items in new_date_list:
        for x in range(len(new_manufactlist)):
            if items[0] == new_manufactlist[x][0]:
                write_past_sdi.writerow([new_manufactlist[x][0], new_manufactlist[x][1],
                                         new_manufactlist[x][2], new_manufactlist[x][4],
                                         new_manufactlist[x][5], new_manufactlist[x][3]])

# here an empty list is created for the damaged products within the inventory
damaged_product_list = []

# here inventory is searched and determines whether listed items have been damaged based on position
for x in range(0, len(items_type)):
    if items_type[x][3] == "damaged":
        damaged_product_list.append(items_type[x])

damaged_product_list = (sorted(damaged_product_list, key=itemgetter(4), reverse=True))

# here a new file is written to put damaged products within in required order order
with open('DamagedInventory.csv', 'w') as new_files:
    write_damaged_inv = csv.writer(new_files)
    for x in range(0, len(damaged_product_list)):
        write_damaged_inv.writerow([damaged_product_list[x][0], damaged_product_list[x][1], damaged_product_list[x][2],
                                    damaged_product_list[x][4], damaged_product_list[x][5]])

# here contains the user input for their manufacturer and item type so output can generated
input_manufacturer = str(input("Please Enter your Manufacturer: "))
input_type = str(input("Please Enter your Item Type: "))
