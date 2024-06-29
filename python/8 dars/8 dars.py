# # numbers = [1, -2, -5, 7]
# # len(numbers)  #uzunligini sanaydi
# # min(numbers) #eng kichik soni topadi
# # max(numbers)  # eng katta soni topadi
# # sum(numbers)  # sonlar yegindisini topadi

# # numbers = [1, 2, 3, 4, 5]

# # juft_sonlar = 0
# # for num in numbers:
# #     if num % 2 == 0:
# #         juft_sonlar += 1
# # print(juft_sonlar)


# #3 - Vazifa: Sonlar ro'yxatini yarating. Ro'yxatdagi musbat sonlarni nechta ekanligini 
# # while tsikli yordamida sanang.
# # Misol:
# # Ro'yxat: [-1, 3, 5, -2, 9]
# # Chiqish: "Ro'yxatda 3 ta musbat son bor."
# # Ro'yxat Elementlarini Teskarisiga Aylantirish:

# # numbers = [-1, 3, 5, -2, 9]
# # musbat_sonlar = 0
# # for num in numbers:
# #     if num > 0:
# #         musbat_sonlar += 1

# # print(musbat_sonlar)


# # 4- Vazifa: Sonlar ro'yxatini yarating. While tsikli yordamida 
# # ro'yxatdagi eng kichik qiymatni toping va uni chop eting.
# # Misol:
# # Ro'yxat: [4, 2, 7, 1, 9]
# # Chiqish: "Ro'yxatdagi eng kichik qiymat 1."

# # royxat = [33, 55, 22, 31, 43, 1, 3]
# # eng_kichik_son = 999
# # for num in royxat:
# #     if eng_kichik_son > num:
# #         eng_kichik_son = num
# # print(eng_kichik_son)

# # alph = ["a", "o", "u", "e", "i"]
# # name = "python"
# # for char in name:
# #     if char in alph:
# #         print(char)

# # name = input()
# # if name == name[::-1]:
# #     print("palindrome")
# # else:
# #     print("not palindrome")

# # text = "2 haftada 2 ta imtixon bor 2"
# # x = "2"
# # y = 0
# # for num in text:
# #     if x == num:
# #         y += 1
# # print(y)

# # a = [[9,6],2,3]
# # print(a[0][1])

# # sum = [
# #     [1, 2, 3], 
# #     [4, 5, 6],
# #     [7, 8, 9],
# # ]
# # print(sum[0][2])
# # print(sum[1][1])
# # print(sum[2][0])

# # import random
# # print(random)
# # a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # for num in a:
# #     print(num)

# # sum = [
# #     [1, 2, 3], 
# #     [4, 5, 6],
# #     [7, 8, 9],
# # ]
# # for i in range(len(sum)):
# #     for j in range(len(sum)):
# #         print(sum[i][j], end=(''))

# #     print()

# # a = int(input("Nechta son kiritish kerak?"))
# # num = []
# # for i in range(a):
# #     nums = int(input("son yozing >>>"))
# #     num.append(nums)
# #     print("raqamlar ro'yhati", num)


# # import random
# # def  decor(func):
# #     def wrapper():
# #         print("Said ali Aka, dekoretorsiz qildim")
# #         while True:
# #             func()
# #             print("Qaytadan o'ynaysizmi ?")
# #             repeater = int(input("Ha: 1>>>,\nYo'q: 2"))
# #             if repeater == 1:
# #                 func()
# #             else:
# #                 print("Hayir")
# #                 break
# #     return wrapper

# # @decor
# # def solishtirish():
# #     z = random.randint(1, 10)
# #     while True:
# #         x = int(input("1 son kirit"))
# #         if x == z:
# #             print(f"topdingiz, to'gri jovop {z}")
# #             break
# #         else:
# #             print("yana urinib koring")
# # solishtirish()


# # import random

# # def decor(func):
# #     def wrapper():
# #         print("Said ali Aka, dekoretorsiz qildim")
# #         while True:
# #             func()
# #             print("Qaytadan o'ynaysizmi ?")
# #             repeater = int(input("Ha: 1>>>,\nYo'q: 2"))
# #             if repeater == 1:
# #                 func()
# #             else:
# #                 print("Hayir")
# #                 break
# #     return wrapper

# # @decor
# # def solishtirish():
# #     z = random.randint(1, 10)
# #     while True:
# #         x = int(input("1 son kirit"))
# #         if x == z:
# #             print(f"topdingiz, to'gri jovop {z}")
# #             break
# #         else:
# #             print("yana urinib koring")

# # solishtirish()

class Students:
    def  __init__(self, name, surname, age:int):
        self.gruppa_U_1_24 = ["Bayram, Azamat, Otabek, Aziz, Iftihor, Jalol, Miraziz"]
        self.gruppa_U_2_24 = ["Saidali, Abduvohob, Nurbek, Azim, Nurulloh, Jovohir, Asadulloh, Nodirbek"]

        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
         return f"{self.name},\n{self.surname},\n{self.age}"
    
    def grup(self):
        if self.name in self.gruppa_U_1_24: # in ishlamayapti
            return self.gruppa_U_2_24
        elif self.name in self.gruppa_U_2_24:
            return self.gruppa_U_1_24
student1 = Students("Abduvohob", "Zuhriddinov", 25)
print(student1)
print(student1.grup())         