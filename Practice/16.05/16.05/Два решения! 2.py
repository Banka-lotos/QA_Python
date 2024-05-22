 #для циклов!
def is_uniq(lst):
    #пройтись по всем элементам списка
    for i in range(len(lst)):
        #сравнить текущий элемент с остальными элементами списка
        for j in range(i+1,len(lst)):
            if lst[i] == lst[j]:
                return False
    return True


print(is_uniq([1,2,3,4,5]))
print(is_uniq([1,2,3,4,5,1]))
  

  #для множества!
def is_uniq(lst):
   
    uniq_set = set(lst)


    return len(uniq_set) == len(lst)


print(is_uniq([1,2,3,4,5]))
print(is_uniq([1,2,3,4,5,1]))
