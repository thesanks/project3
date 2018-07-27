import os
class Configuration(object):
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    STATIC_DIR      = os.path.join(APPLICATION_DIR, 'static')
    IMAGES_DIR      = os.path.join(STATIC_DIR, 'images')

    DEBUG = True
    SECRET_KEY = 'welcome to the jungle'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/blog.db' % APPLICATION_DIR
