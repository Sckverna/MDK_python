def calculator(num1,num2,oper):
    try:
        return eval(f'{num1}{oper}{num2}')
    except:
        return "ошибка! на 0 делить нельзя."
num1,oper,num2 = input().split()
print(calculator(num1,num2,oper))