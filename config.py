# import os

# class Config:
#     SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql+pymysql://user:password@localhost/employee_management'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     UPLOAD_FOLDER = os.path.join('app', 'static', 'uploads')



from flask import Flask

app = Flask(__name__)
@app.get('/hello')
def get_hello():
    return 'Hello, World!'
app.run("0.0.0.0",5000)