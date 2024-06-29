#1--Vazifa: Sonlar ro'yxatini yarating. Ro'yxatdagi juft sonlarni nechta ekanligini 
# while tsikli yordamida sanang.
# Misol:
# Ro'yxat: [2, 5, 8, 3, 10]
# Chiqish: "Ro'yxatda 3 ta juft son bor."
# Birinchi N ta Sonning Yig'indisi:

# sonlar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# juft_sonlar = 0
# juft_sonlar_yegindisi = 0
# harakat = 0
# while harakat < len(sonlar):
#     if sonlar[harakat] % 2 != 1:
#         juft_sonlar += 1
#         juft_sonlar_yegindisi += sonlar[harakat]
#     harakat += 1
# print(f"Sonlar to'plamida: {juft_sonlar} juft sonlar bor \n Ularni yeg'indis: {juft_sonlar_yegindisi} ga teng")


#2 - Vazifa: Foydalanuvchidan N sonini kiriting. While tsikli yordamida 
# birinchi N ta sonning (1 dan N gacha) yig'indisini hisoblang va natijani chop eting.
# Misol:
# Foydalanuvchi Kirishi: 5
# Chiqish: "Birinchi 5 ta sonning yig'indisi 15."
# Musbat Sonlar Soni:

# son = int(input("son kiriting"))
# toplam = []
# toplam = list(range(1, son + 1))
# harakat = 0
# sonlar_yegindisi = 0
# musbat_sonlar = 0
# while harakat < len(toplam):
#     if son > 0:
#         musbat_sonlar += 1
#     sonlar_yegindisi += toplam[harakat]
#     harakat += 1
# print(f"Birinchi {son} ta sonning yig'indisi {sonlar_yegindisi}.")
# print(f"Musbat Sonlar Soni: {musbat_sonlar}")

# 2 - yechim

# son = int(input("son kiriting"))
# x = 0
# y = 0 
# while son > 0:
#     if son > 0:
#         x += son
#         if son > 0:
#            y += 1 
#     son -= 1
# print(f"Birinchi {son} ta sonning yig'indisi {x}")
# print("Musbat Sonlar Soni:" , y)

# 3 - yechim 

# son = int(input("son kiriting"))
# index = 0
# yegindi = 0
# musbat = 0
# if son > 0:
#     while index < son:
#         if index < son:
#             yegindi += index
#             if son > 0:
#                 musbat += 1 
#         index += 1
# else: 
#     while son < 0:
#         yegindi += son
#         son += 1
#         musbat = 0

# print(f"Birinchi {son} ta sonning yig'indisi {yegindi}")
# print("Musbat Sonlar Soni:" , musbat)


#3 - Vazifa: Sonlar ro'yxatini yarating. Ro'yxatdagi musbat sonlarni nechta ekanligini 
# while tsikli yordamida sanang.
# Misol:
# Ro'yxat: [-1, 3, 5, -2, 9]
# Chiqish: "Ro'yxatda 3 ta musbat son bor."
# Ro'yxat Elementlarini Teskarisiga Aylantirish:

# harakat = 0
# musbat_sonlar = 0
# teskari_toplam = []
# toplam = [-1, -3, 2, 100, 200, 25, -109, 26, 44, -256, 123, -91]
# while harakat <= 11:
#     if toplam[harakat] > 0:
#         musbat_sonlar += 1
#     harakat += 1
# # toplam.reverse()  


# print(f"Ro'yxatda {musbat_sonlar} ta musbat son bor.")
# print("Ro'yxat Elementlarini Teskarisiga Aylantirish:", toplam) #toplam[::-1]

#4- Vazifa: Sonlar ro'yxatini yarating. While tsikli yordamida 
# ro'yxatdagi eng kichik qiymatni toping va uni chop eting.
# Misol:
# Ro'yxat: [4, 2, 7, 1, 9]
# Chiqish: "Ro'yxatdagi eng kichik qiymat 1."

# # 1- yechim
# toplam = [99, 22, 44, 52, 65, 76, 32, 99 ,48, 84, 71, 53]
# toplam.sort()
# print(toplam[0])

# 2 - yechim while bilan
# toplam = [99, 55, 44, 52, 65, 76, 32, 99 ,48, 84, 71, 53]
# eng_kick_son = toplam[0]
# harakat = 1
# while harakat < len(toplam):
#     if eng_kick_son > toplam[harakat]:
#         eng_kick_son = toplam[harakat]
#     harakat += 1
# print(f"eng kick son: {eng_kick_son}")

# 3 - yechim 
# numbers = [22, 3, 8, 9, 11]

# min_nuber = 99999
# index = 0
# while index <= 4:
#     if numbers[index] < min_nuber:
#         min_nuber = numbers[index] 
#     index += 1
# print(min_nuber)