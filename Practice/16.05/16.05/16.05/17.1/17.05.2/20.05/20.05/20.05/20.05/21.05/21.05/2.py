

telkniga = {}


def contakt(telbook):
    print("Тел книга:")
    if not telbook:
        print("Книга пуста.")
    else:
        for name, nomer in telbook.items():
            print(f"Имя: {name}, Номер тел: {nomer}")


while True:
    print("\nМеню:")
    print("1. Просмотреть тел книгу")
    print("2. Добавить контакт")
    print("3. Выйти")
    choice = input("Выберите действие (1, 2, 3): ")

    if choice == '1':
        contakt(telkniga)
    elif choice == '2':
        name = input("Введите имя: ")
        
        if name in telkniga:
            print("Имя уже сущ")
            continue
        
        nomer = input("Введите номер тел: ")

        if any(nomer == existing_nomer for existing_nomer in telkniga.values()):
            print("Номер уже сущ")
            continue

        telkniga[name] = nomer
        print("Контакт добавлен")

    elif choice == '3':
        print("Выход из программы.")
        break
    else:
        print("Выберите действие")





