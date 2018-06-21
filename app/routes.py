from app import app

#decorators
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Catherine'}
    return '''

<html>
    <head>
        <title>Home Page - Microblog </title>
    </head>

    <body>
        <h1>Hello,''' + user['username'] + '''!</h1>
    </body> 
</html>
'''
