#№5Палиндром.
def task5(s: str) -> bool:

    m=s[::-1] # m - обратная строка для s
    if s==m: # сравним изначальную строку s и обратную m
        return True
    else:
        return False
print(task5(input('введите строку s=')))