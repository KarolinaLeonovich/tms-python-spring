# Для заданного числа N составьте программу вычисления
# суммы S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число

n = input()
s = 1

if n.isdigit():
    n = int(n)
    for i in range(2, n + 1):
        s += 1 / i
print(s)
