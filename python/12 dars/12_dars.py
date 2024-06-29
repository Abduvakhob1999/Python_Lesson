# name = "salom"
# name.upper()
# name.lower()
# name.capitalize() #har bir gapni 1 harfini kotta qiladi
# name.title() #har bir so'zi 1 harfi kotta qiladi

# print(name.upper())
# print(name.lower())
# print(name.capitalize())
# print(name.title())


# gamer = [2, 4, 6, 8, 10]
# x,y haqiqiy sonlari berilgan. Ularning kichigini sonlar 
# yig’indisining yarmiga, kattasini
# ko’paytmasining ikkilanganiga almashtiruvchi programma tuzilsin. 
# Agar sonlar teng
# bo'lsa, o'zgarishsiz qoldirilsin.

# x = int(input("x son kiriting"))
# y = int(input("y son kiriting"))
# z = 0

# if x < y:
#     z = x
#     b = y
#     b = (x + y) / 2
#     z = (x * y) * 2
# elif x > y:
#     z = y
#     b = x
#     z += (x + y) / 2
#     b += (x * y) * 2
# else:
#     z = x
#     b = y
# print(z, b)

# Yil berilgan (musbat butun son). Berilgan yilda nechta kun 
# borligini aniqlovchi
# programma tuzilsin. Kabisa yilida 366 kun bor, 
# kabisa bo’lmagan yilda 365 kun bor.
# Kabisa yil deb 4 ga karrali yillarga aytiladi. 
# Lekin 100 ga karrali yillar ichida faqat 400
# ga karrali bo’lganlari kabisa yil hisoblanadi. 
# Masalan 300, 1300 va 1900 kabisa yili
# emas. 1200 va 2000 kabisa yili
# import datetime
# yil = int(input("yil kiriting"))
# result = 0
# result = yil
# if (yil % 4 == 0 and result % 100 != 0) or (yil % 400 == 0):
#     print(f"{result} berilgan son kabisa")
# else:
#     print(f"{result} berilgan son kabisamas")
    
# Uchta son berilgan. 
# Shu sonlarning kichigini aniqlovchi programma tuzilsin.

# x = int(input("son kiriting"))
# c = int(input("son kiriting"))
# y = int(input("son kiriting"))
# while True:
#     if x > y:
#         x = y
#         if x > c:
#             x = c
#             print(x)
#             break
#         else:
#             print(x)
#             break
#     else:
#         print(x)
#         break

# 6.N natural soni berilgan.
#  Shu songacha bo’lgan tub sonlarni chiqaruvchi programma


# a, *b, c = [1, 2, 3, 4, 5]
# print(b)

# Ikkita butun son berilgan Day (kun) va Month (oy). 
# (Kabisa bo`lmagan yil sanasi
# kiritiladi). Berilgan sanadan keyingi sanani ifodalovchi programma
# tuzilsin.

# x = int(input("month kiriting"))
# y = int(input("month kiriting"))

# z = {"month":0, "day":0}
# z["month"] = x + 1
# z["day"] = y + 12
# print(z)

# 8.While15. Bankka boshlang’ich Summa so’mda qo’yildi.
# Har oyda bor bo’lgan summa p
# foizga oshadi (0 < p < 12 ). Necha oydan keyin boshlang’ich qiymat 
# 2 martadan ko’p
# bo’lishini hisoblovchi programma tuzilsin. Necha 
# oy k – butun son. Bankda hosil
# bo’lgan summa haqiqiy son ekranga chiqarilsin.

# summa = int(input("summa kiriting: >>"))
# p = int(input("foizni kiriting: >>"))
# k = 0
# result = 0
# while True:
#     if summa != 0:
#         result += (summa / 100 * p)
#         k += 1
#         if result >=  summa * 2:
#             break
#     else:
#         print("pul kiriting")
# print(k)

# N natural soni berilgan. Shu songacha bo’lgan mukammal 
# sonlarni chiqaruvchi
# programma tuzilsin. O`zidan boshqa bo’luvchilari 
# yig’indisi o’ziga teng bo’lgan son
# mukammal son deyiladi. Masalan: 6, 28

# x = int(input("son kiriting: "))
# n = 1
# jovop = 0
# while x >= n:
#     if x % n == 0:
#         jovop += n
#         n += 1
#         if jovop == x:
#             print(f"berilgan {jovop} ")

# N natural soni berilgan. Shu songacha bo’lgan tub sonlarni 
# chiqaruvchi programma
# tuzilsin

