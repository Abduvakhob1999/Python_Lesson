# import time
# def timer(func):
#     def  wrapper(*args, **kwargs):
#         start = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         print(end - start)
#     return wrapper

# @timer
# def example_function():
#     print("function executed")

# @timer
# def add(x, y):
#     print(x + y)

# example_function()
# add(1, 2)



# def not_negative(func):
#     def ichki(a, b):
#         if a < 0:
#             print("a is negative")
#         elif b < 0:
#             print("b is negative")
#         else:
#             func(a,b)
#     return ichki

# @not_negative
# def add(a, b):
#     print(a + b)

# @not_negative
# def sub(a, b):
#     print(a * b)

# @not_negative
# def mul(a, b):
#     print(a / b)

# add(1 , 4)
# mul(8, 2)
# sub(5, 7)


# def logger(func):
#     def wrapper(*args, **kwargs):
#             print(f"funkisiyada berilgan argumentlar {args}, {kwargs}")
#             result = func(*args, **kwargs)
#             print(f"funksiyadan qaytarilgan narsa {result}")
#             return result
#     return wrapper

# @logger
# def subtract(a, b):
#     return a - b

# # subtract(10, 7)
# def authenticate(func):
#     def wrappers(**kwargs):
#         a = kwargs.get("user")
#         if a in logged_in_users:
#             return func(**kwargs) 
#         else:
#             print("Access denied, pleas log in.")
#     return wrappers

# logged_in_users = ["user1", "user2","user3"]

# @authenticate
# def sensitve_operation(user):
#     print(f"{user} performed a sansitive operation")

# sensitve_operation(user="user1")
# sensitve_operation(user="user4")



# def uppercase(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result.upper()
#     return wrapper

# @uppercase
# def great(name):
#     return f"hello, {name}!"

# print(great("alice"))


# def twice(func):
#     def wrapper(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper

# @twice
# def greet(name):
#     print(f"hello, {name}")

# greet("alice")


# def my_decorator(func):
#     def wraper():
#         print("aaaaaaa")
#         func()
#         print("aaaaaaaa")
#     return wraper
    
# @my_decorator
# def say_hello():
#     print("hello")

# say_hello()


# def double(func):
#     def wrappeer(*args):
#         a = func(*args)
#         return a * 2
#     return wrappeer

# @double
# def add_five(x):
#     return x + 5

# result = add_five(3)
# print(result)

# def tekshir_argumentlar(func):
#     def wrapper(*args, **kwargs):
#         try:
#             func_result = func(*args, **kwargs)
#             x = [arg for arg in args if arg < 0]
#             if not x:
#                 print("Hech qanday Hatolik yo'q")
#                 return  func_result
#         except:
#             # print("TypeError: 'b' argumenti 0 ga teng bo'lmasligi kerak!")
#             return "TypeError: 'b' argumenti 0 ga teng bo'lmasligi kerak!"
#     return wrapper   
 
# @tekshir_argumentlar
# def bolish(a, b):
#     return a / b

# natija = bolish(10, 2)  # Hech qanday xatolik yo'q
# print(natija)          # Chiqish: 5

# natija = bolish(10, 0)  # TypeError xatolik chiqarishi kerak: TypeError: 'b' argumenti 0 ga teng bo'lmasligi kerak!
# print(natija)

# 2 usul

# def tekshir_argumentlar(func):
#     def wrapper(*args, **kwargs):
#         worker_func = func(*args, **kwargs)
#         for arg in args:
#             if arg > 0:
#                 return worker_func
#             else:
#                 return "TypeError: 'b' argumenti 0 ga teng bo'lmasligi kerak!"
#         return wrapper    
    
# @tekshir_argumentlar
# def bolish(a, b):
#     return a / b

# natija = bolish(10, 2)  # Hech qanday xatolik yo'q
# print(natija)          # Chiqish: 5

# natija = bolish(10, 0)  # TypeError xatolik chiqarishi kerak: TypeError: 'b' argumenti 0 ga teng bo'lmasligi kerak!
# print(natija)

# for i in range(10):
#     for j in range(10):
#         if i == 0 or j == 0 or j == 10 - 1 or i == 10 - 1:
#            print("* ", end="")
#         else:
#            print("  ", end="")
#     print()


# def tekshir_argumentlar(func):
#     def wrapper(*args):
#         # funksiya = func(*args)
#         for arg in args:
#             if arg == 0:
#                return "TypeError: 'b' argumenti 0 ga teng "
            
#         return func(*args)
#     return wrapper
               


 
# @tekshir_argumentlar
# def bolish(a, b):
#     return a / b

# natija = bolish(10, 2)  # Hech qanday xatolik yo'q
# print(natija)          # Chiqish: 5

# natija = bolish(10, 0)  # TypeError xatolik chiqarishi kerak: TypeError: 'b' argumenti 0 ga teng bo'lmasligi kerak!
# print(natija)

# def salomlash(func):
#     def wrapper(ism):
#         print("salom")
#         return func(ism)
#     return wrapper


# @salomlash
# def salom(ism):
#     print(f"Ismingiz nima? {ism}")

# salom("Ali")  

a = open("text.txt", "w") 
x = [i for i in range(1, 10) if i > 0]
a.write(str(x) + "\n")
a.close()
