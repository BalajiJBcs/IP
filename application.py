from flask import Flask, session, render_template, request, json, flash, redirect, url_for, make_response
from flaskext.mysql import MySQL
from datetime import date, time, datetime 

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
    if not session.get('logged_in'):
        return render_template('Login_Student.html')
    else:
        cursor = mysql.connect().cursor()
        cursor.execute("select diningName from DiningHalls where diningName in ( select userWorkPlace from User where netID = '"+username+"')")
        dining_hall = cursor.fetchall();
        cursor.execute("select userName from User where netID = '"+username+"'")
        name = cursor.fetchall();
        for row in dining_hall:
            diningHall = row[0];
        for row in name:
            user_name = row[0]; 
        print(diningHall)
        print(user_name)
        return render_template('DashBoard.html',variable=user_name,variable1=diningHall)

@app.route("/dashboard_supervisor")
def dashboard_supervisor(username):
    if not session.get('logged_in'):
        return render_template('Login_Supervisor.html')
    else:
        cursor = mysql.connect().cursor()
        cursor.execute("select diningName from DiningHalls where diningName in ( select userWorkPlace from User where netID = '"+username+"')")
        dining_hall = cursor.fetchall();
        cursor.execute("select userName from User where netID = '"+username+"'")
        name = cursor.fetchall();
        for row in dining_hall:
            diningHall = row[0];
        for row in name:
            user_name = row[0]; 
        print(diningHall)
        print(user_name)
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
        session['logged_in'] = True;
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
        session['logged_in'] = True;
        return dashboard_student(username)


@app.route("/MySchedule")   
def mySchedule():
    cursor = mysql.connect().cursor()
    username = "apmahaja"
    cursor.execute("select A_date,WorkingFrom,workingto from permanentsubschedule_b where netid='"+username+"' and openShift='N';")
    myschedule = cursor.fetchall(); 
    json_data = []

    for result in myschedule:
        date = result[0].isoformat()
        workingFrom_hours, workingFrom_mins = result[1].seconds//3600, (result[1].seconds//60)%60
        workingTo_hours, workingTo_mins = result[2].seconds//3600, (result[2].seconds//60)%60

        data = {
                'title': username,
                'start': str(date) + " " + str(workingFrom_hours) +":"+ str(workingFrom_mins),
                'end': str(date) + " " + str(workingTo_hours) +":"+ str(workingTo_mins),
                'color': "#D44500",
            }
        json_data.append(data)

    js= json.dumps(json_data)
    response = make_response(js)
    response.headers['Content-Type']='application/json'
    return response


@app.route("/AvailableShifts")   
def availableShifts():
    cursor = mysql.connect().cursor()
    username = "apmahaja"
    cursor.execute("select A_date,WorkingFrom,workingto from permanentsubschedule_b where openShift='Y';")
    myschedule = cursor.fetchall(); 
    json_data = []

    for result in myschedule:
        date = result[0].isoformat()
        workingFrom_hours, workingFrom_mins = result[1].seconds//3600, (result[1].seconds//60)%60
        workingTo_hours, workingTo_mins = result[2].seconds//3600, (result[2].seconds//60)%60

        data = {
                'title': "Available Shift",
                'start': str(date) + " " + str(workingFrom_hours) +":"+ str(workingFrom_mins),
                'end': str(date) + " " + str(workingTo_hours) +":"+ str(workingTo_mins),
                'color': "#009900",
            }
        json_data.append(data)

    js= json.dumps(json_data)
    response = make_response(js)
    response.headers['Content-Type']='application/json'
    return response

@app.route("/logout")
def logout():
    session.pop('logged_in',None)
    #flash('You have logged out!')
    return redirect(url_for('main'))
    
if __name__ == "__main__":
    app.run()
