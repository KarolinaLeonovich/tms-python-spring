# Задание 8.2:
# Даны три слова. Выяснить, является ли хоть одно из них палиндромом
# ("перевертышем"), т. е. таким, которое читается одинаково слева направо и
# справа налево. (Определить функцию, позволяющую распознавать слова
# палиндромы.)

def palindrom_check(word_string):
    if word_string == word_string[::-1]:
        print("Введенное слово является палиндромом")
    else:
        print("Это не палиндром!")


string_to_check = input("Введите слово для проверки: ")
palindrom_check(string_to_check)
