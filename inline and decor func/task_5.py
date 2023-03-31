def countdawn(lis):
    lis = sorted(lis)
    lis = reversed(lis)
    lis = [str(i) for i in lis]
    p = 'Пуск!'
    lis.append(p)
    return lis
S=[0,7, 5, 9, 3, 8, 6, 2, 1]
print(*countdawn(S))