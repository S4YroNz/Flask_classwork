from flask import *
from random import choice

app = Flask(__name__)





@app.route('/')
@app.route('/index')
def index():
    title = "Миссия"
    return render_template('base.html', title=title)


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


@app.route('/astronaut_selection')
def astronaut_selection():
    def create_check_boxes():
        res = ''
        works = ['Инженер-исследователь',
                 'Инженер-строитель',
                 'Пилот',
                 'Метеоролог',
                 'Инженер по жизнеобеспечению',
                 'Инженер по радиационной защите',
                 'Врач',
                 'Экзобиолог']
        for i in range(len(works)):
            res += f'''<input class="form-check-input" type="checkbox" id="gridCheck{i + 1}">
                        <label class="form-check-label" for="gridCheck{i + 1}">
                          {works[i]}
                        </label>\n
                        '''
        return res
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
                    <h1>Анкета претендента</h1>
                    <h2>на участие в миссии</h2>
                    <div id="form-div">
                    <form id="main-form">
                    <div class="row mb-3">
                          <input type="text" class="form-control" id="inputSurname" placeholder="Введите Фамилию">
                      </div>
                      <div class="row mb-3">
                          <input type="text" class="form-control" id="inputName" placeholder="Введите имя">
                      </div>
                      <br>
                      <div class="row mb-3">
                          <input type="email" class="form-control" id="inputEmail" placeholder="Введите адрес почты">
                      </div>
                      <div class="row mb-3">
                        <label for="inputState" class="form-label">Какое у Вас образование?</label>
                        <select id="inputState" class="form-select">
                          <option selected>Начальное</option>
                          <option>Среднее</option>
                          <option>Высшее</option>
                        </select>
                      </div>
                      <div class="row mb-3">
                      <label for="form-check" class="form-label">Какие у Вас есть профессии?</label>
                      <div class="form-check">
                      
                        {create_check_boxes()}
                        
                      </div>
                      
                      </div>
                      <fieldset class="row mb-3">
                        <legend class="col-form-label col-sm-2 pt-0">Radios</legend>
                        <div class="col-sm-10">
                          <div class="form-check">
                            <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios1" value="option1" checked>
                            <label class="form-check-label" for="gridRadios1">
                              First radio
                            </label>
                          </div>
                          <div class="form-check">
                            <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios2" value="option2">
                            <label class="form-check-label" for="gridRadios2">
                              Second radio
                            </label>
                          </div>
                          <div class="form-check disabled">
                            <input class="form-check-input" type="radio" name="gridRadios" id="gridRadios3" value="option3" disabled>
                            <label class="form-check-label" for="gridRadios3">
                              Third disabled radio
                            </label>
                          </div>
                        </div>
                      </fieldset>
                      <div class="row mb-3">
                        <div class="col-sm-10 offset-sm-2">
                          <div class="form-check">
                            <input class="form-check-input" type="checkbox" id="gridCheck1">
                            <label class="form-check-label" for="gridCheck1">
                              Example checkbox
                            </label>
                          </div>
                        </div>
                      </div>
                      <button type="submit" class="btn btn-primary">Sign in</button>
                    </form>
                    </div>
                  </body>
                </html>

            """

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
