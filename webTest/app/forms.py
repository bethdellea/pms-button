from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField, validators


class LoginForm(Form):
    email_l = StringField("Email", validators=[validators.required()])
    password_l = PasswordField("Password", validators=[validators.required()])
    submit_l = SubmitField("Submit")


class SignUpForm(Form):
    username_s = StringField("Username", validators=[validators.required(), validators.length(min=4, max=32),
                                                     validators.regexp("[0-9A-Za-z_]+")],
                             description="Letters, numbers, and underscores only, please!")
    password_s = PasswordField("Password", validators=[validators.required(), validators.length(min=6, max=48),
                                                       validators.EqualTo('confirm_s', message="Passwords don't match")],
                               description="At least 6 characters. Maybe don't use the same password here as you use "
                                           "for, say, your online banking.")
    confirm_s = PasswordField("Confirm password", validators=[validators.required()])
    email_s = StringField("Email address", validators=[validators.required(), validators.Email()],
                          description="We might use this to contact you about important account info, but probably not.")
    submit_s = SubmitField("Submit")
