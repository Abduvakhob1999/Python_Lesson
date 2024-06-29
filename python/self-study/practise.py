# Мерцай, мерцай, звездочка,
# 	Как я жажду узнать, кто ты!
# 		Над миром так высоко,   		
# 		Как алмаз в небе.
# Мерцай, мерцай, звездочка,
# 	Как я жажду узнать, кто ты
# print("Мерцай, мерцай, звездочка,\n\tКак я жажду узнать, кто ты!\n\t\tНад миром так высоко,\n\t\tКак алмаз в небе.\n Мерцай, мерцай, звездочка,\n\tКак я жажду узнать, кто ты ")



# foods = []
# while len(foods) < 10:
#     number = input("matn kiriting: >>>")
#     foods.append(number)
# print(foods)

# x = int(input("son"))    
# s = 0
# for i in range(1, x):
#     if x % i == 0:
#         s += 1
#         print(i)
# print(s)


# class Foo:
#     global x
#     x = open("ismlar.txt", "w")
#     def __init__(self, ism, familya, yosh):
#         self.ism = ism
#         self.familya = familya
#         self.yosh = yosh
#     def ismlar(self):
#         x.write(self.ism)
#     def familyalar(self):
#         x.write(self.familya)
#     def yosh_kirit(self):
#         x.write(self.yosh)

# func = Foo("Abdulaziz", "Dadaxadjayev", 41)
# print(Foo.yosh_kirit(32))

x = int(input("son1: "))
y = int(input("son2: "))
z = int(input("son3: "))

if x < y: 
    if x < z:
        print(f"eng kichik son {x}")
    else:
        print(f"eng kichik son {z}")
elif y < x:
    if y < z:
        print(f"eng kichik {y}")
    else:
        print(f"eng kichik son {z}")

        