import re

def val_pas(passw):

    if len(passw) < 8:
        return False
    
    if not re.search(r'\d', passw):
        return False
    
    if not re.search(r'[a-zA-Z]', passw):
        return False
    
    if not (passw.startswith('+') or passw.endswith('+')):
        return False
    
    return True

#пример
passw = "+fgfgfWWW123"
passw = '-ghgghgfgffdftdx'

if val_pas(passw):
    print("Пароль кор")
else:
    print("Пароль некор")