from flask import Flask, render_template

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/user')
def userPage():
    return render_template('user.html')

myUsername = "giantsquid750@gmail.com"
myPassword = "giantsquidspassword"

@app.route('/login')
def loginPage():
    return render_template('login.html', showNavbar=False)

@app.route('/signup')
def signupPage():
    return render_template('signup.html', showNavbar=False)
