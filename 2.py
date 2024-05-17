#№2 Наибольшее произведение трех чисел.
from typing import List

def task2(n: List[int]) -> List[int]:
   
#находим 3 наибольших числа из введенного списка n :
    s_1=sorted(n) # отсортируем список в порядке возрастания
    n_1=[] #создадим пустой список
    n_1.append(s_1[-1]) # запишем в список n_1 максимальное число 
    n_1.append(s_1[-2])
    n_1.append(s_1[-3]) 
#находим 3 наименьших числа из введенного списка n :
    s_12=min(n)# находим минимальное число из списка n
    n.remove(s_12)# удаляем минимальное число из списка n
    s_22=min(n)# находим минимальное число в обновленном списке n
    s_32=max(n)
    n_2=[]
    n_2.append(s_12) #запишем в список n_2 минимальное значение  из списка n
    n_2.append(s_22)
    n_2.append(s_32)
    if s_1[-1] * s_1[-2]* s_1[-3] > s_12 * s_22 * s_32 : #проверяем какое произведение чисел больше, 3-х наибольших или 3-х наименьших
        return n_1
    else:
        return n_2
print(task2([int (i) for i in input('введите список целых чисел n= ').split()]))