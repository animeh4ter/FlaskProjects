from flask import Flask, url_for, render_template

app = Flask(__name__)

menu = [{'name': 'Main Page', 'url': 'main'},
        {'name': 'About HW', 'url': 'about'},
        {'name': 'Lorem Ipsum', 'url': 'loremipsum'},
        {'name': 'GitHub', 'url': 'github'}
        ]


@app.route('/')
@app.route('/main')
def main_page():
    return render_template("mainpage.html", title='Main', site_menu=menu)


@app.route('/about')
def about_page():
    return render_template("aboutHW.html", title='About', site_menu=menu)


@app.route('/loremipsum')
def lorem_ipsum():
    return render_template("loremipsum.html", title='Fish text', site_menu=menu)


@app.route('/github')
def github_page():
    return render_template("github.html", title="Git")


if __name__ == '__main__':
    app.run(debug=True)
