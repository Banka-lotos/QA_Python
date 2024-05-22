

def search(sentence, word): 
    return word in stroka 
stroka = 'питон, тумбочка, ручка, планета' 
i = 'питон' 
 
if search(stroka, i): 
    print(f"Слово '{i}' найдено в строке.") 
else: 
    print(f"Слово '{i}' не найдено в строке.")