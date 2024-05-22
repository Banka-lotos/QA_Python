
def check_emails(email):


    #проверка на наличие собаки
    if '@' not in email:
        return False
    #делим адрес по символу собаки
    parts = email.split('@')


    #проверку н наличие логина и домена
    if len(parts) != 2:
        return False
   
    login,domain = parts[0],parts[1]


    #проверка длины логина
    if len(login) < 4:
        return False


    #проверка формата логина
    if not login or not login.replace('.','').isalnum():
        return False
   
    #проверка формы домена
    domain_par = domain.split('.')

    

print(check_emails('example@email.com')) # True
print(check_emails('invalid.email@domain'))  #False
print(check_emails('another.example@sub.domain.com'))  #True
print(check_emails('invalid_enother?@domain.name')) # false
print(check_emails('we@domain.name')) # false
