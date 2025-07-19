carres = []

for i in range(1,21):
    carres.append(i ** 2)

print("Tous les carrés : ", carres)

print("carrés > 100 :")
for val in carres :
    if val > 1000:
        print(val)