
#первый вариант
#def count_letters(text): 
    #count = {}  # словарь 
    #for a in text: 
        #if a.isalpha(): 
            #if a in count: 
                #count[a] += 1 
            #else: 
                #count[a] = 1 
     
    #return count 
 
#text = input ('введи строку :')
#result = count_letters (text) 
#print(result)


#второй вариант
def count_letters(word):
    letter_count = {}
    for i in word:
        if i.isalpha():
            i  = i.lower()
            letter_count[i] = letter_count.get(i,0) +1
    return letter_count


word = input()
print(count_letters(word))