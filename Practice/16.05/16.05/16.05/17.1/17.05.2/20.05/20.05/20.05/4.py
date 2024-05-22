

def val_email(email):
    if '@' not in email:
        return False
    
    if '.' not in email:
        return False
    
    if email.index('@') >= email.index('.'):
        return False
    return True

#пример
email = "example@example.com"
#email = 'example.com'

if val_email(email):
    print("Email TRUE")
else:
    print("Email FALSE")