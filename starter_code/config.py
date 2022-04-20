import os
##SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# TODO IMPLEMENT DATABASE URL
# FORMAT - dialect://username:password@hostaddress:portnumber/dbname

class config(object):
    SQLALCHEMY_DATABASE_URI = 'postgresql://Struan:jasper94@localhost:5432/fyyur_app'
    DEBUG = False

class productionConfig(config):
    pass

class developmentConfig(config):
    DEBUG = True
