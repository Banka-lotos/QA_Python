import random
import string

def gener_password(len=8, upper=True, lower=True, digits=True, symvol=True):
    len = random.randint(8,32)
    
    chars = ''    
    if upper:
        chars += string.ascii_uppercase
    if lower:
            chars += string.ascii_lowercase
    if digits:
            chars += string.digits
    if symvol:     
          chars += string.punctuation  

    passw = ''.join(random.choice(chars) for _ in range(len))
    return passw


print(gener_password())




