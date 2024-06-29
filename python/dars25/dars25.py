# class BankAccount:
#     def __init__(self, balance=0) -> None:
#         if balance < 0:
#             raise ValueError("Balance cannot be negativ")
#         self.balance = balance
    
#     def add(self, amount):
#         self.balance += amount
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise ValueError("Insufficient balance")
#         self.balance -= amount
    
#     def check_balance(self):
#         return self.balance

# account = BankAccount(100)
# print(account.check_balance())
# account.add(100)
# print(account.check_balance())
# account.withdraw(50)
# print(account.check_balance())


# 
 
class ATMOperations:
    def __init__(self):
        self.currencies = {
            "1000": 50, "5000": 90, "10000": 100, "20000": 100, 
            "50000": 100, "100000": 77, "200000": 10000
        }

    def withdraw(self, amount):
        withdrawn_notes = {} # yechiladigan pullar
        remaining_amount = amount # qolgan summa
        notes_names = [key for key in self.currencies.keys() if self.currencies[key] > 0][::-1]
        for note in notes_names:
            note_value = int(note)

            # Nechta pul olib chiqish kerakligini aniqlash
            potential_notes = remaining_amount // note_value 

            # Agar pullar mavjud bo'lsa, ularni hisobga olish
            notes_to_withdraw = 0
            while notes_to_withdraw < potential_notes and notes_to_withdraw < self.currencies[note]:
                notes_to_withdraw += 1
            
            if notes_to_withdraw > 0:
                withdrawn_notes[note] = notes_to_withdraw
                remaining_amount -= notes_to_withdraw * note_value
                self.currencies[note] -= notes_to_withdraw

        if remaining_amount == 0:
            print("Yechilgan pullar:")
            for note, count in withdrawn_notes.items():
                print(f"{note}: {count}")
        else:
            print("Bankomatda pul yetarli emaas")

    def check_balance(self):
        total_balance = 0
        for note, count in self.currencies.items():
            total_balance += int(note) * count
        return total_balance

    

atm = ATMOperations()
atm.withdraw(951_237_000)




class BankomatAmaliyoti:
    def __init__(self):
        self.pul_turlari = {
            "1000": 50, "5000": 90, "10000": 100, "20000": 100, 
            "50000": 100, "100000": 77, "200000": 10000
        }

    def pul_qilish(self, miqdor):
        yechilgan_pullar = {} # yechiladigan pullar
        qolgan_miqdor = miqdor # qolgan miqdor
        pullar_nomlari = [nom for nom in self.pul_turlari.keys() if self.pul_turlari[nom] > 0][::-1]
        for nom in pullar_nomlari:
            nom_qiymati = int(nom)

            # Nechta pul olib chiqish kerakligini aniqlash
            potentsial_pullar = qolgan_miqdor // nom_qiymati 

            # Agar pullar mavjud bo'lsa, ularni hisobga olish
            olinadigan_pullar = 0
            while olinadigan_pullar < potentsial_pullar and olinadigan_pullar < self.pul_turlari[nom]:
                olinadigan_pullar += 1
            
            if olinadigan_pullar > 0:
                yechilgan_pullar[nom] = olinadigan_pullar
                qolgan_miqdor -= olinadigan_pullar * nom_qiymati
                self.pul_turlari[nom] -= olinadigan_pullar

        if qolgan_miqdor == 0:
            print("Yechilgan pullar:")
            for nom, sanasi in yechilgan_pullar.items():
                print(f"{nom}: {sanasi}")
        else:
            print("Bankomatda pul yetarli emas")

    def balansni_tekshirish(self):
        jami_balans = 0
        for nom, sanasi in self.pul_turlari.items():
            jami_balans += int(nom) * sanasi
        return jami_balans

    

bankomat = BankomatAmaliyoti()
bankomat.pul_qilish(951_237_000)
