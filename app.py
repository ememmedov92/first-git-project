################################
#TASK1


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
#TASK13

age = int(input("Yasinizi daxil edin: "))
maas = int(input("Aylig maasinizi daxil edin: "))
qiymet = int(input("Istifade etdiyiniz kredit meblegi: "))

if age < 0:
    print("Sehvdi")
else:
    if maas < 0:
        print("Sehvdi")
    else:
        if qiymet <= 0:
            print("Sehvdi")
        else:
            if age < 18:
                print("Sehvdi")
            else:
                if maas < 500:
                    print("Sehvdi")
                else:
                    if qiymet > 10 * maas :
                        print("Sehvdi")
                    else:
                        print("Alindi")
                        print("Hersey hazirdi.")

###########################################
#TASK14

a = int(input("1 ci terefi : "))
b = int(input("2 ci terefi : "))
c = int(input("3 ci terefi : "))

if a <= 0:
    print("Olmaz")
else:
    if b <= 0:
        print("Olmaz")
    else:
        if c <= 0:
            print("Olmaz")
        else:
            if a + b > c:
                if a + c > b:
                    if b + c > a:
                        if a == b:
                            if b == c:
                                print("Beraberterefli")
                            else:
                                print("Beraberyanli")
                        else:
                            if a == c:
                                print("Beraberyanli")
                            else:
                                if b == c:
                                    print("Beraberyanli")
                                else:
                                    print("3 terefi ferqli")
                    else:
                        print("Olmaz")
                else:
                    print("Olmaz")
            else:
                print("Olmaz")

#########################################
#Task15
dimnetice = int(input("Enter exam score (0-700): "))
mektebnetice = int(input("Enter school score (0-100): "))
age = int(input("Enter age: "))

if age < 0:
    print("Olmaz.")
elif dimnetice < 0 or dimnetice > 700:
    print("Olmaz.")
elif mektebnetice < 0 or mektebnetice > 100:
    print("Olmaz.")
elif age < 16:
    print("Olmaz.")
elif dimnetice >= 600:
    print("Scholarship")
elif dimnetice >= 450:
    print("Qebul")
elif dimnetice >= 300:
    if mektebnetice >= 80:
        print("Qebul")
    else:
        print("Olmaz.")
else:
    print("Olmaz.")

#########################################
#TASK16
score = int(input("Ededi daxil ele: "))

if score < 0 or score > 100:
    print("Olmaz.")
else:
    if score >= 51 :
        print("Pass")
    else :
        print("Fail")

#########################################
#TASK17
total = int(input("pulunu yaz : "))
he_ya_yox = input("he mi yox mu : ")
if total < 0 or he_ya_yox != "he" :
    print("Olmaz")
if total > 100 or he_ya_yox != "he" :
    print("tam endrirm")
    print("Odeyin" , total)
else :
    print("5 man olmasin")
    print("Odeyin" , total + 5)

#########################################
#TASK18

heftegunu = int(input("Heftetin gununu daxil ele reqemle haa : "))

match heftegunu:
    case 1:
        day_name = "Monday"
        day_type = "Study day"
    case 2:
        day_name = "Tuesday"
        day_type = "Study day"
    case 3:
        day_name = "Wednesday"
        day_type = "Study day"
    case 4:
        day_name = "Thursday"
        day_type = "Study day"
    case 5:
        day_name = "Friday"
        day_type = "Study day"
    case 6:
        day_name = "Saturday"
        day_type = "Weekend"
    case 7:
        day_name = "Sunday"
        day_type = "Weekend"
    case _:
        day_name = "Invalid day"
        day_type = ""

print(day_name)
if day_type != "":
    print(day_type)
