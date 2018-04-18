from flask import Flask, session, render_template, request, json, flash, redirect, url_for
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__,static_url_path="", static_folder="templates")
app.secret_key = 'random string'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hello'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
#transaction lock; mutex lock; overwrite the data; create a transaction log in a separate text file; constant querying management;
@app.route("/")
def main():
    return render_template('LoginPage1.html')
   

@app.route("/showSignUp_student")
def showSignUp_student():
    return render_template('Login_Student.html')

@app.route("/showSignUp_supervisor")
def showSignUp_supervisor():
    return render_template('Login_Supervisor.html')

@app.route("/dashboard_student")
def dashboard_student(username):
    if not session.get(username):
        return render_template('Login_Student.html')
    else:
        return render_template('DashBoard.html')

@app.route("/dashboard_supervisor")
def dashboard_supervisor(username):
    if not session.get(username):
        return render_template('Login_Supervisor.html')
    else:
        return render_template('DashBoardSupervisor.html')

@app.route("/AuthenticateStudent")
def AuthenticateStudent():
    username = request.args.get('uname')
    password = request.args.get('psw')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where netID='" + username + "' and userPassword='" + password + "' and userDesignation='Student'")
    data = cursor.fetchone()
    if data is None:
        flash("Username or Password is wrong")
        return redirect(url_for('showSignUp_student'))
    else:
        session[username] = True;
        return dashboard_student(username)

@app.route("/AuthenticateSupervisor")
def AuthenticateSupervisor():
    username = request.args.get('uname')
    password = request.args.get('psw')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where netID='" + username + "' and userPassword='" + password + "' and userDesignation='Supervisor'")
    data = cursor.fetchone()
    if data is None:
        flash("Username or Password is wrong")
        return redirect(url_for('showSignUp_supervisor'))
    else:
        return "Logged in successfully"

if __name__ == "__main__":
    app.run()
