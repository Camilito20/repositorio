def main():
    print('----- Меню -----')
    print('1. Вычислить х в ln(1+x)')
    print('2. Вычислить х в ln(1-x)')
    print('3. Выходить')
    respuesta = input('выбирайте вариант(1-3): ')

    if respuesta == '1':
        return exersice1()

    elif respuesta == '2':
        print('вторая функция')

    elif respuesta == '3':
        print('Выход....')

    else:
        print("\nВыбидайте вариант(1, 2 или 3)\n")
        return main()


def exersice1():
    x = float(input('''\nнаптшите ценность x в ln(x + 1)
число нужно (-1 < x <= 1): '''))
    N = 100
    if (-1 < x <= 1) == False:
        raise ValueError("число должен -1 < x <= 1)")

    suma = 0
    for n in range(1, N + 1):
        ecuacion = ((-1)**(n + 1) * (x ** n) / (n))
        suma += ecuacion

    print(f'Решении ln(x + 1) = {suma}')


if __name__ == "__main__":
    main()
