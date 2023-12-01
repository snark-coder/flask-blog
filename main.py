from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')



