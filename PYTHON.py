########################################
#TASK1

l = [ i for i in range(1, 11) ]
for i in l[: : -1] :
    print(i)
print("Liftoff")

######################################
#TASK2

a1 = input("yasinizi daxil edin: ")
a2 = input("yasinizi daxil edin: ")
a3 = input("yasinizi daxil edin: ")
a4 = input("yasinizi daxil edin: ")
a5 = input("yasinizi daxil edin: ")
l = [a1, a2, a3, a4, a5] ; m = 0 ; n = 0
for i in l:
    if int(i) >= 18 :
        m += 1
    else :
        n += 1
print(f"18 yashindan yuxari olanlar: {m}")
print(f"18 yashindan asagi olanlar: {n}")

# child_tickets = 0
# adult_tickets = 0

# for visitor in range(1, 6):
#     age = int(input(f"Age of visitor {visitor}: "))
#     if age < 18:
#         child_tickets += 1
#     else:
#         adult_tickets += 1

# print(f"Child tickets: {child_tickets}")
# print(f"Adult tickets: {adult_tickets}")

###############################
#TASK3

# 1 3 5 7 9

#############################
#TASK4

total = 0

for item in range(5):
    price = float(input(f"Price of item {item}: "))
    total += price

average = total / 5

print(f"Total: {total}")
print(f"Average: {average}")

############################
#TASK5

while True:
    password = input("New password: ")
    if len(password) < 8:
        print("Too short, try again")
    else:
        print("Password accepted")
        break #ELSENIN ICINDEDIR DEYE BURA YAZIRIQ YENI NORMALDI

##########################################
#TASK6

# balance
# balance
# balance
# done

###############################################
#TASK7

for gun in range(1 , 8) :
    print(f"Day {gun} :" , gun * 1200)
    gun += 1

############################################
#TASK8

correct_username = "admin"
correct_password = "1234"

for attempt in range(3):
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Welcome!")
        break #FOR OLANLARDADA BREAK ELEMEK OLUR!

    print("Wrong username or password")
else:
    print("Account locked")

###############################################
#TASK9

balance = 500

while True:
    amount = float(input("Amount: "))

    if amount == 0:
        print("Goodbye")
        break
    elif amount < 0:
        print("Invalid amount")
    elif amount > balance:
        print("Insufficient funds")
    else:
        balance -= amount
        print(f"Balance: balance: {g}")

###########################################
#TASK10

# wrong pin 2 attempts left
# wrong pin 1 attempts left
# access granted
# attempts used 3

###############################################
#TASK11

passed = 0                                    
failed = 0
total = 0
highest = 0
count = 0

grade = int(input("Grade: "))

while grade != -1:
    total += grade
    count += 1

    if grade >= 51:
        passed += 1
    else:
        failed += 1

    if grade > highest:
        highest = grade

    grade = int(input("Grade: "))

print(f"Passed: {passed}")
print(f"Failed: {failed}")
print(f"Highest: {highest}")
print(f"Average: {total / count.2f}")

######################################################
#TASK12

free_spaces = 20

while True:
    command = input("Command: ")

    if command == "stop":
        break
    elif command == "in":
        if free_spaces == 0:
            print("Garage full")
        else:
            free_spaces -= 1
    elif command == "out":
        if free_spaces == 20:
            print("Garage is empty")
        else:
            free_spaces += 1
    else:
        print("Unknown command")

    print(f"Free spaces: {free_spaces}")





