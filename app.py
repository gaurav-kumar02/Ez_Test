from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from flask_migrate import Migrate
from models import db, User, File
from resources.user import SignUp, EmailVerify, Login
from resources.file import UploadFile, ListFiles, DownloadFile, AccessFile

from config import Config

app = Flask(__name__)
api = Api(app)

app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///file_sharing.db'
app.config['JWT_SECRET_KEY'] = 'EZ_test'  # Change this!
app.config['UPLOAD_FOLDER'] = 'uploads'
# app.config['MAIL_SERVER'] = 'ez_test.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_email'
app.config['MAIL_PASSWORD'] = 'your_password'

db.init_app(app)
jwt = JWTManager(app)
mail = Mail(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

# Routes
api.add_resource(SignUp, '/signup')
api.add_resource(EmailVerify, '/email-verify')
api.add_resource(Login, '/login')
api.add_resource(UploadFile, '/upload-file')
api.add_resource(ListFiles, '/list-files')
api.add_resource(DownloadFile, '/download-file/<string:filename>')
api.add_resource(AccessFile, '/access-file/<string:secure_url>')

if __name__ == '__main__':
    app.run(debug=True)

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
db.init_app(app)
jwt = JWTManager(app)
mail = Mail(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

api.add_resource(SignUp, '/signup')
api.add_resource(EmailVerify, '/email-verify')
api.add_resource(Login, '/login')
api.add_resource(UploadFile, '/upload-file')
api.add_resource(ListFiles, '/list-files')
api.add_resource(DownloadFile, '/download-file/<string:filename>')
api.add_resource(AccessFile, '/access-file/<string:secure_url>')

if __name__ == '__main__':
    app.run(debug=True)
