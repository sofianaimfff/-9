# 4. Пользователь вводит время в часах. Если введенное число находится между 5 и 11
# часами вĸлючительно, выведите строĸу 'Утро'. Если число лежит в диапазоне от 12
# до 17 часов вĸлючительно, выведите строĸу 'День'. Если число находится между 18 и
# 22, то выведите 'Вечер'. В случае поздней ночи (от 23 до 4 вĸлючительно) выведите
# 'Ночь'. В остальных случаях выведите строĸу 'Ошибĸа'.

x = int(input("Введите время на часах: "))
if 5 <= x <= 11:
    print("Утро")
elif 12 <= x <= 17:
    print("День")
elif 18 <= x <= 22:
    print("Вечер")
elif 00 <= x <= 23:
    print("Ночь")
else:
    print("Ошибка")