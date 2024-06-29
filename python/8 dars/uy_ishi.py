# Vazifa: Foydalanuvchidan bir son kiriting. For tsikli yordamida shu sonning ko'paytirish jadvalini 10 gacha chop eting.
# Misol:
# Foydalanuvchi Kirishi: 3
# Chiqish: "3 x 1 = 3, 3 x 2 = 6, ..., 3 x 10 = 30"
# Ro'yxatni Ikki Baravar Ko'paytirish:

# son = int(input("son kiriting: >>>"))
# for i in range(1, 10):
#     print(f"{son} * {i} = {son * i}")


#2- Vazifa: Sonlar ro'yxatini yarating. For tsikli yordamida har bir sonni 
# ikki baravar ko'paytirilgan yangi ro'yxat yarating.
# Misol:
# Asl Ro'yxat: [1, 2, 3]
# Chiqish: "Ikki Baravar Ko'paytirilgan Ro'yxat: [2, 4, 6]"
# Belgi Sanog'i:

# royxat = [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
# yengi_royxat = []
# for i in royxat:
#     yengi_royxat.append(i * 2)
# print("Asl Ro'yxat: ", royxat)
# print("Ikki Baravar Ko'paytirilgan Ro'yxat:", yengi_royxat)

# 3- Vazifa: Foydalanuvchidan bir matn kiriting. 
# For tsikli yordamida matndagi belgilar sonini sanab, natijani chop eting.
# Misol:
# Foydalanuvchi Kirishi: "Hello"
# Chiqish: "'Hello' matnida 5 ta belgi bor."
# Juft Sonlarni Filtrlash:

# text = input("Matn kiriting: >>>")
# belgilar_soni = 0
# for i in text:
#     belgilar_soni += 1
# print(f"{text} matinida {belgilar_soni} ta belgi bor")

# Vazifa: Sonlar ro'yxatini yarating. 
# For tsikli yordamida faqat juft sonlarni o'z ichiga olgan yangi ro'yxat yarating.
# Misol:
# Asl Ro'yxat: [1, 2, 3, 4, 5]
# Chiqish: "Juft Sonlar: [2, 4]"

# Asl_royxat = [32, 33, 54, 55, 65, 23, 11, 37, 10, 15, 16]   
# juft = []

# for i in Asl_royxat:
#     if i % 2 == 0:
#         juft.append(i)
# print(juft)


# Vazifa: Foydalanuvchidan bir son kiriting. For tsikli yordamida shu sonning ko'paytirish jadvalini 10 gacha chop eting.
# Misol:
# Foydalanuvchi Kirishi: 3
# Chiqish: "3 x 1 = 3, 3 x 2 = 6, ..., 3 x 10 = 30"
# Ro'yxatni Ikki Baravar Ko'paytirish:


son = int(input("son kiriting"))
for i in range(1, 11):
    son * i
    print(f"{son} * {i} = {son * i}")


