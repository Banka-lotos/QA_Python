def check_email_format(email):
    if "@" not in email:
        return False
    
    parts = email.split("@")
    if len(parts) != 2:
        return False
    
    username, domain = parts
    if len(username) < 6:
        return False
    
    if not all(char.isalnum() or char in ['.', '_', '-'] for char in username):
        return False
    
    if "." not in domain:
        return False
    
    domain_name, extension = domain.split(".")
    if not all(part.isalnum() for part in [domain_name, extension]):
        return False
    
    return True

print(check_email_format('example@email.com')) # True
print(check_email_format('invalid.email@domain'))  #False
print(check_email_format('another.example@sub.domain.com'))  #True
print(check_email_format('invalid_enother?@domain.name')) # false
print(check_email_format('we@domain.name')) # false
