from flask import render_template, request, redirect, url_for, session, flash, send_from_directory
from allpy import app
from allpy.sudoku import Sudoku
from allpy.forms import NextSolForm, RegisterForm, LoginForm
from allpy.models import User
from allpy import db
from wtforms import IntegerField
from flask_login import login_user, logout_user, login_required

@app.route('/')
@app.route('/home')
def home_page():
	return render_template('home.html')

@app.route('/sudoku', methods = ['GET', 'POST'])
@login_required
def sudoku_game():
	if request.method == 'GET':
		return render_template('sudoku.html')
	if request.method == 'POST':
		fata = request.form
		data = {}
		for i in fata :
			data[int(i)] = fata[i]
		s = Sudoku(data)
		s.solve(0, 0)
		session["sudoku"] = s.solutions
		session["sol_no"] = 0
		return redirect(url_for('sudoku_solved'))

@app.route('/solved', methods = ['GET', 'POST'])
def sudoku_solved():
	nxtsol = NextSolForm()
	s = session["sudoku"]
	sol_no = session["sol_no"]
	if request.method == 'GET':
		return render_template('solved.html', form= nxtsol, data = s, sol_no=sol_no )

	if request.method == 'POST':
		session["sol_no"] = session["sol_no"]+1
		sol_no = session["sol_no"]
		if (sol_no >= len(s)):
			sol_no = 0
			session["sol_no"] = 0
		return render_template('solved.html', form= nxtsol, data = s, sol_no=sol_no )

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('login_page'))
    if form.errors != {}: #If there are no errors from the validations
        for err_msg in form.errors.values():
            flash(f'error : {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('sudoku_game'))
        else:
            flash('Username and password are not matched! Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))