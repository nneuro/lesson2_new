'''
#Задание
#Напишите функцию get_summ(num_one, num_two), которая принимает 
# на вход два целых числа (int) и складывает их
#Оба аргумента нужно приводить к целому числу при помощи
#  int() и перехватывать исключение ValueError если приведение 
# типов не сработало
'''

def get_summ(num_one, num_two):
    try:
        num_one = int(num_one)
        num_two = int(num_two)
        summ = num_one + num_two
        return summ
    except ValueError:
        return 'Измените в программе значение переменной'

a = get_summ(3,1)
print(a)

b = get_summ('s',1)
print(b)
