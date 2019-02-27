'''
# Создать список из словарей с оценками учеников разных классов школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.
'''


score_list = [
    {'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '5a', 'scores': [2,5,3,2,4]},
    {'school_class': '6a', 'scores': [3,5,4,5,4]}
]


for a in score_list:
    b=a['scores']
    mean=sum(b)/len(b)
    c=a['school_class']
    print(f'Класс {c}, средний балл {mean}')

all=[]   
for a in score_list:
    b=a['scores']
    for el in b:
        all.append(el)
mean_school = sum(all)/len(all)
mean_school = "%.1f" % mean_school
print(f'Средний балл по школе составляет {mean_school}')






