import random

joke_template = [
    'Почему %s перешел дорогу?',
    'Потому что %s смеются над ним!',
    'Кто %s в книгах?',
    'Кто %s?',
    'Что сказал %s ему %s когда они встретились?'
]

joke_elements = [
    'слон','заяц','бетмен','крокодил','чебурашка','студент','препод',
    'водитель','улитка'
]

def generate_joke():
    template = random.choice(joke_template)
    if '%' in template:
        return template % tuple(random.sample(joke_elements, template.count('%s')))
    else:
        return template

if __name__ == "__main__":
    for _ in range(8):  # Генерируем  шуток
        print(generate_joke())