# Завдання1

number_1 = int(input("Введіть число 1: "))
number_2 = int(input("Введіть число 2: "))
number_3 = int(input("Введіть число 3: "))
suma = number_1 + number_2 + number_3
dobutok = number_1 * number_2 * number_3
print("Ваша сума чисел:" + str(suma))
print("Ваш добуток чисел:" + str(dobutok))

#Завдання2
zarplata = int(input("Введіть зарплату за місяць : "))
platizh = int(input ("Введіть місячний платіж за кредитом : "))
borg = int(input("Введіть заборгованість за комунальні послуги : "))
result = zarplata-platizh-borg

print("Сума,яка залишилась: " + str(result))

