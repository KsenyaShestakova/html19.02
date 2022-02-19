from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template('base1.html', title=title)


@app.route('/training/<profession>')
def prof(profession):
    if 'инженер' in profession.lower() or 'строитель' in profession.lower():
        return render_template('training.html',
                               title='InT',
                               image=url_for('static', filename='img/InT.png'))

    return render_template('training.html',
                            title='dr',
                            image=url_for('static', filename='img/dr.png'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')