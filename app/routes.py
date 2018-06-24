from flask import render_template
from app import app



@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Catherine'}
    posts = [
        {'author': {'username':'Cat'},
        'body': 'hello world'
         },
        {
            'author':{'username':'quinoa'},
            'body':'s;dflkajsd'
            }
        ]
    #rendere_template('file', extravariablesyouwanttoinherit)
    return render_template('index.html', title='Home', user=user, posts=posts) #user=user lets user var here be inherited


@app.route("/members")
def members(): 
    return "Members"
