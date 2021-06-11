# Jarandon Adams - 1812590
# Zylabs 1.12

first_service_cost = 0
second_service_cost = 0

print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12\n")

service1 = input("Select first service:\n")
service2 = input("Select second service:\n")

if service1 == "Oil change":
    first_service_cost = 35
elif service1 == "Tire rotation":
    first_service_cost = 19
elif service1 == "Car wash":
    first_service_cost = 7
elif service1 == "Car wax":
    first_service_cost = 12
elif service1 == "-":
    service1 = "No service"
    first_service_cost = 0

if service2 == "Oil change":
    second_service_cost = 35
elif service2 == "Tire rotation":
    second_service_cost = 19
elif service2 == "Car wash":
    second_service_cost = 7
elif service2 == "Car wax":
    second_service_cost = 12
elif service2 == "-":
    service2 = "No service"
    second_service_cost = 0


print("\nDavy's auto shop invoice")
print("\nService 1: " + service1 + ", $" + str(first_service_cost))
print("Service 2: " + service2 + ", $" + str(second_service_cost))
print("\nTotal: $" + str(first_service_cost + second_service_cost))
