class Configuration(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user='flask_user',pw='123',url='localhost:5432',db='flask_db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
