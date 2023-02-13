from flask import *

app = Flask(__name__)


@app.route('/')
def main():
    return '<b>Миссия Колонизация Марса</b>'


@app.route('/index')
def index():
    return '<b>И на Марсе будут яблони цвести!</b>'


@app.route('/promotion')
def promotion():
    frases = ['Человечество вырастает из детства.',
              'Человечеству мала одна планета.',
              'Мы сделаем обитаемыми безжизненные пока планеты.',
              'И начнем с Марса!',
              'Присоединяйся!']
    return '<br>'.join(map(lambda x: '<b>' + x + '</b>', frases))


@app.route('/image_mars')
def image_mars():
    return f'''<h1>Привет, Марс!</h1>
                <img src="{url_for('static', filename='images/mars.png')}" alt="Картинка Марса">
                <br>
                Вот онка какая, красная планета.
           '''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
