def func_string(string_1, string_2):
    if type(string_1) != str or type(string_2) != str:
        return 0
    elif string_1 == string_2:
        return 1
    elif string_1 != string_2 and len(string_1) > len(string_2):
        return 2
    elif string_1 != string_2 and string_2 == 'learn':
        return 3


print(func_string(1, 'b'))
print(func_string('b', 'b'))
print(func_string('asd', 'b'))
print(func_string('a', 'asd'))
print(func_string('a', 'learn'))