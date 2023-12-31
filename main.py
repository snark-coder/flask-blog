from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '743fe7dfa22cfb0f55042e5c30bb8e83'

posts = [
    {
        'name': 'Durga',
        'title': 'Blog Post 1',
        'content': 'blog post content',
        'dateJoined': 'December 2 2023'

    },
    {
        'name': 'Kundan',
        'title': 'Blog Post 2',
        'content': 'blog post content2',
        'dateJoined': 'December 3 2023'

    }

]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash("Logged in!", 'success')
            return redirect(url_for('home'))
        else:
            flash('check your credentials!', 'danger')  
    return render_template('login.html', title='Login', form=form)

