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

print(f"Total: {total : .2f}")
print(f"Average: {average :2f}")

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
print(f"Average: {total / count : .2f}")

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

#########################################################
#TASK13

temps = [int(input(f"Day {i}: ")) for i in range(1 , 8)]

hot_days = sum(1 for temp in temps if temp > 30)

hottest_day = temps.index(max(temps))

print(f"Hot days: {hot_days}")
print(f"Hottest day: {hottest_day}")

######################################################
#TASK14

#attempts en basda olmali idi attempts = 0

#####################################################
#TASK15

# Password: hello2024 
# Weak password: no 
# uppercase letters   
# Password: Hello2024 
# Strong password 

# m = "Weak password"
# while True :
#     pswrd = input()
#     if len(pswrd) < 8 :
#         print(f"{m:>2f} : cant be less than 8 characters")

###########################################################
#TASK16

d = 0
s = 0
k = 50
a = 1000

while s < a:
    s += k
    k += 10
    d += 1
    print(f"Month {d}: {s}")

print(f"Goal reached in month {d}")

###########################################################
#TASK17

# 101 den sonra ilk 7 ye bolunen tek ededi tapib cixarir

###########################################################
#TASK18

pin = "2580"
balance = 1000.0
attempts = 0
logged_in = False

while attempts < 3:
    entered_pin = input("Enter PIN: ")
    if entered_pin == pin:
        logged_in = True
        break
    else:
        attempts += 1
        print(f"Wrong PIN. Attempts left: {3 - attempts}")

if not logged_in:
    print("Card blocked")
    exit()

while True:
    print("\n--- ATM Menu ---")
    print("1 - Check balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Exit")
    
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        print(f"Balance: {balance} AZN")
        
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Invalid amount. Must be greater than 0.")
        else:
            balance += amount
            print(f"Successfully deposited. New balance: {balance} AZN")
            
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0 or amount > balance:
            print("Invalid amount. Cannot withdraw .")
        else:
            balance -= amount
            print(f"Successfully withdrew. New balance: {balance} AZN")
            
    elif choice == '4':
        print("Goodbye")
        break
        
    else:
        print("Invalid choice")

###############################################################
#TASK19

su_qiymeti = 1.50
qebul_edilenler = [0.05, 0.10, 0.20, 0.50, 1.0, 1]  

toplam = 0.0

while toplam < su_qiymeti:
    pul = float(input("Insert coin: "))
    
    if pul in qebul_edilenler:
        toplam += pul
        print(f"Total: {round(toplam, 2)}") 
    else:
        print("Coin not accepted")

print("Here is your water")

qaliq = toplam - su_qiymeti
print(f"Change: {round(qaliq, 2)}") #PYTHON KESR EDEDLERI TOPLAYANDA SEHVLER EDIR VERGULDEN EEEY SONRA XETALAR VERE BILIR
                                    #BUNA GORE DE KESR EDEDLERIN TOPLANMA PRINTINDE ROUND(NESE , 2) YAZMALIYIQ KI VERGULDEN SONRA 2 REQEM QALSIN
                                    #AMMMA 2 CI YOLDA VAR { :.2f} YAZARAQ SELIQELI OQLAN EDERIK TEMIZ CAVAB

##################################################################
#TASK20



    








