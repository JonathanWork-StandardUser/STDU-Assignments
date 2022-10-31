from flask_login import current_user, login_user, logout_user, login_required
from randNum import randFunc
from toDict import fileToDict
from random import randint
import matplotlib.pyplot as plt
import numpy as np

from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm
from app.models import User
from werkzeug.urls import url_parse

@app.route('/')
def randDice():
    myDict = fileToDict("words.txt")
    randWords = []
    randNum = []
    for x in range(5):
        randList = randFunc(5)
        print(int(randList), type(int(randList)))
        randWords.append(myDict[randList])
        randNum.append(randList)

    return render_template('randDice.html', randWords = randWords, numbers = randNum, title = 'Random Dice')
#
#@app.route("/swap", methods = ["GET", "POST"])
#def swapCase():
#    if request.method == "POST":
#        first
#
@app.route("/swapCase")
@login_required
def swapCase():
    myString = input("Enter string here por favor: ")
    outString = ""
    for x in myString:
        #print(x)
        if(x.isupper()):
            #print("B4 Capital Letter: " + x)
            outString += x.lower()
            #print("After lower Letter: " + x)
        else:
            #print("B4 Lowercase Letter: " + x)
            outString += x.upper()
            #print("After Capital Letter" + x)
        
    return(outString)

@app.route("/plotDice")
@login_required
def plotDice():
    myList = []
    for x in range(100):
        #print(x)
        myList.append(randint(1, 6))

    print(myList, len(myList))
    plt.plot(myList)
    plt.xlabel('Iterations')
    plt.ylabel('Dice Rolls')
    return render_template('plotDice.html', imageName = 'plot.png', title = 'Plot Dice')

#get request are used to retrieve data
#post are used to submit data to a route
@app.route("/login", methods=('GET', 'POST'))
def login():
    if current_user.is_authenticated:
        return redirect(url_for('randDice'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('randDice'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('randDice')
        return redirect(url_for('randDice'))
    return render_template('login.html', title = 'Sign in', form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('randDice'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('randDice'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are registered!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

if __name__ == '__main__':
    app.run(debug = True, host='0.0.0.0', port=9001)