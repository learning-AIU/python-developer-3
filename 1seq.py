# допускаем, что пользователь всегда вводит только цифровые символы
n = int(input('Введите количество элементов: '))
numbers = [int(input(f'Введите {i} элемент: ')) for i in range(1, n+1)]
numbers = sorted(numbers)
print(numbers)


# stdout:
# Введите количество элементов: 3
# Введите 1 элемент: 1
# Введите 2 элемент: 5
# Введите 3 элемент: 3
# [1, 3, 5]
