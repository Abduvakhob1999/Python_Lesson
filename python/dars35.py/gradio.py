x = input("matn kirit")
y = x.split()
matnlar = {}

for i in y:
    if i not in matnlar:
        matnlar[i] = 1
    else:
        matnlar[i] += 1

max = 0
min = 9999

for i,j in matnlar.items():
    if j > max:
        max = j
    if j < min:
        min = j

print(min, max)