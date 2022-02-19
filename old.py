from flask import request, url_for, Flask

app = Flask(__name__)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style_form.css')}" />
                            <title>Пример формы</title>
                          </head>
                          <body>
                            <h1 align="middle">Анкета претендента</h1>
                            <h2 align="middle">на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" aria-describedby="surnameHelp"
                                    placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" aria-describedby="namelHelp"
                                    placeholder="Введите имя" name="name">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp"
                                    placeholder="Введите адрес электронной почты" name="email">
                                    <div class="form-group">
                                        <label for="eduSelect">Какое у вас образование?</label>
                                        <select class="form-control" id="classSelect" name="edu">
                                          <option>Базовое</option>
                                          <option>Среднее общее</option>
                                          <option>Среднее специальное</option>
                                          <option>Среднее полное</option>
                                          <option>Высшее</option>
                                          <option>Наивысшее</option>
                                        </select>
                                     </div>
                                    <label for="profSelect">Какие у Вас есть профессии?</label>
                                    <div class="form-group form-check">
                                      <input type="checkbox" class="form-check-input" id="prof" name="prof">
                                      <label class="form-check-label" for="acceptRules">инженер-исследователь</label>
                                      <br>
                                      <input type="checkbox" class="form-check-input" id="prof" name="prof1">
                                      <label class="form-check-label" for="acceptRules">пилот</label>
                                      <br>
                                      <input type="checkbox" class="form-check-input" id="prof" name="prof2">
                                      <label class="form-check-label" for="acceptRules">учитель</label>
                                      <br>
                                      <input type="checkbox" class="form-check-input" id="prof" name="prof3">
                                      <label class="form-check-label" for="acceptRules">астролог</label>
                                      <br>
                                      <input type="checkbox" class="form-check-input" id="prof" name="prof4">
                                      <label class="form-check-label" for="acceptRules">врач</label>
                                      <br>
                                      <input type="checkbox" class="form-check-input" id="prof" name="prof5">
                                      <label class="form-check-label" for="acceptRules">оператор-марсохода</label>                                            
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Зачем вам все это????</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        print(request.form)
        print(request.form.get('surname', None))
        print(request.form.get('name', None))
        print(request.form.get('email', None))
        print(request.form.get('edu', None))
        print(request.form.get('file', None))
        print(request.form.get('about', None))
        print(request.form.get('sex', None))
        print(request.form.get('prof', None))
        print(request.form.get('prof1', None))
        print(request.form.get('prof2', None))
        print(request.form.get('prof3', None))
        print(request.form.get('prof4', None))
        print(request.form.get('prof5', None))
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')