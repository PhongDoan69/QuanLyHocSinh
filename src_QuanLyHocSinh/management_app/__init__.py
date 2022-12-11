from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
from flask_babelex import Babel
import cloudinary


app = Flask(__name__)
app.secret_key = '$#&*&%$(*&^(*^*&%^%$#^%&^%*&56547648764%$#^%$&^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/dataqlhs?charset=utf8mb4' % quote('Matkhau81@')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db =SQLAlchemy(app=app)