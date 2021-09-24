# Даны целые положительные числа A и B (A < B). Вывести все целые числа от A до B включительно; при этом каждое
# число должно вы- водиться столько раз, каково его значение
# (например, число 3 выводит- ся 3 раза).

def print_numbers(a, b):
	for i in range(a, b + 1):
		for j in range(i):
			print(i)


a, b = map(int, input("Введите а и б: ").split())

if a < b:
	print_numbers(a, b)
else:
	print("Ошибка")