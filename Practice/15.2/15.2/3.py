try:
    with open (r"c:\Users\AttekPC\Desktop\Новый текстовый документ.txt",'r', encoding='utf-8') as file:
     print(file.read())
except FileNotFoundError:
    print('ошибка открытия файла')