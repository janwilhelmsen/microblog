import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY_FLASK') or 'you_will_never_guess'
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL') or \
    'sqlite:///' + os.path.join(basedir,'app.db')
