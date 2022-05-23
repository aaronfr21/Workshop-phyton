#Connect to Database
##flaskr/db.py
"""
import sqlite3
import click
from flask import current_app, g
from flask.cli import with_appcontext
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db
def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()
"""

#Create the Tables
##flaskr/schema.sql
"""
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS post;
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);
CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  author_id INTEGER NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);
"""

##flaskr/db.py
"""
def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
@click.command('init-db')
@with_appcontext
def init_db_command():
    Clear the existing data and create new tables.
    init_db()
    click.echo('Initialized the database.')
"""

#Register with the Application
##flaskr/db.py
"""
def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
"""

##flaskr/__init__.py
"""
def create_app():
    app = ...
    # existing code omitted
    from . import db
    db.init_app(app)
    return app
"""

#Initialize the Database File
##Run the init-db command:
'''
$ flask init-db
Initialized the database.
'''