# # # Kiritish: Foydalanuvchidan gap kiritishni so'rang.
# # # So'zlar Soni: Gapdagi so'zlarning umumiy sonini hisoblang.
# # # Eng Uzun So'z: Gapdagi eng uzun so'zni toping va chiqaring.
# # # Eng Qisqa So'z: Gapdagi eng qisqa so'zni toping va chiqaring.
# # # O'rtacha So'z Uzunligi: Gapdagi so'zlarning o'rtacha uzunligini 
# # # hisoblang va chiqaring.
# # # Takrorlanmas So'zlar: Gapda ishlatilgan barcha takrorlanmas so'zlar 
# # # ro'yxatini chiqaring (harf katta-kichikligiga e'tibor bermasdan). 
# # #  Iltimos, gap kiriting: Tezkor jigarrang tulki dangasa it ustidan sakrab o'tdi.

# # So'zlar soni: 8
# # Eng uzun so'z: jigarrang
# # Eng qisqa so'z: it
# # O'rtacha so'z uzunligi: 5.25
# # Takrorlanmas so'zlar: ['tezkor', 'jigarrang', 'tulki', 'dangasa', 'it', 'ustidan', 'sakrab', 'o'tdi']

# # def gap():
# #     gap = input("Gap kiriting: ")
# #     gap = gap.split()
# #     return gap


# # def eng_uzun():
# #     sozlar = gap()
# #     eng_uzun = sozlar[1]
# #     for i in sozlar:
# #         eng_uzun.len() > i.len()
# #         eng_uzun = i
# #     return eng_uzun

# # def eng_qissqa():
# #     sozlar = gap()
# #     eng_qissqa = sozlar[1]
# #     for i in sozlar:
# #         eng_qissqa.len() > i.len()
# #         eng_qissqa = i
# #     return eng_qissqa

# # def ortacha():
# #     sozlar = gap()
# #     ortacha = 0
# #     for i in sozlar:
# #         ortacha += i.len()
# #     return ortacha.len() / sozlar.len()


# # def takrorlanmas():
# #     sozlar = gap()
# #     takrorlanmas = []
# #     for i in sozlar:
# #         i in takrorlanmas
# #         takrorlanmas.append[i]
# #     return takrorlanmas


# # def menu():
# #     print()
# #     gap_ozi = gap()
# #     eng_qissqa_soz = eng_qissqa()
# #     eng_uzun_soz = eng_uzun()
# #     ortacha_soz = ortacha()








# # fayl ichidagi juft sonlar nechtaligi
# # fayl ichidagi toq sonlar nechtaligi
# # fayl ichidagi juft sonlar yig'indisi
# # fayl ichidagi toq sonlar yig'indisi


# # fayl = open("text.txt", "w")
# # fayl.write("121234r5365yerffrghyjukiloiuy424546575645321")
# # fayl.close()

# # fayl = open("text.txt", "r")
# # fayl_read = fayl.read()
# # sonlar = []

# # try:
# #     for i in fayl_read:
# #         sonlar.append(int(i))
     

# # except:
# #     pass

# # toq_sonlar = [i for i in sonlar if i % 2 == 0]
# # juft_sonlar = [i for i in sonlar if i % 2 == 1]
# # fayl.close()

# # print(toq_sonlar)
# # print(juft_sonlar)
# # print(sum(toq_sonlar))
# # print(sum(juft_sonlar))


# 1. Игра угадайки:

# Напишите программу, которая генерирует случайное число между 1 и 100 (используйте модуль random).
# Создайте цикл (for или while), который позволяет пользователю угадать число.
# После каждой попытки предоставьте подсказку (например, "Слишком много!" или "Слишком мало!").
# Если пользователь угадает правильно, выведите поздравительное сообщение и количество попыток.
# Следите за количеством попыток с помощью переменной.

# import random

# def randomInt():
#     a = random.randint(1, 100)
#     c = 0
#     while True:
#         b = int(input("son kiriting"))
#         if b == a:
#             print(f"siz tog'ri topingiz,  siz urunishlaringiz soni {c}")
#             break
#         elif b > a:
#             print("kichikroq son kiriting")
#             c += 1
#         elif b < a:
#             print("kattaroq son kiriting")
#             c += 1
        
# randomInt()

# 2. Генераторы списков: 

# Напишите код, который создает список квадратов чисел от 1 до 10 с помощью цикла for.
# Теперь перепишите код, используя генератор списков для более лаконичного решения.

# kvadratlar = [i ** 2 for i in range(1, 11)]
# print(kvadratlar)

# 3. Проверка пароля:

