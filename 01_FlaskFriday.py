# https://www.youtube.com/watch?v=0Qxtt4veJIc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz&ab_channel=Codemy.com

from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return "<h1>Hello world!</h1>"

@app.route('/')
def index():
    return render_template('index_01.html')

# http://localhost:5000/user/Radu
@app.route('/user/<name>')
def user(name):
    return "<h1>Hello {}!</h1>".format(name)

