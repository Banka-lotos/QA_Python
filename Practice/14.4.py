def chek_password(password):
    if len(password) < 8:
        return False
    
    strochnye = any(h.islower() for h in password)
    zaglavnye = any(h.isupper() for h in password)
    digit = any(h.isdigit() for h in password)

    return strochnye and zaglavnye and digit


print(chek_password('Abcd1234')) 
print(chek_password('abcD'))  
print(chek_password('ABCD1234'))
print(chek_password('2121ghfgjh'))
