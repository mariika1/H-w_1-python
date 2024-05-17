#№3Возрастает ли список?
from typing import List

def task3(n: List[int]) -> bool:
    
    s=sorted(n) # отсортируем список в порядке возрастания
    if n==s:# проверяем возрастает ли список n
        i=0
        j=1
        n_1=True
        while j<=len(n)-1:
            if n[i]==n[j]: # проверяем нет ли одинаковых чисел идущих подряд
                n_1=False
                break
            i+=1
            j+=1
        return n_1
    else:
        return 'False'
print(task3([int (i) for i in input('введите список целых чисел n= ').split()]))