Services = {
            'Oil change': 35,
            'Tire rotation': 19,
            'Car wash': 7,
            'Car wax': 12,
            '-': 0
            }
print("Davy's auto shop services")
print("Oil change -- $35")
print("Tire rotation -- $19")
print("Car wash -- $7")
print("Car wax -- $12")
print()
print("Select first service:")
First = input()
print()
print('Select second service:')
Second = input()
Total = 0
print()
print("Davy's auto shop invoice")
print()

if First == 'Oil change':
    print("Service 1: Oil change, $", 35)
elif First == 'Tire rotation':
    print("Service 1: Tire rotation, $", 19)
elif First == 'Car wash':
    print("Service 1: Car wash, $", 7)
elif First == 'Car wax':
    print("Service 1: Car wax, $", 12)
elif First == '-':
    print("Service 1: No service")
    print()

if Second == 'Oil change':
    print("Service 2: Oil change, $", 35)
elif Second == 'Tire rotation':
    print("Service 2: Tire rotation, $", 19)
elif Second == 'Car wash':
    print("Service 2: Car wash, $", 7)
elif Second == 'Car wax':
    print("Service 2: Car wax, $", 12)
elif Second == '-':
    print("Service 2: No service",)
Total = Services.get(First) + Services.get(Second)
print("Total: $", Total)