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


#############################
#TASK19

# İçki kodunu və miqdarı daxil edirik
code = input("İçki kodunu daxil edin (T, C, J): ")
miqdar = int(input("Miqdari daxil edin (1-10): "))

if 1 <= miqdar <= 10:
    
    match code:
        case "T":
            drink_name = "Tea (Çay)"
            price = 2
        case "C":
            drink_name = "Coffee (Kofe)"
            price = 4
        case "J":
            drink_name = "Juice (Şirə)"
            price = 3
        case _:
            drink_name = "Naməlum"
            price = 0
            print("Xəta: Yalniz böyük hərflərlə T, C və ya J daxil edin!")

    if price > 0:
        total = price * miqdar

        if total >= 20 :
            order_status = "Large order"  
        else:
            order_status = "Regular order"
        
        print("İçki:", drink_name)
        print("Miqdar:", miqdar)
        print("Ümumi qiymət:", total, "AZN")
        print("Sifariş növü:", order_status)

else:
    print("Xəta: Miqdar yalniz 1 ilə 10 arasinda ola bilər!")

##############################
#TASK20

id = input("Tələbə nömrəsini daxil edin: ")

if len(id) == 0:
    print("Boş daxiletmə qəbul olunmur")
elif len(id) != 8:
    print("Tələbə nömrəsi tam olaraq 8 simvoldan ibarət olmalidir")
elif not id.isdigit():
    print("Nömrə yalniz rəqəmlərdən ibarət olmalidir")
else:
    print("Qəbul edilən nömrə:", id)

##############################
#TASK21

esl = "0427"

yaz = input("daxil ele kodu: ")

if len(yaz) == 0:
    print("bos qoyma")
elif len(yaz) != 4:
    print("4 digits olmalidi")
elif not yaz.isdigit():
    print("ancaq reqemler")
elif yaz == esl:
    print("Halaldi sene")
else:
    print("Sehvdi")

###############################
#TASK22

nomre = input("Nomreni daxil edin: ")
if len(nomre) == 0:
    print("Bos qoyma")
elif len(nomre) != 10:
    print("Nomre 10 reqemden ibaret olmalidi")
elif not nomre.isdigit():
    print("Nomre yalniz reqemlerden ibaret olmalidi")
elif nomre[0:3] != "050" and nomre[0:3] != "051" and nomre[0:3] != "055" and nomre[0:3] != "070" and nomre[0:3] != "077" and nomre[0:3] != "099":
    print("Nomre yalniz 050, 051, 055, 070, 077 ve 099 ile baslamalidi")
else:
    print("Nomre qebul olundu:", nomre)

#############################
#TASK23

var = 1000
pin = "0742"
daxil = input("Pin daxil edin: ")
if not daxil.isdigit():
    print("Pin yalniz reqemlerden ibaret olmalidi")
elif len(daxil) != 4:
    print("Pin tam olaraq 4 reqemden ibaret olmalidi")
elif daxil != pin:
    print("Sehv pin")
else: 
    print("Pin dogrudur. Balansiniz:", var, "AZN")
    cek = input("Cekeceyiniz meblegi daxil edin: ")
    if not cek.isdigit():
        print("Xəta: Məbləğ yalnız rəqəmlərdən ibarət olmalıdır!")
    else:
        cek = int(cek)
        if cek <= 0:
            print("Mebleg menfi ola bilmez")
        elif cek > var :
            print("Balansinizda kifayet qeder pul yoxdur")
        elif 10 <= cek <= 500 and cek % 10 == 0:
            print("sertimiz var olmaz")
        elif cek > 200 :
            print("Mebleg 200 AZN-dan cox olanda 2 manat gotururuk elave") 
            print("Cekeceyiniz mebleg:", cek, "AZN")
            print("Balansiniz:", var - cek - 2, "AZN")
        else:
            print("Cekeceyiniz mebleg:", cek, "AZN")
            print("Balansiniz:", var - cek, "AZN")


