# Задание 1
# from datetime import datetime as dt, timedelta
# def working_hours_only(func):
#     def wrapper():
#         if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 18):
#             func()
#         else:
#             print('Работать нельзя!')
#     return wrapper
#
# @working_hours_only
# def work():
#     print('Работаем')

# work()

# Задание 2
def type_check(correct_type):
    def type_main(type_x):
        def wrapper(arg):
            if type(arg) == correct_type:
                return type_x(arg)
            else:
                return 'Bad type'
        return wrapper
    return type_main

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
print(times2(True))

@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(1.5))
