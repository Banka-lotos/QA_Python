
import random   
 
def generate(file_path): 
    with open (r"c:\Users\AttekPC\Desktop\Новый текстовый документ.txt",'r', encoding='utf-8') as file:
        a = file.read().splitlines() 
    return random.choice(a) if a else 'пустой файл' 
 
 
file_path = r"c:\Users\AttekPC\Desktop\Новый текстовый документ.txt"
print(generate(file_path))








