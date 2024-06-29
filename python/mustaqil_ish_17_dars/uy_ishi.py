

# royhat = [1, 2, 3, 4, 5]
# def royhatga_qosh(*sonlar):
#     for son in sonlar:
#         royhat.append(son)
#     return royhat
# jami = royhatga_qosh(6, 7)
# print(jami)




# Eng Kichik Elementni Topish:
# Sonlar ro'yxatini qabul qiladigan va ro'yxatdagi eng kichik sonni qaytaradigan 
# eng_kichik funksiyasi yarating.Misol Kirish:
# Ro'yxat: [34, 19, 23, 58, 12, 7, 90]
# Natija: 7



# royhat = [34, 19, 23, 58, 12, 7, 90]
# def eng_kichik(royhat):
#     eng_kichik_son = royhat[0]
#     x = 1
#     while x < len(royhat):
#         if eng_kichik_son > royhat[x]:
#             eng_kichik_son = royhat[x]
#         x += 1
#     return eng_kichik_son

# natija = eng_kichik()



#  Ro'yxatni Teskari Tartibga Keltirish:
# Sonlar ro'yxatini qabul qilib, uni teskari tartibda qaytaradigan teskari funksiyasi yarating.
# Misol Kirish:
# Ro'yxat: [1, 2, 3, 4, 5]
# Natija: [5, 4, 3, 2, 1]


# x = [1, 2, 3, 4, 5]
# def teskari_formula(list):
#     natija = list[::-1]
#     return natija

# teskari_formula(x)

#  Ro'yxatdan Ma'lum Elementni Olib Tashlash:
# Ro'yxat va olib tashlanadigan element qabul qiladigan, va shu elementni ro'yxatdan olib tashlaydigan
# elementni_olib_tashla funksiyasi yarating.Misol Kirish:
# Ro'yxat: [1, 2, 3, 4, 5, 3]
# Olib tashlanadigan element: 3
# Natija: [1, 2, 4, 5]
    


# royxat = [1, 2, 3, 4, 5, 3]
# def ochirish(royxatlar , son):
#     royxatlar.remove(son)
#     return royxatlar

# print(ochirish(royxat, 3))

# def kalkulyator(*arks):
#     natija = 0
#     for i in arks:
#         natija += i
#     return natija
# print(kalkulyator(1, 4, 5, 6,2,3,45,21,54))

#  Foydalanuvchi Ma'lumotlarini Chop Etish:
# Foydalanuvchidan turli xil shaxsiy ma'lumotlar qabul qiladigan va ularni chop etadigan foyda
# ma'lumotlari funksiyasi yarating.Misol Kirish va Natija:
# foyda_ma'lumotlari(ism="Ali", yosh=25, kasb="Dasturchi") -> Natija: Ism: Ali, Yosh: 25, Kasb: Dasturchi
# foyda_ma'lumotlari(ism="Zara", manzil="Toshkent") -> Natija: Ism: Zara, Manzil: Toshkent
# def malumotlar(**malumotlar):
#     return malumotlar
# a = malumotlar(ism="Ali", yosh=25, kasb="Dasturchi")             
# print(a)


def foyda_malumotlari(**kwargs):
    malumotlar = ", ".join([f"{key.capitalize()}: {value}" for key, value in kwargs.items()])
    print("Natija:", malumotlar)
    # for k,v in kwargs.items():
    #     malum = f"{k.capitalize()} ---- {v}, "
    #     print("nat:", malum)

# Test qilish
foyda_malumotlari(ism="Ali", yosh=25, kasb="Dasturchi")
foyda_malumotlari(ism="Zara", manzil="Toshkent")

# def malumot_turi(*luboy):
#     e = dict(luboy)
#     e.keys()
#     return e

# b = {"aziz": 15, "anvar": 10, "olim":12}
# a = malumot_turi(b)
# print(a)


# def malumot_turi(royxat):
#     e = dict(royxat)
#     return e.values()

# b = {"aziz": 15, "anvar": 10, "olim": 12}
# a = malumot_turi(b)
# print(a)


 
