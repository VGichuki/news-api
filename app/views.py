from flask import render_template
from app import app

#Views
@app.route('/')
def index():
    '''
    View root page function that returns data from index.html
    '''
    return render_template('index.html')
    