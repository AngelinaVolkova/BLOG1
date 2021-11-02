from flask_wtf import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required


class LoginForm(Form):
    username = TextField('username', validators=[Required()])
    pwd = TextField('pwd', validators=[Required])
