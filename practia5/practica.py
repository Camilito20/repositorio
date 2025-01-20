def main():
    print('----- Меню -----')
    print('1. Вычислить х в ln(1+x)')
    print('2. Вычислить х в ln(1-x)')
    print('3. Выходить')
    respuesta = input('выбирайте вариант(1-3): ')

    if respuesta == '1':
        print('1')

    elif respuesta == '2':
        print('второе задание')

    elif respuesta == '3':
        print('Выход....')

    else:
        print("\nВыбидайте вариант(1, 2 или 3)\n")
        return main()


if __name__ == "__main__":
    main()
