from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def homePage():
    return render_template('home.html')

@app.route('/user')
def userPage():
    return render_template('user.html')

myUsername = "giantsquid750"
myPassword = "giantsquidspassword"

@app.route('/login')
def loginPage():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == myUsername and password == myPassword:
            return render_template('home.html')
        else:
            return render_template("user.html")
    else:
        return render_template('login.html', showNavbar=False)

@app.route('/signup')
def signupPage():
    return render_template('signup.html', showNavbar=False)