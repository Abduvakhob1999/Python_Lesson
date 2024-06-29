product = {"iphone": 3, "ipad": 2, "samsung": 22}
user_buy = {}  

while True:
    user = input("Nima sotib olasiz? To'xtatish uchun 'q' ni bosing: ")
    if user != "q":
        if user in product:  
            if product[user] > 0:  
                if user not in user_buy:
                    user_buy[user] = 1 
                else:
                    user_buy[user] += 1 
                product[user] -= 1 
                print(f"{user} sotib olindi. Qolgan {product[user]} ta {user} qoldiqda.")
            else:
                print(f"Kechirasiz, {user} hozir mavjud emas.")
        else:
            print("Kechirasiz, bizda bunday mahsulot yo'q.")
    else:
        break

print("Sizning sotib olishingiz:")
print(user_buy)