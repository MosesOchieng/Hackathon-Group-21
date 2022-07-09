# Code contains both the project task challange complete file functionality of Door lock system below and a Scaled project of Panda door lock system fully intergrated with flask ,speech recognition system and an update of the visitors to your door which is under development.
# time to complete the fully panda door lock system is short therefore a submission on the directives for the working of the door system is given after the flask import and functionalities.


# door lock panda system code
from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('signin.html')

if  __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
    """
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30),nullable=False, unique=True)
    email = db.Column(db.String(length=30),nullable=False,unique=True)
    password = db.Column(db.String(length=30),nullable=False, unique=True)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('sign.html', password='password')
@app.route('/home')
def home_page():
    return render_template('index,html')

@app.route('/register')
def register_page():
    form = RegisterForm()
    return render_template('signup.html', form=form)
"""


# door lock system challenge system(assignment)
# run this part of the code
import re   # this is a library module that helps in checking for a strong password.
import datetime  # library imports date and time

from datetime import datetime



# accepting password input and checking for the stregth
def main():
    password_input = input("set a password to open and close your door:")
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"

    # compiling regex
    pat = re.compile(reg)

    # searching regex
    mat = re.search(pat, password_input)

    # validating conditions
    if mat:
        print("Password is valid.")
        if mat:
            print("Please now put your set password to login to the system")
            password = input("Enter password to unlock your door system application:")
            if password == password_input:
                print("Password input is matching with set password")
                if password == password_input:
                    answer = ["open", "close", "quit"]# array to contain responses from user
                    question = input("Dear user what would you want to do to the door:")
                    if answer[0] == question:
                        print("Door is on Open mode , kindly wait")
                        if answer[0] == question:
                            now = datetime.now().time()  # time object
                            print("The time and date is", now)
                        if answer[0] == question:
                            question = input("Dear user we have opened your door, what would you want us to do to the door again:")
                            if answer[1] == question:
                                print("Door that was opened is now closing.")
                                if answer[0] == question:
                                    now = datetime.now().time()  # time object
                                    print("The time and date is", now)
                            if answer[0] == question:
                                now = datetime.now().time()  # time object
                                print("Door is already open at", now)
                    if answer[1] == question:
                        print("Door is closing ,kindly be patient")
                        if answer[1] == question:
                            question = input(
                                "Dear user we have closed your door ,what would you want us to do to the door again:")
                            if answer[1] == question:
                                now = datetime.now().time()  # time object
                                print("Door is already Closed", now)
                    if answer[2] == question:
                        print("It is sad to see you leave.")
            elif password != password_input:# wrong  password prompting the user to input the password again
                print("Your password does not match set password")
                password = input("Input your password again:")
                if password_input == password:
                    answer = ["open", "close", "quit"]
                    question = input("Dear user what would you want to do to the door:")
                    if answer[0] == question:
                        print("Door is on Open mode , kindly wait")
                        if answer[0] == question:
                            now = datetime.now().time()# time object
                            print("The time and date is", now)
                        if answer[0] == question:
                            question = input("Dear user we have opened your door, what would you want us to do to the door again:")
                            if answer[1] == question:
                                print("Door that was opened is now closing.", now)
                                if answer[0] == question:
                                    now = datetime.now().time()  # time object
                                    print("The time and date is", now)
                            if answer[0] == question:
                                now = datetime.now().time()  # time object
                                print("Door is already open at", now)
                    if answer[1] == question:
                         print("Door is closing ,kindly be patient")
                         if answer[1] == question:
                             question = input("Dear user we have closed your door ,Click quit to log out")
                             if answer[1] == question:
                                 now = datetime.now().time()  # time object
                                 print("Door is already Closed",now)
                    if answer[2] == question:
                        print("It is sad to see you leave.")
    elif mat != password_input:
        print("Password is not correct please follow the listed instructions to set a strong password ")
        password_input = input("Set password again:") # incase user does not set a password according to the regulation required to input password the user is forced to input password again.

if __name__ == '__main__':
        main()
# connection to a new created database





