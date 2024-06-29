#1st class function -> bir funksiya boshqa funksiyani argument sifatida qabul qilishi

# def add(x, y):
#     return x + y

# def sub(x, y):
#     return x - y

# def calculator(add, x, y):
#     return add(x, y)

# result = calculator(add, 10, 20)
# print(result)

#-------------------------------------------------------------------------------------

#Nested function = funksiya ichida funksiya
# python closure = funksiya ichida funksiya qaytarish

# def  tashqi(n):
#     def ichki(num):
#         print(num ** n)
#     return ichki

# result = tashqi(2)
# result(5)
# result(4) #result == def ichki()
# result(6)


# # check ahe decorator
# def check_age(func):
#     def checking(name, age):
#         if age > 18:
#             func(name, age)
#         else:
#             print("siz yoshsiz")
#     return checking

# @check_age
# def  passport(name, age):
#     print(name, age)

# @check_age
# def  driving_l(name, age):
#     print(name, age)

# @check_age
# def  diplom(name, age):
#     print(name, age)

# diplom("Ali", 28)
# diplom("Ali", 19)
# diplom("Ali", 11)

# def cheker(func):
#     def chaking(name):
#         if len(name) < 50:
#             func(name)
#         else:
#             print("ismingiz juda uzun")
#     return chaking



# @cheker
# def creat_diplom(name):
#     print(name)

# @cheker
# def creat_passport(name):
#     print(name)

# creat_diplom(input("isim kirgiz"))
# # creat_passport("Assssssssssssssssssssssssssssssssssssssssssaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaakkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


# def tekshiruv(func):
#     def tekshiruv_bot(name, age):
          

# password = "12345aaa"
# x = input("passwoerd kirg'iz").lower()
# if password == x:
#     print("Xush kelipsiz")
# else:
#     print("")


# x = 10
# y = 20
# print(x < y)
# print(x + 15 < 20 + y)
# print(True == 1)

# x = "ext ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."
# x = x.title()
# print(x)

# y = "ext ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. "
# y = y.capitalize()
# print(y)
# x = y.count("1")
# print(x)
# x = y.split(",")
# print(x)


# def qoldig(son):
#     if son % 2 == 0:
#         return "son juft"
#     else:
#         return "son toq"
# x = qoldig(100)
# print(x)



matn = """Where does it come from?
        Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32.
        The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32 and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form, accompanied by English versions from the 1914 translation by H. Rackham"""

def  matn_func():
    sonlar = 0
    for i in matn:
        try:
            int(i)
            sonlar += 1
        except:
            pass
    print(sonlar)


