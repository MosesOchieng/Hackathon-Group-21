# form collection from python
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import stringField, PasswordField, submitField
class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email_address = StringFiled(label='email')
    password1 = PasswordField(label='password1')
    password2 = PasswordField(label='password2')
    submit = SubmitField(label='submit ')
# ...

@app.route('/create/', methods=('GET', 'POST'))
def create():
    return render_template('signin.html')

