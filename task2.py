# Единицы длины
# пронумерованы следующим образом: 1 — деци- метр,
# 2 — километр, 3 — метр, 4 — миллиметр, 5 — сантиметр. Дан номер единицы длины (целое число в
# диапазоне 1-5) и длина отрез- ка в
# этих единицах (вещественное число). Найти длину отрезка в метрах.

def find_length(unit, length):
	if unit == 1:
		length = length / 10
		print(length)
	elif unit == 2:
		length = length * 1000
		print(length)
	elif unit == 3:
		print(length)
	elif unit == 4:
		length = length * 0.001
		print(length)
	elif unit == 5:
		length = length * 0.01
		print(length)


unit = int(input("Введите целое число в диапозое 1 - 5: "))
length = float(input("Введите вещественное число, длина: "))

if 1 <= unit <= 5:
	find_length(unit, length)
else:
	print("Ошибка")
