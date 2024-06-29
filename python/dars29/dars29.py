#  Vazifa: So'z Chastotasi Hisoblagichi

# Berilgan matndagi so'zlarning chastotasini tahlil qiluvchi Python dasturini yarating.

# Ma'lumotlar tuzilmasi:

# word_freq lug'ati so'zlarni (matnlar) kalit sifatida va ularning chastotalarini
# (butun sonlar) qiymat sifatida saqlaydi.
# Funksionallik:

# process_text(text):

# Kirish matnini oladi (text - matn).
# Barcha so'zlarni kichik harflarga o'zgartiradi.
# Tinish belgilarini olib tashlaydi (masalan, ".", ",", "?", "!").
# Matnni so'zlar ro'yxatiga ajratadi.
# Tozalangan so'zlar ro'yxatini qaytaradi.
# count_words(word_list):

# word_list (matnlar ro'yxati) ni oladi.
# word_freq lug'atini yaratadi.
# for tsikli yordamida word_list dagi har bir so'z bo'yicha takrorlaydi:
# Agar so'z allaqachon word_freq da bo'lsa, uning hisobini oshiradi.
# Agar bo'lmasa, uni word_freq ga 1 ga teng hisob bilan qo'shadi.
# word_freq lug'atini qaytaradi.




# def process_text(text):
#     tinish_belgilar = ".", ",", "?", "!"
#     lower = text.lower()

#     lower = lower.split()
    
            
#     return lower
        
# print(process_text("Bu namunaviy !!matn. Bu matn sinov !!uchun ishlat!iladi."))


fovorites = []

def add_favorite(list1, text):
    list1.append(text)
    return list1
        
def list_favorite(list1):
    for i in range(1, len(list)):
        
    
