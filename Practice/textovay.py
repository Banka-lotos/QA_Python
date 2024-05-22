
with open (r"c:\Users\AttekPC\Desktop\Новый текстовый документ.txt",'r', encoding='utf-8') as file:
     

     text = (file.read())
if 'Рэдрик' in text:
        print('слово найдено')
else:
        print('слово не найдено')

    

