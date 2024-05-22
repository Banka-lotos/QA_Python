
vopros = {
    "Какая американская поп-группа 1960-х годов создала «саунд серфинга?": "Beach Boys",
    "В каком году был выпущен Крестный отец?": "1972",
    "Мастера монет Лорда Петра Баелиша также знали под каким именем?": "Мезинец",
    "Сколько сердец у Осьминога?": "Три"
}



def victorina(vopros):
    score = 0
    n = len(vopros)

    for i, (vopros, besst) in enumerate(vopros.items(), start=1):
        print(f"Вопрос {i}: {vopros}")
        user_answer = input("Введите ответ: ")

        if user_answer.lower() == besst.lower():
            print("верно")
            score += 1
        else:
            print(f"Неверно! Ответ: {besst}")

    print(f"Конец! Счет: {score}/{n}")


# пуск
victorina(vopros)