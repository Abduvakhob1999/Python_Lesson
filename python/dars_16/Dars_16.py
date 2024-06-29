# Working with files
   

# r = read

# fayl ochish

# file = open("text.txt","r")  # text.txt file ochish kerak ishlashi uchun


# # fayl oqish

# text = file.read()
# print(text)

# # faylni yopish
# file.close()



# email = "john@gmail.com"
# email_splitted = email.split(".") #string ni ajratib beradi
# print(email_splitted)


# email = "john@gmail.com"
# foo = email.replace("j", "l")  #almashtirib qoyadi ochiribam tawasa boladi
# print(foo)


# blocked = ["mail.ru", "yahoo.com"]

# file = open("text.txt","r")

# lines = file.readline()
# for email in lines:
#     email = email.replace("\n","")
#     email_domain = email.split("@") [1]
#     if email_domain in blocked:
#         continue
#     else:
#         print(email)

# file.close()


# file = open("text.txt", "w")
# file.write(file)


# def count_numbers(filename):
#     file = open(filename, "r")

#     file_read = file.read()
#     file_num_count = 0
#     for char in file_read:
#         try:
#             int(char)
#             file_num_count += 1
#         except:
#             pass
#     return file_num_count
# file1_num_count = count_numbers("text.txt")
# file2_num_count = count_numbers("text2.txt")

# if file1_num_count > file2_num_count:
#     print("file1 da korproq raqam")
# elif file2_num_count < file2_num_count:
#     print("file2 da koproq raqam")
# else:
#     print("bir xil")


# blocked = ["mail.ru", "yahoo.com"]

# file = open("text.txt","r")
# file2 = open("text2.txt", "w")

# lines = file.readlines()
# for email in lines:
#     email = email.replace("\n","")
#     # print(email)
#     email_domain = email.split("@")[1]
#     if email_domain in blocked:
#         file2.write(email_domain)
#     else:
#         print(email)
# print(file2)
# file.close()
# file2.close()

# son = open("son.txt", "w")
# for i in range(1, 100):
#     son.write("i")
#     if i % 3 == 0:
#         son.write("\n")


# son = open("son2.txt","w")
# for i in range(10):
#       for j in range(10):
#         if i == 0 or j == 0 or j == 10 - 1 or i == 10 - 1:
#            son.write("* ")
#         else:
#            son.write(" ")
#       son.write("\n")
# son.close()

# while True:
#     if 
#     x = int(input("son kirit: >>>"))
#     if x % 2 == 0:
#         print("son juft")
#     else:
#         print("son toq")


# Uchta son berilgan. 
# Shu sonlarning kichigini aniqlovchi programma tuzilsin.

# x = input("1 son")
# y = input("2 son")
# z = input("3 son")
# son = [x, y, z]
# son.sort()
# print(son[0])

# aziz = int(input("  "))
# begzod = int(input("  "))
# farhod = int(input("  "))
# eng_kichik = 0
# if aziz < begzod:
#     eng_kichik = aziz
#     if eng_kichik < farhod:
#         print(eng_kichik)
#     elif eng_kichik > farhod:
#         eng_kichik = farhod
#         print(eng_kichik)
# elif aziz > begzod:
#     eng_kichik = begzod
#     if eng_kichik > farhod:
#         eng_kichik = farhod
#         print(eng_kichik)
#     else:
#         print(eng_kichik)


    
# x,y haqiqiy sonlari berilgan. Ularning kichigini sonlar yig’indisining yarmiga, kattasini
# ko’paytmasining ikkilanganiga almashtiruvchi programma tuzilsin. Agar sonlar teng
# bo'lsa, o'zgari ishsiz qoldirilsin.

# x = int(input("  "))
# y = int(input("  "))

# if x < y:
#     x = (x + y) / 2
#     y = (x * y) * 2
# else:
#     x = (x * y) * 2
#     y = (x + y) / 2
# print(f"bu son x = {x}, bu son y = {y}")

# N natural soni va n ta sonlar 
# to’plami berilgan. Kiritilgan to’plamdagi eng
# katta va eng kichik sonni topuvchi programma tuzilsin. 
# Massivdan foydalanmang



