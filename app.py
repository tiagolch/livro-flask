from flask import Flask

app = flask(__name__)

@app.route('/')
def index():
	return '<h1>teste</h1>'