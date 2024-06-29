# Mantiqiy qiymat qaytaruvchi IsLeapYear(Year) funksiyasini hosil qiling.
# Funksiya berilgan Year – yil kabisa yili bo’lsa true, aks holda false qiymat qaytarsin.
# Berilgan 3 ta yildan nechtasi kabisaligini aniqlovchi dastur tuzing. (Kabisalik shartini
# bilish uchun IF28 masalaga qarang.)

def IsLeapYear(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return("Berilgan yil kabisa")
    else:
        return("Berilgan yil kabisa emas")
a = IsLeapYear(2020)
print(a)

