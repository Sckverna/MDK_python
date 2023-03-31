def decor(func):
    def wrapper(*args, **kwargs):
        n = func(*args)
        return f'<p>{n}</p>'
    return wrapper
@decor
def render_input(field):
    return f'<input id="id_{field}" name="{field}">'

username = render_input('username')
print(username)