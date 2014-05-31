import os

from flask import Flask
from flask.ext.mongorest.views import ResourceView
from flask.ext.mongorest.resources import Resource
from flask.ext.mongorest import operators as ops
from flask.ext.mongorest import methods

from flask import render_template

app = Flask(__name__)
app.debug = True


db = MongoEngine(app)
api = MongoRest(app)

@app.route('/')
def index():
    return "hello world"
    return render_template('cover.html')

if __name__ == '__main__':
    app.run()

