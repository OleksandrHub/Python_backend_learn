import math
# test = 5 - змінна
# тип даних - int, float, str, bool, list, tuple, set, dict
name = "Vlad"

print("Hello world")
# перевід з нової строки
print("Hello\nworld")
# Конкатенація
print("Hello" + " world " + name + "!")
# Тайпкастинг
print("Hello " + str(5) + " world " + name + "!")

name = input("Enter your name: ")
print("Hello " + name + "!")

# +, -, *, /, //, %, **, унарний мінус та заокруглення - арифметичні оператори
print(math.ceil(5.2))  # округлення до більшого
print(math.floor(5.2))  # округлення до меншого
print(math.pi)  # число Пі