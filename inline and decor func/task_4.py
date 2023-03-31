def cesar(str):
    lis = []
    s = []
    for enum in str:
        for i in enum:
            num = ord(i)
            num+=3
            num = chr(num)
            s.append(num)
        lis.append(s)
    return lis
print("введите строку")
str = input().split()
print(cesar(str))