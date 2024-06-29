# # number = ["python" , 2 , 3, 4, 5, 22]
# number = ["python" , "js" , "c" , "php"] 
# # foo = number[0:3:1] # [boshlanishi : tugashi : qadam]
# number.append("Java") # qoshadi 
# print(number)
# number.pop(1) # index boyicha ochirish
# print(number)
# number.remove("c") # qiymat bo'yicha ochirish
# print(number)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# jami = sum(numbers)

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = numbers.append(11)
# print(a)
# for x in numbers:
#     print(x)
# print(numbers)

# print(numbers[0])

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# jammi = 0
# list_uchun_harakat = 0
# while list_uchun_harakat < 10:
#     if numbers[list_uchun_harakat] % 2 == 0:
#         jammi += numbers[list_uchun_harakat]
#     list_uchun_harakat += 1
# print(jammi)

# numbers = tuple(range(2, 11, 2))
# print (numbers)

# for x in numbers:
#     print(x)


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = 0

# while b < len(a):
#     if a[b] % 2 != 0:
#         print(a[b])
#     b = b + 1

# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = 0

# while b < len(a):
#     if a[b] % 2 == 0:
#         print(a[b])
#     b = b + 1


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = 0


# while b < len(a):
#     if a[b] % 2 != 0:
#         print(a[b])
# #     b = b + 1

# a = int(input("son kiriting"))
# b = 0
# while b < 0:
#     if a % 2 == 0:
#         print("qoldiqsiz bo'linadi")
#     else:
#         print("qoldiqli bo'linadi")
            
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = 0
# # t = a[b]
# # print(t)
# while b < len(a):
#     if a[b] % 2 != 0:
#         print(a[b])
#     b = b + 1

x = 0
number = int(input("son kirg'izing"))
while x < 100:
    if number % 2 == 0:
        print("siz kirg'izgan soningiz juft")
    else:
        print("siz kirg'izgan soningiz toq")