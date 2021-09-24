# Даны целые положительные числа N и K. Найти
# сумму 1K + 2K + . . . + NK .

def sum(n, k):
	res = 0
	for i in range(1, n + 1):
		res += i * k
	print(res)


n, k = map(int, input("Введите положительніе числа а, б: ").split())

if n > 0 and k > 0:
	sum(n, k)
else:
	print("Ошибка")
