# Дано целое число K. Вывести строку-описание оценки, соответствующей
# числу K (1 — «плохо», 2 — «неудовлетворительно», 3 — «удов- летворительно», 4 — «хорошо», 5 —
# «отлично»). Если K не лежит в диапазоне 1-5, то вывести
# строку «ошибка».

def rating(k):
    if k == 1:
        print("Плохо")
    elif k == 2:
        print("Неудовлетворительно")
    elif k == 3:
        print("Удовлетворительно")
    elif k == 4:
        print("Хорошо")
    elif k == 5:
        print("Отлично")


k = int(input("Введите целоеле число: "))

if 1 <= k <= 5:
    rating(k)
else:
    print("Ошибка")
