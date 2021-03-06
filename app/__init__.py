# coding:utf8
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
import uuid
import os
import pymysql
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Z1y5L9Qll@127.0.0.1:3306/movie'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = uuid.uuid4().hex
app.config['REDIS_URL'] = 'redis://10.31.161.44:6379/0'
app.config['UP_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'static/uploads/')
app.config["FC_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")
app.debug = True
db = SQLAlchemy(app)
rd = FlaskRedis(app)

from app.admin import admin as admin_blueprint
from app.home import home as home_blueprint
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('home/404.html'), 404
