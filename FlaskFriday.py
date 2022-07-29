# https://www.youtube.com/watch?v=0Qxtt4veJIc&list=PLCC34OHNcOtolz2Vd9ZSeSXWc8Bq23yEz&ab_channel=Codemy.com

from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='SUper Secret Key'


class NameForm(FlaskForm):
    name = StringField('Cum te cheama', validators=[DataRequired()])
    submit = SubmitField('Submit')




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
    return render_template('index.html',
                           first_name=first_name,
                           stuff=stuff,
                           favorite_pizza=favorite_pizza)


# http://localhost:5000/user/Radu
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data=''
    return render_template('name.html',
                           name=name,
                           form=form)