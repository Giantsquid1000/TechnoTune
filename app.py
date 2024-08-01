from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def hello_world():
    return render_template('template.html')

@app.route('/login')
def loginPage():
    return render_template('login.html')