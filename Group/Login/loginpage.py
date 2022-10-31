from flask import Flask, render_template, url_for
# sqlalchemy (Object Relational Mapper (ORM)) allows apps to manage database
# using high-level entities such as classes, objects, and methods instead
# of tables and SQL. Translates operations to database commands.
from flask_sqlalchemy import SQLAlchemy
# ensure you install flask_login with 'sudo pip install flask_login'
from flask_login import UserMixin
# migrates any changes made to the data
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt

# The URI config should be initialized after flask
app = Flask(__name__)
# connects app file to the html files
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
# creates database instance
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
# connects app file to the html files
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db' 
# this will create a key to secure the session cookie
app.config['SECRET_KEY'] = 'thisisasecretkey'

# create a table for database.db
class User(db.Model, UserMixin):
    # The ID column in the database
    id = db.Column(db.Integer, primary_key=True) 
    # The username column in the database with max 20 characters, nullable disables empty input
    # unique=True restricts 2 or more of the same username
    username = db.Column(db.String(20), nullable=False, unique=True)
    # The password column in the database with max 100 characters, nullable disables empty input
    password = db.Column(db.String(100), nullable=False)

# The argument 'FlaskForm' will be inherited 
class RegisterForm(FlaskForm): 
    """ 
    StringField allows user to read characters 
    InputRequired is used to ensure there is input
    Length is set to 4 characters minimum and max of 20
    Same applies to password field which will turn the password into
    many black dots.
    Notice that the password is set to 20 max. It will be set to 100
    when it gets hashed.
    """
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Register")

    # This will validate whether the username is taken or not
    def validate_username(self, username):
        # Here, it will query the database table and checks
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        # if existing username is found, it raises a flag error
        if existing_user_username:
            raise ValidationError(
                "That username is already taken. Please choose a different username.")

class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired(), Length(
        min=4, max=20)], render_kw={"placeholder": "Password"})
    submit = SubmitField("Login")

@app.route('/')
def home():
    # home page
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # directs to login page
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    # Anytime a user submits the form, it will create a hashed version to be encrypted
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        # Here, it adds the user to the database
        db.session.add(new_user)
        db.session.commit()
    # directs to user registration
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
# type 127.0.0.1:5000 and use either /login or /register to test