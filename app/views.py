from app import app
from flask import render_template

# @app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    # return 'hello'

@app.route('/demo_page1')
def demo_page1():
    return render_template('demo_page1.html')
