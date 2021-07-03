from flask import Flask, render_template
from flask import make_response
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
	return render_template('index.html')
	

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
