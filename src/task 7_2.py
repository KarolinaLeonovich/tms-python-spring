# Задание 7_2
# Написать программу со следующим интерфейсом:
# пользователю предоставляется на выбор 12 вариантов перевода (описанных в первой задаче).
# Пользователь вводит цифру от одного до двенадцати.
# После программа запрашивает ввести численное значение.
# Затем программа выдает конвертированный результат.
# Использовать функции из первого задания.
# Программа должна быть в бесконечном цикле.
# Код выхода из программы - "0"

def dyim_v_sant(d):  # Дюймы в сантиметры
    d *= 2.54
    return d


def sant_v_dyim(s):  # Сантиметры в дюймы
    s /= 2.54
    return s


def mili_v_km(m):  # Мили в километры
    m *= 1.6
    return m


def km_v_mili(k):  # Километры в мили
    k /= 1.6
    return k


def funt_v_kg(f):  # Фунты в килограммы
    f /= 2.2
    return f


def kg_v_funt(kg):  # Килограммы в фунты
    kg *= 2.2
    return kg


def unc_v_gr(u):  # Унции в граммы
    u *= 28.35
    return u


def gr_v_unc(gr):  # Граммы в унции
    gr /= 28.35
    return gr


def gall_v_litr(g):  # Галлоны в литры
    g *= 4.55
    return g


def litr_v_gall(lt):  # Литры в галлоны
    lt /= 4.55
    return lt


def pint_v_litr(p):  # Пинты в литры
    p /= 1.76
    return p


def litr_v_pint(lit):  # Литры в пинты
    lit *= 1.76
    return lit


print('Список доступных операций:')
list_op = ['Дюймы в сантиметры', 'Сантиметры в дюймы', 'Мили в километры',
           'Километры в мили', 'Фунты в килограммы', 'Килограммы в фунты',
           'Унции в граммы', 'Граммы в унции', 'Галлоны в литры',
           'Литры в галлоны', 'Пинты в литры', 'Литры в пинты']
for number, operation in enumerate(list_op, 1):
    print(f'{number}. {operation}')

