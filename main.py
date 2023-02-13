from flask import *
from random import choice

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
                <img src="{url_for('static', filename='images/mars_2.png')}" alt="Картинка Марса">
                <br>
                Вот онка какая, красная планета.
           '''


@app.route('/promotion_image')
def promotion_image():
    frases = ['Человечество вырастает из детства.',
              'Человечеству мала одна планета.',
              'Мы сделаем обитаемыми безжизненные пока планеты.',
              'И начнем с Марса!',
              'Присоединяйся!']
    div_types = ['primary', 'success', 'warning', 'danger']
    return f"""
    <!doctype html>
                <html lang="en">
                  <head>
                   <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <meta charset="utf-8">
                    <title>Марс</title>
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                  </head>
                  <body>
                    <h1>Привет, Марс!</h1>
                    <img src="{url_for('static', filename='images/mars_2.png')}" alt="Картинка Марса">
                    <br>
                    
                    {''.join(map(lambda x: f'<div class="alert alert-{choice(div_types)}" role="alert">' + x + "</div>",
                                 frases))}
                    
                  </body>
                </html>
            
            """


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
