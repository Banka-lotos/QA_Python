import re


user_database = {
    "user1@example.com": {'name':'User', 'password': 'Qwe12343r'},
    "user2@example.com": {'name':'Vasya', 'password': 'Qwe12343r'},
    "user3@example.com": {'name':'Petya', 'password': 'Qwe12343r'},
    "user4@example.com": {'name':'Sereja', 'password': 'Qwe12343r'},
}

#проверка почты
def reg(name, password, email):

    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            return "Email неккоректен"
        
    if email in user_database:
       return ('почта существ')
 
 #проверка имени
    if not name:
        return 'поле с именем обязательно'

 #проверка пароля
    def password(passw):
      return len(password) >= 8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password) and any(char in "!@#$%^&*()_+=-" for char in password)


    user_database[email]  
    return f"Пользователь {name} зарегистрирован"


# регитсрация
   
 
name = input("Введите ваше имя: ") 
email = input("Введите ваш email: ") 
password = input("Введите ваш пароль: ") 
 
result = reg(name, email, password) 
print(result)


