import pymysql
import pymysql.cursors
from main_confing_base import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('Success')
    print('#' * 30)

    try:
        with connection.cursor() as cursor:
            # Создание таблицы team
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS team (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    team_name VARCHAR(255) NOT NULL,
                    num_members INT CHECK (num_members <= 10)
                )
            """)
            print('Table "team" created successfully.')

    except Exception as e:
        print('An error occurred while executing SQL queries:')
        print(e)

    # Заполнение таблицы 10 командами
    try:
        with connection.cursor() as cursor:
            teams = [
                ("Дракончики 1", 10),
                ("Цветы 2", 10),
                ("Самолеты 3", 10),
                ("Одуваны 4", 10),
                ("Сантехники 5", 6),
                ("Водители 6", 10),
                ("Пилоты 7", 10),
                ("Авиаторы 8", 10),
                ("Матросы 9", 10),
                ("Механики 10", 10)
            ]

            insert_query = "INSERT INTO team (team_name, num_members) VALUES (%s, %s)"
            cursor.executemany(insert_query, teams)
            connection.commit()

            # Вывести в консоль все строки в которых количество участников будет выше 5 если таких нет выдать сообщение о том, что таких нет

            def print_teams_with_more_than_5_members(connection):
                try:
                    with connection.cursor() as cursor:
                        select_query = """
                        SELECT * FROM team WHERE num_members > 5
                        """
                        cursor.execute(select_query)
                        teams = cursor.fetchall()
                        if teams:
                            print("Команды с более чем 5 уч:")
                            for team in teams:
                                print(team)
                        else:
                            print("Команд с более чем 5 уч не найдено.")

                except Exception as e:
                    print('Ошибка при получении данных:')
                    print(e)

            # Вызов функции для вывода команд с более чем 5 участниками
            print_teams_with_more_than_5_members(connection)

             # Создание представления для таблицы user
            try:
                cursor.execute("""
                    CREATE OR REPLACE VIEW users_a_or_b AS
                    SELECT * FROM user WHERE name LIKE 'А%' OR name LIKE 'Б%' 
                """)
                print('Представление "users_a_or_b" создано')
            except Exception as e:
                print('представление не создано:')
                print(e)


    except Exception as e:
        print('An error occurred while inserting data:')
        print(e)

finally:
    if connection:
        connection.close()
        print('Connection closed.')