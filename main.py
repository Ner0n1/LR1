#Веб-сервере на питоне
# Импорт библиотеки flask для работы веб-сайта
from flask import Flask, render_template, url_for, abort, request


main = Flask(__name__)

#Секция разрешённых путей на сайте
@main.route('/')
def index():
    return render_template("index.html")


@main.route('/login')
def login_page():
    return render_template("login.html")

#Секция проверки пароля
@main.route('/signin', methods=['POST','GET'])
def signin_page():
    #Если метод POST, то пускаем, если GET, то код 405
    if request.method == 'POST':
        #Подхватываем логин/пароль со страницы login.html
        user = request.form.get('user')
        password = request.form.get('pass')
        #Если логин или пароль пустые, то код 400
        if user == '' or password == '':
            abort(400)
        #Если файла нет logins.txt, то код 500
        try:
            login = open('logins/logins.txt','r')
        except FileNotFoundError:
            abort(500)
        #Проверка по каждой строке в файле login.txt
        for line in login:
            #Разделение линии по двоеточию
            uspas = line.split(':')
            #Проверка имени пользователя
            if user == uspas[0]:
                #Проверка правильности пароля, если неправильный, то код 403
                if password == uspas[1][:-1]:
                    login.close()
                    #Переход на страницу входа
                    return render_template("/signin/signin.html")
                else:
                    abort(403)
                    login.close()
        #Если пользователь не найден, то код 403
        abort(403)
        login.close()
    if request.method == 'GET':
        abort(405)


#Запуск сервера на любом доступном IP, на порту 8080, без дебага
if __name__ == "__main__":
    main.run(host='0.0.0.0', port=8080, debug=False)

