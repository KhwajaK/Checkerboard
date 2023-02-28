from flask import Flask, render_template
app = Flask(__name__)  

@app.route('/')
def index():
    return render_template("index.html", row=8, col=8, color1='maroon', color2='midnightblue')

@app.route('/<int:a>')
def start(a):
    return render_template('index.html', row=a, col=8, color1='maroon', color2='midnightblue')

@app.route('/<int:a>/<int:b>')
def mid(a,b):
    return render_template('index.html', row=a, col=b, color1='maroon', color2='midnightblue')

@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'

if __name__=="__main__":
    app.run(port=8000, debug=True)  