while True:
    try:
        num = input('Введите номер операции, которую хотите использовать: ')
        num = int(num)
        if num == 0:
            print('Программа завершена. Для повторного использования нажмите '
                  'на значок запуска программы.')
            break
        if num > 12:
            print('Ошибка ввода. Пожалуйста, введите номер операции от 1 до 12 '
                  'из вышеприведенного списка или введите 0 для окончания работы '
                  'программы. Попробуйте заново.')
            continue
    except(ValueError):
        print('Ошибка ввода. Пожалуйста, введите номер операции от 1 до 12 '
              'из вышеприведенного списка или введите 0 для окончания работы '
              'программы. Попробуйте заново.')
        continue


    while True:
        try:
            if num == 1:
                d = input('Введите количество дюймов: ')
                if d == 'стоп':
                    break
                elif float(d) < 0:
                    print('Программа с отрицательными числами не работает. Попробуйте заново.')
                elif d == 'стоп':
                    break
                else:
                    d = float(d)
                    print(f'Количество сантиметров = {dyim_v_sant(d)}. Если хотите вернуться в '
                          f'окно выбора операций введите "стоп"')

            elif num == 2:
                s = input('Введите количество сантиметров: ')
                if s == 'стоп':
                    break
                elif float(s) < 0:
                    print('Программа с отрицательными числами не работает. Попробуйте заново.')
                else:
                    s = float(s)
                    print(f'Количество дюймов = {sant_v_dyim(s)}. Если хотите вернуться в '
                          f'окно выбора операций введите "стоп"')

            elif num == 3:
                m = input('Введите количество миль: ')
                if m == 'стоп':
                    break
                elif float(m) < 0:
                    print('Программа с отрицательными числами не работает. Попробуйте заново.')
                else:
                    m = float(m)
                    print(f'Количество километров = {mili_v_km(m)}. Если хотите вернуться в '
                          f'окно выбора операций введите "стоп"')

            elif num == 4:
                k = input('Введите количество километров: ')
                if k == 'стоп':
                    break
                elif float(k) < 0:
                    print('Программа с отрицательными числами не работает. Попробуйте заново.')
                else:
                    k = float(k)
                    print(f'Количество миль = {km_v_mili(k)}. Если хотите вернуться в '
                          f'окно выбора операций введите "стоп"')

            elif num == 5:
                f = input('Введите количество фунтов: ')
                if f == 'стоп':
                    break
                elif float(f) < 0:
                    print('Программа с отрицательными числами не работает. Попробуйте заново.')
                else:
                    f = float(f)
                    print(f'Количество килограммов = {funt_v_kg(f)}. Если хотите вернуться в '
                          f'окно выбора операций введите "стоп"')

            if num == 6:
                kg = input('Введите количество килограммов: ')
                if kg == 'стоп':
                    break
                elif float(kg) < 0:
                    print('Программа с отрицательными числами не работает. Попробуйте заново.')
                else:
                    kg = float(kg)
                    print(f'Количество фунтов = {kg_v_funt(kg)}. Если хотите вернуться в '
                          f'окно выбора операций введите "стоп"')

            elif num == 7:
                u = input('Введите количество унций: ')
                if u == 'стоп':
                    break
                elif float(u) < 0:
                    print('Программа с отрицательными числами не работает. Попробуйте заново.')
                else:
                    u = float(u)
                    print(f'Количество граммов = {unc_v_gr(u)}. Если хотите вернуться в '
                          f'окно выбора операций введите "стоп"')

            if num == 8:
                gr = input('Введите количество граммов: ')
                if gr == 'стоп':
                    break
                elif float(gr) < 0:
                    print('Программа с отрицательными числами не работает. Попробуйте заново.')
                else:
                    gr = float(gr)
                    print(f'Количество унций = {gr_v_unc(gr)}. Если хотите вернуться в '
                          f'окно выбора операций введите "стоп"')

            elif num == 9:
                g = input('Введите количество галлонов: ')
                if g == 'стоп':
                    break
                elif float(g) < 0:
                    print('Программа с отрицательными числами не работает. Попробуйте заново.')
                else:
                    g = float(g)
                    print(f'Количество литров = {gall_v_litr(g)}. Если хотите вернуться в '
                          f'окно выбора операций введите "стоп"')

            if num == 10:
                lt = input('Введите количество литров: ')
                if lt == 'стоп':
                    break
                elif float(lt) < 0:
                    print('Программа с отрицательными числами не работает. Попробуйте заново.')
                else:
                    lt = float(lt)
                    print(f'Количество галлонов = {litr_v_gall(lt)}. Если хотите вернуться в '
                          f'окно выбора операций введите "стоп"')

            elif num == 11:
                p = input('Введите количество пинты: ')
                if p == 'стоп':
                    break
                elif float(p) < 0:
                    print('Программа с отрицательными числами не работает')
                else:
                    p = float(p)
                    print(f'Количество литров = {pint_v_litr(p)}. Если хотите вернуться в '
                          f'окно выбора операций введите "стоп"')

            if num == 12:
                lit = input('Введите количество литров: ')
                if lit == 'стоп':
                    break
                elif float(lit) < 0:
                    print('Программа с отрицательными числами не работает. Попробуйте заново.')
                else:
                    lit = float(lit)
                    print(f'Количество пинты = {litr_v_pint(lit)}. Если хотите вернуться в '
                          f'окно выбора операций введите "стоп"')
        except(ValueError):
                print('Ошибка ввода. Пожалуйста, в выбранной вами операции '
                      'используйте только положительные целые (или дробные) '
                      'числа, либо слово "стоп", если хотите вернуться '
                      'в окно выбора операции. Попробуйте заново.')
