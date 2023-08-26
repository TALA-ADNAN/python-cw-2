my_name = input("What is your name ? ")
my_age = int(input("How old are you ? "))
print(f'Your name is {my_name} and you are {my_age} years old')
first_number = int(input("Enter the first number "))
secound_number = int(input("Enter the secound number "))
operation = (input("What is your type of operation? "))
print(f'your type of operation is {operation}')
if operation == "+":
    print(first_number+secound_number)
elif operation == "-":
    print(first_number-secound_number)
elif operation == "*":
    print(first_number*secound_number)
elif operation == "/":
    print(first_number/secound_number)
else:
    print("the operation is not valid")
bus_capacity = 50
people_inbus = int(input("How many people are on the bus?"))
people_outbus = int(input("How many people do you want to enter the bus?"))
empty_seats = bus_capacity - people_inbus
print(empty_seats)
if empty_seats > people_outbus:
    print(f'There are {empty_seats} empty seats ')
elif empty_seats <= people_outbus:
    print("The bus is full")
