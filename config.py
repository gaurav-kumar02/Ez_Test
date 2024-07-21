

class Config:
    SECRET_KEY = 'your_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///file_sharing.db'
    JWT_SECRET_KEY = 'your_jwt_secret_key'  # Change this!
    UPLOAD_FOLDER = 'uploads'
    MAIL_SERVER = 'smtp.example.com'  # Change this to your mail server
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'your_email@example.com'  # Change this
    MAIL_PASSWORD = 'your_password'  # Change this
