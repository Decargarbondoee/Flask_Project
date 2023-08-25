from app import app

@app.route('/')
@app.route('/index')
#def index():
    #return 'Hello World!!'

def index():
    user = {'username': 'Emmett'}
    return '''
    <html>
        <head>
            <title>Home Page - CS Academy</title>
        </head>
        <body>
            <h1>Hello ''' + user['username'] + '''!</h1>  
        </body>
    </html>