##############################
#TASK24

# • Read product code, quantity, coupon code, and delivery code as strings.
# • Use match / case for products: K = Keyboard (40 AZN), M = Mouse (20 AZN), H = Headphones (60 AZN). Only
# these uppercase codes are valid.
# • Quantity must contain ASCII digits only and represent a value from 1 to 5. Reject empty input, letters, spaces, signs,
# and decimal points before conversion.
# • Coupon must be exactly NONE or SAVE10. SAVE10 gives a 10% discount only when the subtotal is at least 100
# AZN; otherwise reject it as ineligible.
# • Use match / case for delivery: P = Pickup (free), S = Standard. Any other code is invalid.
# • For Standard delivery, use a ternary expression: free when the discounted subtotal is at least 80 AZN, otherwise 5
# AZN.
# • Validate in this order: product, quantity format, quantity range, coupon code, coupon eligibility, delivery code. Print
# the first error and no receipt if invalid.
# • On success, display product, quantity, subtotal, discount, delivery fee, and final total.

#################################
#TASK24

product_code = input("Məhsul kodunu daxil edin (K - Keyboard, M - Mouse, H - Headphones): ")

match product_code:
    case "K":
        product_name = "Keyboard"
        unit_price = 40
        valid_product = True
    case "M":
        product_name = "Mouse"
        unit_price = 20
        valid_product = True
    case "H":
        product_name = "Headphones"
        unit_price = 60
        valid_product = True
    case _:
        valid_product = False
        print("Xəta: Naməlum məhsul kodu! Yalnız böyük K, M və ya H qəbul olunur.")

if valid_product:
    qty_input = input("Miqdarı daxil edin (1-5): ")
    
    if len(qty_input) == 0 or not qty_input.isdigit():
        print("Xəta: Miqdar boş ola bilməz və yalnız rəqəmlərdən ibarət olmalıdır!")
    else:
        quantity = int(qty_input)
        
        if not (1 <= quantity <= 5):
            print("Xəta: Miqdar yalnız 1 ilə 5 arasında ola bilər!")
        else:
            coupon = input("Kupon kodunu daxil edin (NONE və ya SAVE10): ")
            
            if coupon != "NONE" and coupon != "SAVE10":
                print("Xəta: Yanlış kupon kodu! Yalnız NONE və ya SAVE10 qəbul olunur.")
            else:
                subtotal = unit_price * quantity
                
                if coupon == "SAVE10" and subtotal < 100:
                    print("Xəta: SAVE10 kuponu yalnız alt-cəmi 100 AZN və ya daha çox olan sifarişlərə tətbiq edilir!")
                else:
                    delivery_code = input("Çatdırılma kodunu daxil edin (P - Pickup, S - Standard): ")
                    
                    match delivery_code:
                        case "P":
                            delivery_name = "Pickup"
                            valid_delivery = True
                        case "S":
                            delivery_name = "Standard"
                            valid_delivery = True
                        case _:
                            valid_delivery = False
                            print("Xəta: Yanlış çatdırılma kodu! Yalnız P və ya S qəbul olunur.")
                    
                    if valid_delivery:
                        discount = (subtotal * 0.10) if coupon == "SAVE10" else 0
                        discounted_subtotal = subtotal - discount
                        
                        if delivery_code == "P":
                            delivery_fee = 0
                        else:
                            delivery_fee = 0 if discounted_subtotal >= 80 else 5
                        
                        final_total = discounted_subtotal + delivery_fee
                        
                        print("\n--- Sifariş Qəbzi ---")
                        print("Məhsul:", product_name)
                        print("Miqdar:", quantity)
                        print("Alt-cəmi:", subtotal, "AZN")
                        print("Endirim:", discount, "AZN")
                        print("Çatdırılma növü:", delivery_name)
                        print("Çatdırılma haqqı:", delivery_fee, "AZN")
                        print("Yekun məbləğ:", final_total, "AZN")

############################################
#TASK25

