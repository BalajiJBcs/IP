from flask import Flask, render_template, request, json
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'hello'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def main():
    return render_template('LoginPage1.html')

@app.route("/showSignUp_student")
def showSignUp_student():
    return render_template('Login_Student.html')

@app.route("/showSignUp_supervisor")
def showSignUp_supervisor():
    return render_template('Login_Supervisor.html')

@app.route("/AuthenticateStudent")
def AuthenticateStudent():
    username = request.args.get('uname')
    password = request.args.get('psw')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where netID='" + username + "' and userPassword='" + password + " and userDesignation='Student'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"

@app.route("/AuthenticateSupervisor")
def AuthenticateSupervisor():
    username = request.args.get('uname')
    password = request.args.get('psw')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where netID='" + username + "' and userPassword='" + password + " and userDesignation='Supervisor'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"

if __name__ == "__main__":
    app.run()
