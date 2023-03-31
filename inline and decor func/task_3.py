def honnest(lis):
    return lis % 2 == 0
ls = [int(i) for i in range(21)]
print(*filter(honnest,ls))