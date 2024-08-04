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

@app.route('/login', methods=["GET", "POST"])
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

@app.route('/signup', methods=["GET", "POST"])
def signupPage():
    if request.method == "POST":
        username = request.form["newUsername"]
        password = request.form["newPassword"]
    else:
        return render_template('signup.html', showNavbar=False)