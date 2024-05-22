

#def validate_phone_num(phone_num):
   
    #if phone_num[0] != '+':
     #   return False
    
    #for char in phone_num[1:]:
        #if not char.isdigit():
            #return False
    
    #if len(phone_num) != 12:
       # return False
    #return True

#phone_num = "+12345678912"

#if validate_phone_num(phone_num):
 #   print("Номер телефона корректен!")
#else:
 #   print("Номер телефона некорректен!")


#Второй вариант
import re


def valid_num(num):


    phone_pattern = r'^\+\d{11}$'


    if re.match(phone_pattern, num):
        return True
    else:
        return False

