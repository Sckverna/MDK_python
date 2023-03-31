import string
'''def alphabet():  (a)
    alpha = list(string.ascii_lowercase)
    for i in range(len(alpha)):
        print(f"буква - {alpha[i]}, порядковый номер - {i+1}")
alphabet()'''

def alphabet():     #(б)
    alpha = list(string.ascii_lowercase)
    dic = {}
    for i in range(len(alpha)):
        dic[i+1] = alpha[i]
    print(dic)
alphabet()