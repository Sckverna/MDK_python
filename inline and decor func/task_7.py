def hello(func):
    def wrapper(*args, **kwargs):
        n = func(*args)
        print(f"привет,{n}!")
        return n
    return wrapper()
@hello
def get_name( ):
    name = input('Введите имя')
    return name