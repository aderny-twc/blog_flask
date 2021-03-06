class Configuration():
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://sblog:sblogDBpasswd@localhost/sblogdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'Really strong key for my application'
