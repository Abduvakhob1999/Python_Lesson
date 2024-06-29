# def menu():
    
#     mahsulot = []
#     try:
#         while True:
#             print(
#                 " 1.Mahsulot qo'shish \n 2.Mahsulot olib tashlash \n 3.Mahsulot ko'rsatish \n 4 chiqish" 
#                 )
#             tanlov = int(input("tanlov kiriting: (1-4)"))
#             if tanlov == 4:
#                 break
#             elif tanlov == 1:
#                 mahsulot_tanlov = input("Mahsulot nomini kiriting")
#                 mahsulot.append(mahsulot_tanlov)
#                 print(f"{mahsulot_tanlov} royhatga qoshildi")
#             elif tanlov == 2:
#                 mahsulot.remove(mahsulot_tanlov)
#                 print(f"{mahsulot_tanlov} royhatdan olib tashlandi")
#             elif tanlov == 3:
#                 print(f"Joriy Mahsulotlar royhati \n{mahsulot}")
#     except:
#         print("Hali mahsulot tanlamdingiz")
#         while True:
#             print(
#                 " 1.Mahsulot qo'shish \n 2.Mahsulot olib tashlash \n 3.Mahsulot ko'rsatish \n 4 chiqish" 
#                 )
#             tanlov = int(input("tanlov kiriting: (1-4)"))
#             if tanlov == 4:
#                 break
#             elif tanlov == 1:
#                 mahsulot_tanlov = input("Mahsulot nomini kiriting")
#                 mahsulot.append(mahsulot_tanlov)
#                 print(f"{mahsulot_tanlov} royhatga qoshildi")
#             elif tanlov == 2:
#                 mahsulot.remove(mahsulot_tanlov)
#                 print(f"{mahsulot_tanlov} royhatdan olib tashlandi")
#             elif tanlov == 3:
#                 print(f"Joriy Mahsulotlar royhati \n{mahsulot}")

# menu()


# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

# def my_function(food):
#   for x in food:
#     print(x)

# fruits = ["apple", "banana", "cherry"]

# my_function(fruits)

# def my(*args):
#     for i in args:
#         if i > 10:
#             print(i < 10)
    
# my(10, 100)

# p, q, r = 10, 20 ,30
# print(p, q, r)

# def calculate (num1, num2=4):
#   res = num1 * num2
#   print(res)

# calculate(5, 6)

# sampleSet = {"Jodi", "Eric", "Garry"}
# sampleSet.add(1, "Vicki")
# print(sampleSet)

# salary = 8000

# def printSalary():
#   salary = 12000
#   print("Salary:", salary)
  
# printSalary()
# print("Salary:", salary)


# def display_menu():
#     print("\nMahsulotlar Ro'yxat Dasturi")
#     print("1. Mahsulot qo'shish")
#     print("2. Mahsulot olib tashlash")
#     print("3. Ro'yxatni ko'rsatish")
#     print("4. Chiqish")



# def add_item(grocery_list):
#     item = input("Qo'shmoqchi bo'lgan mahsulotni kiriting: ")
#     grocery_list.append(item)
#     print(f"{item} ro'yxatga qo'shildi.")




# def remove_item(grocery_list):
#     item = input("Olib tashlamoqchi bo'lgan mahsulotni kiriting: ")
#     if item in grocery_list:
#         grocery_list.remove(item)
#         print(f"{item} ro'yxatdan olib tashlandi.")
#     else:
#         print(f"{item} ro'yxatda mavjud emas.")

        

# def show_list(grocery_list):
#     if grocery_list:
#         print("\nJoriy Mahsulotlar Ro'yxati:")
#         for item in grocery_list:
#             print(item)
#     else:
#         print("Sizning mahsulotlar ro'yxatingiz hozircha bo'sh.")


# grocery_list = []
# while True:
#     display_menu()
#     choice = input("Tanlovni kiriting (1-4): ")
    
#     if choice == '1':
#         add_item(grocery_list)
#     elif choice == '2':
#         remove_item(grocery_list)
#     elif choice == '3':
#         show_list(grocery_list)
#     elif choice == '4':
#         print("Mahsulotlar Ro'yxat Dasturidan chiqilmoqda. Xayr!")
#         break
#     else:
#         print("Noto'g'ri tanlov, iltimos to'g'ri raqamni tanlang (1-4).")
