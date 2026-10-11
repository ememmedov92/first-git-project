################################
#TASK1
from turtle import distance


a1 = int(input("Ededi daxil edin: "))
a2 = int(input("Ikinci ededi daxil edin: "))

if a1 > a2 :
    print(a1, "daha boyukdu") 
elif a2 > a1 :
    print(a2, "daha boyukdu")
else:
    print("beraberdiler")

######################################################
#TASK2
number = float(input("Ededi daxil edin: "))

if number > 0:
    print("Musbet")
elif number < 0:
    print("Menfi")
else:
    print("Sifir")

#################################################
#TASK3
number = int(input("Ededi daxil edin: "))

if number % 2 == 0:
    print("Cut")
else:
    print("Tek")

##################################################
#TASK4
score = int(input("Balı daxil edin: "))

if score < 0 or score > 100:
    print("Duzgun bal daxil edin")
elif score >= 91:
    print("A")
elif score >= 81:
    print("B")
elif score >= 71:
    print("C")
elif score >= 61:
    print("D")
elif score >= 51:
    print("E")
else:
    print("F")

##############################################
#TASK5
a1 = float(input("Birinci ededi daxil edin: "))
a2 = float(input("Ikinci ededi daxil edin: "))
a3 = float(input("Ucuncu ededi daxil edin: "))

if a1 > a2:
    if a1 > a3:
        m = a1
    else:
        m = a3
elif a2 > a3:
    m = a2
else:
    m = a3

print("Böyük:", m)

#############################################
#TASK6
a1 = float(input("Birinci ededi daxil edin: "))
emel = input("Emeli daxil edin (+, -, *, /, %, **, //): ")
a2 = float(input("Ikinci ededi daxil edin: "))

if emel == "+":
    print("Netice :", a1 + a2)
elif emel == "-":
    print("Netice :", a1 - a2)
elif emel == "*":
    print("Netice :", a1 * a2)
elif emel == "/":
    if a2 == 0:
        print("0 a bölüne bilmez")
    else:
        print("Netice:", a1 / a2)
elif emel == "%":
    if a2 == 0:
        print("0 a bölüne bilmez")
    else:
        print("Netice:", a1 % a2)
elif emel == "**":
    if a1 == 0 and a2 < 0:
        print("0 in menfi ustlu derecesi olmaz")
    else:
        print("Netice:", a1 ** a2)
elif emel == "//":
    if a2 == 0:
        print("0 a bölüne bilmez")
    else:
        print("Netice:", a1 // a2)
else:
    print("Sehvlik var")

##########################################
#TASK7
yasin = int(input("Yasinizi daxil edin: "))

if yasin < 0:
    print("Olmaz")
elif yasin  <= 12:
    print("Child")
elif yasin <= 17:
    print("Teenager")
elif yasin <= 64:
    print("Adult")
else:
    print("Senior")

#########################################
#TASK8
pul = float(input("Meblegi daxil edin : "))

if pul < 0:
    print("Olmaz")
else:
    if pul < 100:
        faiz = 0
    elif pul < 300:
        faiz = 0.10
    elif pul < 500:
        faiz = 0.15
    else:
        faiz = 0.20

    endirim = pul * faiz
    son = pul - endirim

    print("Netice :", pul, "AZN")
    print("Endirim faizi :", endirim, "AZN")
    print("Son qiymet :", son, "AZN")

#########################################
#TASK9
#########################################
#TASK10
balans = 1000
pul = float(input("Cekeceyin pul: "))

if pul <= 0:
    print("Olma bilmez")
elif pul > balans:
    print("Pulun azdi")
else:
    balans = balans - pul
    print("Qalan pulun :", balans, "AZN")

##########################################
#TASK11
ist_olunan = float(input("Enter monthly electricity usage in kWh: "))

if ist_olunan < 0:
    print("ola bilmez")
else:
    if ist_olunan <= 100:
        emsal = 0.08
    elif ist_olunan <= 300:
        emsal = 0.12
    else:
        emsal = 0.15

    hesab = ist_olunan * emsal

    print("ne qeder istifade :", ist_olunan, "kWh")
    print("1 kwh ya dusen pul :", emsal, "AZN/kWh")
    print("cemi qiymet :", hesab, "AZN")

#########################################
#TASK12
l = float(input("Ne qeder getdin : "))
ilk = 2

if l < 0:
    print("mesafe menfi ola bilmez")
else:
    if l <= 5:
        e = 0.70
    elif l <= 15:
        e = 0.60
    else:
        e = 0.50

    cem = l * e
    son = ilk + cem

    print("Ilk verilen pul :", ilk, "AZN")
    print("Gedilen yol pulu :", cem, "AZN")
    print("Odemeli oldugun pul :", son, "AZN")

##########################################
#TASK13g