# += ,-= , !=

# a = 3 
# a += 3 # a = a + 3 
# a -= 3 # a = a - 3 
# a *= 3 # a = a - 3 
# a != 3 # a = a - 3 


# number = 1
# while number <= 100:
#     print(number)
#     number += 1
# print("tugadi")

# is_true = False
# secret = 7
# while is_true == True:
#     guess = int(input("taxmin kirg'izin"))
#     if guess == secret:
#         print("topdingiz")
#         is_true = True
#     elif guess < secret:
#         print("kattaroq son kirit")
#     elif guess > secret:
#         print("kichikroq son")

# xarakat = 1
# yegindi = 0
# while xarakat <= 10:
#     raqam = int(input("raqam"))
#     yegindi += raqam
#     xarakat += 1
# print(yegindi)


# sonlar = 1
# yegindi = 0
# while sonlar <= 5:
#     raqam = int(input("son"))
#     yegindi += raqam
#     sonlar += 1 
# print(raqam / 5)

#uy vazifasi
    
#  1) Raqamlarni hisoblash:
# Foydalanuvchidan raqam kiritishini so'rang va 
# keyin 1 dan shu raqamgacha bo'lgan barcha raqamlarni chop etish uchun while tsiklidan foydalaning.    

# y = 0
# x = int(input("son kirgizin"))
# while y < x:
#     y += 1
#     print(y)
    
# 2) Raqamlar yig'indisi:
# 1 dan 10 gacha bo'lgan barcha raqamlarning yig'indisini 
# hisoblash va natijani chop etish uchun while tsiklidan foydalaning. 

# x = 1
# y = 0
# while x <= 10:
#     x += 1
#     y += x
#     print(y)


# 3) Asosiy parol tekshiruvi:
# Oldindan belgilangan parolni o'rnating. Foydalanuvchidan parolni to'g'ri qabul qilmaguncha 
# doimiy ravishda kiritishni so'rang. To'g'ri parol kiritilgandan so'ng, xush kelibsiz xabarni chop eting.

# password = 12345
# its_true = False
# while its_true == False:
#     password_user = int(input("parol kiriting"))
#     if password_user == password:
#         print("xush kelibsiz")
#         its_true = True
#     else: 
#         print("yana urinib koring")

# 4) Ortga hisoblash taymeri:
# Foydalanuvchidan raqam kiritishini so'rang, so'ngra 
# bu raqamdan 0 gacha bolgan sonlarni ekranga chiqarib berish uchun  uchun while tsiklidan foydalaning.

# son = int(input("son kiriting"))
# x = 0
# while son >= x:
#     print(son)
#     son -= 1

# yosh = int(input("yoshingiz nechida?"))
# while yosh >= 18 and yosh <= 60:
#     print("sizni yoshingiz togri keladi")
#     if yosh < 18:k
#         print("sizni yoshingiz kichkina")
#     elif yosh > 60:
#         print("sizmi yoshingiz juda kotta")
#     break
    


# while  True:
#     yosh = int(input("yosh"))
#     if yosh < 18:
#         print("sizni yoshingiz kichik")
#     elif yosh > 60:
#         print("sizni yoshingiz juda katta")
#     else:
#         print("sizni yoshingiz tog'ri keladi")
#         break
        
# Raqamlar yig'indisi:
# 1 dan 10 gacha bo'lgan barcha raqamlarning yig'indisini hisoblash va natijani chop 
# etish uchun while tsiklidan foydalaning. 


# Exercise 2: Factorial Calculator
# Write a Python program that calculates the factorial of a number entered by the user using a while loop. The factorial of a non-negative integer n, denoted in mathematics as n!, is the product of all positive integers from 1 to n. For example, 
# 5! (read as "5 factorial") is equal to 5 * 4 * 3 * 2 * 1, which is 120.

# y = 0
# x = int(input("son kirit: "))
# while x > 0:
#     y += x
#     x -= 1
#     print(y)

#3-mashq: Parol tekshiruvi
# Oddiy parol tekshirgichni simulyatsiya qiluvchi Python dasturini yozing.
#Dastur foydalanuvchidan parolni kiritishni so'rashi va to'g'ri parolni kiritmaguncha 
#so'rashni davom ettirishi kerak. To'g'ri parol kiritilgandan
# so'ng, dastur muvaffaqiyatli xabarni chop etishi kerak

# password = 12345
# while True:
#     x = int(input("parolni kiriting"))
#     if password == x:
#         print("Hush kelibsiz")
#     else:
#         print("qaytadan urinib ko'rin")

# 4-mashq: Pawword Checker Davomi
# Maksimal urinishlar sonini qo'shish orqali oldingi parol tekshiruvi misolini kengaytiramiz. 
# Agar foydalanuvchi maksimal urinishlar sonidan oshib ketgan bo'lsa, dastur ularni bloklashi kerak

# password = "12345"
# urunish_soni = 3
# urinish = 0
# while urinish < urunish_soni:
#     user_input = input("passport kiriting")

#     if user_input == password:
#         print("Hush kelibsiz")
#         break
#     else:
#         urinish += 1
#         xato_urinishlar = urunish_soni - urinish
#         if xato_urinishlar > 0:
#             print(f"sizda {xato_urinishlar} imkonyatingiz qoldi")
#         else:
#             print("siz bloklandiz")
    
juft_sonlar = 0
toq_sonlar = 0
x = 1
while x <= 5:
    son = int(input("son kiriting"))
    if son % 2 == 0:
        juft_sonlar += son
    else :
        toq_sonlar += son
    x += 1   
print(f"juft sonlar : {juft_sonlar} \n toq sonlar : {toq_sonlar} ")





