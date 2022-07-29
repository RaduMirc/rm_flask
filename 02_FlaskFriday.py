# https://www.youtube.com/watch?v=0Qxtt4veJIc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz&ab_channel=Codemy.com

from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return "<h1>Hello world!</h1>"

# @app.route('/')
# def index():
#     fname = 'RM'
#     return render_template('index_02.html', first_name=fname)
@app.route('/')
def index():
    first_name="John"
    stuff="This is <strong>Bold</strong> Text"
    favorite_pizza=['Peperoni', 'Cheese', 42]
    return render_template('index_02.html',
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)

# http://localhost:5000/user/Radu
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)

