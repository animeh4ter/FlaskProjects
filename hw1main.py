from flask import Flask, url_for, render_template, g
from DBManipulator import DBM
import sqlite3
import os


DEBUG = True
DATABASE = '/tmp/site_db.db'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(DATABASE=os.path.join(app.root_path, 'site_db.db'))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql', 'r') as file:
        db.cursor().executescript(file.read())
    db.commit()
    db.close()


def get_db():
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


def dbm_thrower():
    db = get_db()
    dbase = DBM(db)
    return dbase


@app.route('/')
@app.route('/main')
def main_page():
    return render_template("mainpage.html", title='Main', site_menu=dbm_thrower().get_menu())


@app.route('/about')
def about_page():
    return render_template("aboutHW.html", title='About', site_menu=dbm_thrower().get_menu())


@app.route('/loremipsum')
def lorem_ipsum():
    return render_template("loremipsum.html", title='Fish text', site_menu=dbm_thrower().get_menu())


@app.route('/github')
def github_page():
    return render_template("github.html", title="Git")


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link.db'):
        g.link_db.close()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Not Found", site_menu=dbm_thrower().get_menu())


if __name__ == '__main__':
    app.run(debug=DEBUG)
