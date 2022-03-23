from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from werkzeug.utils import redirect
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    id_astronaut = StringField('ID астронавта', validators=[DataRequired()])
    password_astronaut = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_capitan = StringField('ID капитана', validators=[DataRequired()])
    password_capitan = StringField('Пароль капитана', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<profession>')
def prof(profession):
    if 'инженер' in profession.lower() or 'строитель' in profession.lower():
        return render_template('training.html',
                               title='InT',
                               image=url_for('static', filename='img/InT.png'))

    return render_template('training.html',
                            title='dr',
                            image=url_for('static', filename='img/dr.png'))


@app.route('/list_prof/<parameter>')
def print_prof(parameter):
    professions = ["инженер-исследователь",
                    "пилот",
                    "строитель",
                    "экзобиолог",
                    "врач",
                    "инженер по терраформированию",
                    "климатолог",
                    "специалист по радиационной защите",
                    "астрогеолог",
                    "гляциолог",
                    "инженер жизнеобеспечения",
                    "метеоролог",
                    "оператор марсохода",
                    "киберинженер",
                    "штурман",
                    "пилот дронов"]
    return render_template('pr.html',
                           list_type=parameter,
                           list_prof=professions)


@app.route('/answer')
@app.route('/auto_answer')
def dsf():
    sl = {
        "title": 'dgs',
        "surname": 'sdfs',
        "name": 'fsdf',
        "education": 'dfsfd',
        "profession": 'fsf',
        'sex': 'dfsd',
        'motivation': 'fsf',
        'ready': 'fsdf'
    }
    return render_template('answer.html',
                           title=sl['title'],
                           surname=sl['surname'],
                           name=sl['name'],
                           education=sl['education'],
                           profession=sl['profession'],
                           sex=sl['sex'],
                           motivation=sl['motivation'],
                           ready=sl['ready'])


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Аварийный доступ', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')