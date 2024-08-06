
import webbrowser
def authenticate(username, password):
    def real_decorator(func):
        def inner(*args):
            if username == 'metronidazol' and password == 'python_2024':
                return func()
            else:
                print('Ошибка аутенфитикации')
                webbrowser.open('https://static1.makeuseofimages.com/wordpress/wp-content/uploads/2017/02/Fix-Access-Denied-Folder-Featured.jpg?q=50&fit=crop&w=1100&h=618&dpr=1.5')
        return inner
    return real_decorator

username = input('Введите имя пользователя: ')
password = input('Введите пароль для входа: ')

@authenticate(username, password)
def some_hiden_function():
    print('Функция выполняется, пароль и имя пользователя верны')
    webbrowser.open('https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/Access-granted.png/800px-Access-granted.png?20170817133601')
some_hiden_function()