import time 
from threading import Thread
import random

def input_data_generation(quantaty, a, b):
    #Функция генерирует входные данные, кол-во чисел равно quantaty, числа случайны - из промежутка от a до b
    input_data = []
    for i in range(quantaty):
        number=random.randint(a, b)
        input_data.append(number)
    print(input_data)
    return input_data

def long_process(id, start_number, end_number, input_data, result):
    #Функция суммирует отдельные элементы массива input_data начиная с номера start_number и заканчивая номером end_number. Результат возвращается в словаре result с номером id 
    sum = 0
    for x in range(start_number, end_number):
        sum += input_data[x]
        time.sleep(0.05)
    result[id] = sum

def sum_by_threads(thread_quantaties, input_data):
    #Функция получает на вход кол-во потоков заданное thread_quantaties, каждый поток суммирует свой участок во входных данных input_data
    output_res = 0
    result = {}
    threads = []
    start_number = 0
    q_ty = len(input_data)
    q_ty_of_number_for_each_thread=int(q_ty/thread_quantaties)
    for every_process in range(thread_quantaties):
        threads.append(str("thread" + "_" + str(every_process)))
    for every_thread in range(thread_quantaties):
        end_number = start_number+q_ty_of_number_for_each_thread
        if end_number > q_ty-1:
            end_number = q_ty
        threads[every_thread] = Thread(target = long_process, name = "Thread N "+ str(every_thread), args = ("ID" + str(every_thread), start_number, end_number, input_data, result))
        start_number = end_number
    for i in range(len(threads)):
        threads[i].start()  
    while True == True:
        flag = True
        for every_status in range(len(threads)):
            if threads[every_status].is_alive() == True: 
                flag = False
                time.sleep(0.1)               
        if flag == True:
            break
    for key in result:
        output_res += result[key]
    print(result)
    print(output_res)
    return output_res
    
def just_sum (input_data):
    #Обычное суммирование
    res=0
    for i in range(len(input_data)):
        res += input_data[i]
    print(res)
    return res

def test ():
    #Проверка корректности суммирования
    data_gen=input_data_generation(1000, 1, 10)
    res_by_threds = sum_by_threads(10, data_gen)
    ordinary_sum = just_sum(data_gen)
    if res_by_threds == ordinary_sum:
        print("Success")
    else:
        print("Bad result")


test()








