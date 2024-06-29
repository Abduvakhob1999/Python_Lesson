# LLM large lenguages model

#prompt engineering
#Annotations  


# def foo(nums: list):
#     result = [i for i in nums if i % 2 == 0]
#     result.pop(0)
#     return result

# foo((1, 2, 3), 2)

# def eng_kotta(listt):
#     x = 0
#     for i in listt:
#         if i > x:
#             x = i
#     listt.remove(x)
#     return listt

# a = eng_kotta([1, 2, 5, 33, 6, 8, 11, 22])
# print(a)

#  Assalomu alaykum! Python tilida test topshirish uchun tayyormisiz?
# Har bir savolga to'g'ri javobni tanlang (a, b, c, d).

# Savol 1:
# Python tilida 1 + 1 qancha?
# 1. a. 1
# 2. b. 2
# 3. c. 3
# 4. d. 4

# Javobingizni kiriting: b
# To'g'ri javob! 👍

# Savol 2:
# Python tilida 3 * 5 qancha?
# 1. a. 5
# 2. b. 8
# 3. c. 15
# 4. d. 35

# Javobingizni kiriting: d
# Noto'g'ri javob. 😔

# Savol 3:
# Python dasturlash tili nima uchun ishlatiladi?
# 1. a. Machine Learning
# 2. b. Web development
# 3. c. Networking
# 4. d. Tepadigi hammasi

# Javobingizni kiriting: d
# To'g'ri javob! 👍

# Test natijalari: 2/3 to'g'ri.
# Sizning test natijalaringizni yaxshi ko'rib chiqing.

def test():
    savollar = [
        {
            "savol": "Python tilida 1 + 1 qancha?",
            "variantlar": {
                "a": "1",
                "b": "2",
                "c": "3",
                "d": "4"
            },
            "to'g'ri_javob": "b"
        },
        {
            "savol": "Python tilida 3 * 5 qancha?",
            "variantlar": {
                "a": "5",
                "b": "8",
                "c": "15",
                "d": "35"
            },
            "to'g'ri_javob": "c"
        },
        {
            "savol": "Python dasturlash tili nima uchun ishlatiladi?",
            "variantlar": {
                "a": "Machine Learning",
                "b": "Web development",
                "c": "Networking",
                "d": "Tepadigi hammasi"
            },
            "to'g'ri_javob": "d"
        }
    ]

#     togri_javoblar_soni = 0
#     print("Assalomu alaykum! Python tilida testga xush kelibsiz!")
#     print("Har bir savolga to'g'ri javobni tanlang (a, b, c, d).\n")

#     for idx, savol in enumerate(savollar, 1):
#         print(f"Savol {idx}:")
#         print(savol["savol"])
#         for variant, javob in savol["variantlar"].items():
#             print(f"{variant}. {javob}")
#         javob = input("\nJavobingizni kiriting: ").strip().lower()
#         if javob == savol["to'g'ri_javob"]:
#             print("To'g'ri javob! 👍")
#             togri_javoblar_soni += 1
#         else:
#             print("Noto'g'ri javob. 😔")
    
#     print(f"\nTest natijalari: {togri_javoblar_soni}/{len(savollar)} to'g'ri.")
#     print("Sizning test natijalaringizni yaxshi ko'rib chiqing.")

# test()

sovolar = [[["Python tilida 1 + 1 qancha?"],['"a": 5']]

            ]

togri_jovoplar = 0
print("Assalomu alaykum! Python tilida testga xush kelibsiz")