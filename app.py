from flask import Flask, render_template
from flask import make_response
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class NameForm(FlaskForm):
    submit = SubmitField('Submit')
    name = StringField('Qual o seu nome?', validators=[DataRequired()])



app = Flask(__name__)
app.config['SECRET_KEY'] = 'chave_secreta'
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.route('/', methods=['GET', 'POST'])
def index():
	name = None
	form = NameForm()
	if form.validate_on_submit():
			name = form.name.data
			form.name.data = ''
	return render_template('index.html',form=form, name=name, current_time=datetime.utcnow())
	

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)


@app.route('/teste')
def teste():
	response = make_response('<h1>Este doc carrega um cookie </h1>')
	response.set_cookie('answer', '42')
	return response


@app.errorhandler(404)
def page_not_found(e):
    	return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    	return render_template('500.html'), 500



app.run(debug=True)
