# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input('Введите значение X: '))
y = bool(input('Введите значение Y: '))
z = bool(input('Введите значение Z: '))

if not (x or y or z) == (not x and not y and not z):
    print ('True')
else:
    print('False')

# Вариант записи:
# x = bool(input('Введите значение X: '))
# y = bool(input('Введите значение Y: '))
# z = bool(input('Введите значение Z: '))

# if ~(x | y | z) == (~x & ~y & ~z):
#     print ('True')
# else:
#     print('False')