from flask import Flask
from flask import render_template


app=Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/hireme')
def hireme():
    return render_template('hireme.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

if __name__ == '__main__':
    app.run(debug=False)

