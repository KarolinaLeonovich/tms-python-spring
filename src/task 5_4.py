# Задание 5_4
# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N - натуральное число

N = int(input('Введите натуральное число: '))
summ = 0
for i in range(1, N+1):
    summ += 1/i
    i += 1
print(summ)
