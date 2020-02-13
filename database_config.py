class DatabaseConfig(object):
    # <DB TYPE>+<DB interface?>://<username>:<password>@<location>/<database>
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/login'
    SQLALCHEMY_TRACK_MODIFICATIONS = False