from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
if __name__=='_main_':
    app.run(debug=true,host='0.0.0.0,port=5000')
