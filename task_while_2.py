'''
# Создайте словарь типа "вопрос": "ответ", например:
#  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} 
# и так далее
# Доработайте ask_user() так, чтобы когда пользователь вводил вопрос который есть в словаре, программа давала ему соотвествующий ответ. Например:
# Пользователь: Что делаешь?
# Программа: Программирую
'''

dict_ask_question = {
    'Как дела?': 'Хорошо!',
    'Что делаешь?' : 'Программирую',
    'Кто тебя придумал?' : 'Я сам себя придумал'
}

def ask_user():
    while True:
        user_say = input('Программа: спроси меня что нибудь или скажи "Пока"\nПользователь: ')
        key_list = dict_ask_question.keys()
        if user_say in key_list:
            print(dict_ask_question.get(user_say))
        elif user_say == 'Пока':
            break
    return('До встречи!')

ask=ask_user()
print(ask)