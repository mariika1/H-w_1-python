#№6Наибольшая подстрока палиндром.
def task6(s: str) -> int:
    for x in range(len(s), 0, -1): #выполним перебор значений в обратном порядке с конца строки (на каждой итерации смещаем начало палиндрома вправо)
        for i in range(len(s)+1 - x): #выполним перебор значений (для каждой левой границы палиндрома смещаем границу от самого правого значения до текущей левой границы )
            s_max = s[i:i + x] #записываем в s_max подстроку из s от левой до правой границы
            if s_max == s_max[::-1]:#проверка на палиндром (если s_max обратна себе же, то выводим длинну данной строки)
# т.к. границы с каждым шагом сужаются, то самый первый найденный палиндром будет самым большим
                return len(s_max)
    return 0
print(task6(input('введите строку s=').lower()))