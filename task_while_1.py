'''
# Напишите функцию ask_user(), которая с помощью 
# input() спрашивает пользователя “Как дела?”, 
# пока он не ответит “Хорошо”
'''

def ask_user():
    while True:
        user_say = input('Как дела? ')
        if user_say == 'Хорошо':
            break
    return('Ну и отлично!')

ask=ask_user()
print(ask)

