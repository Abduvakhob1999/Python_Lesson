#1 Uchta son beifrilgan. Shu sonlarning kichigini aniqlovchi programma tuzilsin.



# def eng_katta(birinchi, ikkinchi, uchinchi):
#     x = 0
#     while True:
#         if birinchi > x:
#             x = birinchi
#             if x > ikkinchi:
#                 x = ikkinchi
#                 if x > uchinchi:
#                     x = uchinchi
#         return x
# a = eng_katta(4, 6, 10)
# print(a)

#2 Yil berilgan (musbat butun son). Berilgan yilda nechta kun borligini aniqlovchi
# programma tuzilsin. Kabisa yilida 366 kun bor, kabisa bo’lmagan yilda 365 kun bor.
# Kabisa yil deb 4 ga karrali yillarga aytiladi. Lekin 100 ga karrali yillar ichida faqat 400
# ga karrali bo’lganlari kabisa yil hisoblanadi. Masalan 300, 1300 va 1900 kabisa yili
# emas. 1200 va 2000 kabisa yili.
# def kabisa(son):       
#     son = int(input("yil kiriting: "))
#     if son % 4 == 0 and son % 100 == 0:
#         if son % 400 == 0:
#             print("berilgan yil kabisa")
#         else:
#             print("Berilgan yil kabisa emas")
#     else:
#         print("Berilgan yil kabisa emas")
# a = kabisa(2000)


# 3.x,y haqiqiy sonlari berilgan. Ularning kichigini sonlar yig’indisining yarmiga, kattasini
# ko’paytmasining ikkilanganiga almashtiruvchi programma tuzilsin. Agar sonlar teng
# bo'lsa, o'zgarishsiz qoldirilsin.

# def sonlar(son1, son2):
#     if son1 < son2:
#         son1 = (son1 + son2) / 2
#         son2 = (son1 * son2) * 2
#         return son1, son2
#     else:
#         son1 = (son1 * son2) * 2
#         son2 = (son1 + son2) * 2
#         return son1, son2
# print(sonlar(2, 4))

#4) Ikkita butun son berilgan Day (kun) va Month (oy). (Kabisa bo`lmagan yil sanasi
# kiritiladi). Berilgan sanadan keyingi sanani ifodalovchi programma tuzilsin.

# def san(son):
#     if son % 4 == 0 and son % 100 != 0:
#         if son % 400 != 0:
#             return "Kabisa yili"
#         else:
#             return "Kabisa yilli emas"
#     else:
#         return "kabisa yilli emas"
    
# print(san(2024))
    
#5) N natural soni berilgan. Shu songacha bo’lgan mukammal sonlarni chiqaruvchi
# programma tuzilsin. O`zidan boshqa bo’luvchilari yig’indisi o’ziga teng bo’lgan son
# mukammal son deyiladi. Masalan: 6, 28

# def mukammal_son(son):
#     # # y = []
#     # # for i in range(1 , son):
#     # #     if son % i == 0:
#     # #         y.append(i)
#     y = [i for i in range(1, son) if son % i == 0]
#     if sum(y) == son:
#         return "Bu mukammal son"
#     else:
#         return "bu mukammal son emas"
# print(mukammal_son(6))

# 6. N natural soni berilgan. Shu songacha bo’lgan tub sonlarni chiqaruvchi programma
# tuzilsin.

# def tub_sonlar(son):
#     x = [i for i in range(1, son) if son % i == 0]
# #     if len(x) < 2:
# def son_deko(func):
#     def wrapper(string):
#         y = func(string)
#         return func
#     return wrapper

# @son_deko
# def foo(string):
#     try:
#         x = [i for i in string if int(i)]
#     except:
#     return x
     

# print(foo("123edjfwcij439h294fojfj"))


# 7. N natural soni berilgan. N gacha bo’lgan do’st sonlarni 
# chiqaruvchi programma tuzilsin.
# Agar birinchi son bo’luvchilari yig’indisi ikkinchi songa, 
# ikkinchi son bo’luvchilari
# yig’indisi birinchi songa teng bo’lsa, bu sonlar do’st sonlar deyiladi.

# x = int(input("son kirit: >>>"))
# y = int(input("son kirit: >>>"))
# a = [i for i in range(1, x + 1) if i % 2 == 0]
# b = [i for i in range(1, y + 1) if i % 2 == 0]
# c = lambda()-