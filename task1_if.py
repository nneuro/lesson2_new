
def age_stage(age):
    if 3 <= age < 7:
        life_stage = 'тебе надо быть в детском саду'
    elif 7 <= age <= 17:
        life_stage = 'тебе надо бы учиться в школе'
    elif 18 <= age <= 23:
        life_stage = 'в таком возрасте все учатся в ВУЗе'
    elif age >= 24:
        life_stage = 'в таком возрасте нормальные люди работают'
    life_stage_out=f'Уважаемый пользователь, {life_stage}'
    return life_stage_out

    
age = int(input('Введите ваш возраст: '))
print(age_stage(age))