# info = {"python": 99, "js": 99}
# #key - value
# info = {"python": [1, 2, 3], "js": 99}
# #{key: value} -> {kalit: qiymat}
# # print(info["python"][1])
# # print(info["python"])
# print(info)
# #changing and adding = qoshish va ozgartirish
# info["c"] = 100 # qo'shish
# info["python"] = 1000 # o'zgartirish
# print(info)

# info = {"python": [1, 2, 3], "js": 99}

# print(info.keys()) # kalitlarni oladi
# print(info.values()) #qiymatlarni oladi
# print(info.items()) #qiymatlarni va kalitlarni oladi

# info = {"python" : 11, "js": 10}
# print(info)
# info.pop("python") #kalit bn ochirish
# print(info)

# marks = {"botir": 50, "anvar": 99, "shoxrux": 20, "nurullo": 100}
# for key in marks:
#     if marks[key] > 80:
#         print(f"{key} imxtixondan {marks[key]} ball oldi")

# db = {"test": "a123456", "megamax" : "secret123"}
# print(db.get("test", False))

db = {"test": "a123456", "megamax": "secret123"}

login = input("enter login: ")
if db.get(login, False): # get() - berilgan narsa bolsa true, bolmasa False qaytaradi
    password = input("enter password: ")
    if db[login] == password:
        print("welcome")
    else:
        print("xato parol")
else:
    print("User mavjud emas")


# kril_lotin_alphabet = {
#     "a": "а", "b": "б", "c": "с", "d": "д", "e": "е", "f": "ф", "g": "г",
#         "h": "ҳ", "i": "и", "j": "ж", "k": "к", "l": "л", "m": "м", "n": "н",
#         "o": "о", "p": "п", "q": "қ", "r": "р", "s": "с", "t": "т", "u": "у",
#         "v": "в", "w": "в", "x": "х", "y": "й", "z": "з", "S": "С"                  
#                        }
# text = input("enter text: ").lower()
# result = ""
# for char in text:
#     if char in kril_lotin_alphabet:
#         result += kril_lotin_alphabet[char]
#     if char == " ":
#         result += " "
# print(result)


academiya = {
    "name": "jhon",
    "age": 40,
    "type": "person"
}
academiya2 = dict(
    name = ["jhon", "Said Ali" ],
    age = 40,
    type = "person"
)
print(type(academiya2))

# print(academiya2.get("name", "tur yoqol"))
# academiya2["age"] = 80
# print(academiya2)
# academiya2["name"][0] = "xoja"
# print(academiya2)
# academiya2.update({"name":["Said Ali Xo'ja", "Hikmatillayev"]})
# print(academiya2)

item = {
    'dota':{
        'first_blood':1,
        'duouble_kill':2,
        'triple_kill':3
    },
    'dota2':{
        'blood':1,
        'kill':2, #
        'kill':3
    },
    'dota3':{
        'dither':"white", #
        'MK':30,
        'AK_40':30
    }
}

print(item['dota2']["kill"], item['dota3']["dither"] )

a = {1, 2, 3, 4}
b = ['text','double']
a.update(b)
print(a)


