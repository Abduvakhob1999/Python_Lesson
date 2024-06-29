#1- Vazifa: Berilgan so'zlar ro'yxatida har bir so'zning 
# chastotasini hisoblang va natijalarni lug'atda saqlang.
# Misoli kirish: 
#     ["apple", "banana", "apple", "cherry", "banana", "cherry", "cherry"]
# Kutilgan chiqish: {'apple': 2, 'banana': 2, 'cherry': 3}

mevalar = ["apple", "banana", "apple", "cherry", "banana", "cherry", "cherry"]
natija = {}
for char in mevalar:
    if char in natija:
        natija[char] += 1
    else:
        natija[char] = 1
print(natija)

#2 -mashq O'quvchilar baholari kitobi:
# Vazifa: Har bir kalit o'quvchining ismi va qiymati ularning baholari 
# ro'yxati bo'lgan lug'at yarating. Keyin, ma'lum bir o'quvchi uchun yangi
# baho qo'shing.
# Misoli kirish: grades = {"Alice": [85, 90], "Bob": [78, 82]},
# Alice uchun 95 baho qo'shing.
# Kutilgan chiqish: {'Alice': [85, 90, 95], 'Bob': [78, 82]}


# bolalar_va_baxolar = {
#     "Olim":[4], "Avaz": [5], "Ahmad": [3],
#     "Asad": [5], "Jamshid": [4], "Abdulloh": [5],
#     "Jamoliddin": [3], "Aziza": [3], "Omina": [5],
#     "Shoxrux": [2], "Akbar": [4], "Saidali": [5] }
# for baho in bolalar_va_baxolar:
#     nazorat_ishi = int(input(f"{baho} bahosini kiriting: >>>"))
#     bolalar_va_baxolar[baho].append(nazorat_ishi)
# print(bolalar_va_baxolar)

#3-mashq Aloqa kitobi:
# Vazifa: Aloqa ma'lumotlarini saqlash uchun lug'at yarating. 
# Har bir kalit shaxsning ismi va qiymati ularning telefon raqami 
# bo'lishi kerak. Yangi aloqa qo'shing va mavjud aloqaning telefon 
# raqamini yangilang.
# Misoli kirish: contacts = {"John": "123-456-7890"}, 
# "Jane" nomli raqam bilan "987-654-3210" qo'shing va Johnning raqamini 
# "111-222-3333" ga yangilang.
# Kutilgan chiqish: {'John': '111-222-3333', 'Jane': '987-654-3210'}

# contacts = {"John": "123-456-7890"}
# contacts["Jane"] = "987-654-3210"
# contacts["John"] = "111-222-3333"


#4 - mashq Inventarizatsiya boshqaruvi:
# Vazifa: Elementlarning inventarizatsiyasini ifodalovchi 
# lug'at berilgan (element nomlari kalitlar va miqdorlari qiymatlar 
# bo'lishi kerak), ma'lum bir elementning miqdorini yangilang.
# Misoli kirish: inventory = {"apples": 10, "oranges": 8}, "apples" ni 5 ga
# ko'paytiring.
# Kutilgan chiqish: {'apples': 15, 'oranges': 

# inventory = {"apples": 10, "oranges": 8}
# user = input("Mevalar kiriting")
# value = input("qiymtni kiriting")
# if user in inventory:
#     inventory[user] = value
# else:
#     inventory[user] = value
# print(inventory)

#5 mashq Film reytingi:

# Vazifa: Film nomlari va ularning reytinglarini saqlash uchun lug'at yarating. Yangi film va uning reytingini qo'shing va mavjud filmning reytingini yangilang.
# Misoli kirish: movies = {"Inception": 8.8}, "The Matrix" filmi bilan 8.7 reytingda qo'shing va "Inception" reytingini 9.0 ga yangilang.
# Kutilgan chiqish: {'Inception': 9.0, 'The Matrix': 8.7}

# reyting = {"intersteller": 0, "seven": 0, "the dark knight": 0, "the god father": 0,
#            "the matrix":    0, "the shawshank redemption" :0, "dune" : 0,
#            "inception": 0, "last samurai": 0, "napoleon": 0, "oppenheimer": 0} 
# while True:
#     user = input("qaysi kino tanladingiz")
#     if user in reyting:
#         ball = int(input("balni kiriting"))
#         if ball > 0:
#             reyting[user] = ball
#             break
# print(reyting)