# Напишите программу, которая запрашивает у пользователя пароль.
# Определите минимальную длину пароля и требования к сложности (например, прописные буквы, цифры, специальные символы).
# Используйте цикл while, чтобы продолжать запрашивать у пользователя пароль, пока не будут выполнены требования.
# Предоставьте конкретную обратную связь о том, чего не хватает введенному паролю.

# while True:
#     password = input("Parol kiriting")
#     simblyol = ["@", "#" , "$", "%", "^", ""]
#     if str in password:
#         if password.len() < 8:
#             if password in simblyol:
#                 print("parol tog'ri")
#             else:
#                 print("sybol ham qoshing")
#         else:
#             print("parollni uznligi 8 ta oshiq bo'lishi kerak")
#     else:
#         print("Harflar ham qo'shing")
# 4. FizzBuzz:

# Напишите код, который выполняет итерации от 1 до 100 (используйте цикл for).
# Для каждого числа печатайте "Fizz", если оно делится на 3, "Buzz", если оно делится на 5, и "FizzBuzz", если оно делится на 3 и на 5.
# В противном случае выведите само число.
# for i in range(1, 10 + 1):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
    
 
# 5. Анализатор текста:

# Напишите программу, которая запрашивает у пользователя предложение или абзац.
# Используйте цикл for для перебора каждого символа.
# Подсчитайте количество гласных, согласных, пробелов и знаков препинания.
# После цикла выведите отчет об анализе.
# Бонусное задание: Таблица умножения:

# Напишите программу, которая запрашивает у пользователя число (например, 7).
# Используйте вложенные циклы for, чтобы создать таблицу умножения для этого числа до указанного предела (например, 12).
# Выведите таблицу в отформатированном виде с четкими строками и столбцами.


# import time
# x1= time.time()
# x = range(1, 100)
# tubsonlar = []

# for i in x:
#     a = 0
#     for j in range(1, i):
#         if i % j == 0:
#             a += 1
#     if a < 2:
#         tubsonlar.append(i)
# print(tubsonlar)
# n = time.time()
# print(x1 , n)



# Topshiriq: So'z Tahlilchisi

# Maqsad: Foydalanuvchi kiritgan gapni tahlil qiluvchi va qiziqarli 
# ma'lumotlarni taqdim etuvchi Python dasturini yozing.

# Aniqliklar:

# Kiritish: Foydalanuvchidan gap kiritishni so'rang.
# So'zlar Soni: Gapdagi so'zlarning umumiy sonini hisoblang.
# Eng Uzun So'z: Gapdagi eng uzun so'zni toping va chiqaring.
# Eng Qisqa So'z: Gapdagi eng qisqa so'zni toping va chiqaring.
# O'rtacha So'z Uzunligi: Gapdagi so'zlarning o'rtacha uzunligini hisoblang va chiqaring.
# Takrorlanmas So'zlar: Gapda ishlatilgan barcha takrorlanmas so'zlar ro'yxatini chiqaring
# (harf katta-kichikligiga e'tibor bermasdan). 

# def  users():
#     user = input("soz kiriting: ")
#     userss = user.split()
#     uzunligi = len(userss)
#     eng_uzun = max(userss)
#     eng_kalta = min(userss)
#     o_uzunlik = sum(len(word) for word in userss)
#     y = o_uzunlik // len(userss)

    
#     # ortacha = x / uzunligi

#     print(f"Uzunligi  {uzunligi}")
#     print(f"Eng uzuni  {eng_uzun}")
#     print(f"Eng kaltasi  {eng_kalta}")
#     print(f"Ortacha uzunligi {y}")

#     # return uzunligi, eng_uzun, eng_kalta, y,


# x = users()
# # print(x)


# input.txt deb nomlangan faylni qator-qator o'qing.
# Har bir qatorda, qatorni katta harflarga o'zgartiring.
# Katta harflardagi qatorlarni yangi output.txt deb nomlangan faylga yozing.
# Bonus: Fayl operatsiyalari paytida yuz berishi mumkin bo'lgan istisnolarni boshqaring.

# file = open("input.txt", "w")
# file.write("abduvohob qalesan")
# file.close()
# file = open("input.txt", "r")
# x = file.read()
# y = x.upper()
# file2 = open("output.txt", "w")
# file2.write(y)
# file.close()
# file2.close()



# def pos_neg(a, b, negative):
#   if False:
#     return (a < 0 and b < 0)
#   else:
#     return ((1 < 0 and -1 > 0) or (1 > 0 and -1 < 0))
  
# x = pos_neg(1, -1, False)

# print(x)



