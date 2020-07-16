import secrets
import os


class ProductionConfig(object):
    """
    Production environment specific configuration
    """
    def __init__(self):
        self.TESTING = False
        self.ENDPOINT_HOST = "https://github.com/0x78f1935"
        # SQLAlchemy settings
        self.SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False
        # Azure Active Directory
        self.AD_AUTH_URL = "https://login.microsoftonline.com/organizations/"
        self.AD_TENANT = ""
        self.JWT_ISSUER = ""
        self.JWT_LIFETIME_SECONDS = 2592000  # Total seconds a token expires after creation 2592000 == 1 month
        # reCaptcha
        self.CAPTCHA_KEY = ""

class DevelopmentConfig(object):
    """
    Development environment specific configuration
    """
    def __init__(self):
        self.TESTING = True
        
        # SQLAlchemy settings
        self.SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://'
        self.SQLALCHEMY_TRACK_MODIFICATIONS = True
        # Azure Active Directory
        self.AD_AUTH_URL = "https://login.microsoftonline.com/organizations/"
        self.AD_TENANT = ""
        self.NOISE = 'test'
        self.TOKEN_NOISE = 'token_dev'
        # reCaptcha
        self.CAPTCHA_KEY = ""

class System(object):
    """
    This class is a configuration class specific for this application.
    If you make changes in this class you are probably breaking the webserver.
    """
    def __init__(self):
        self.MAINTAINER = "https://github.com/0x78f1935"
        self.VERSION = "1.0.0"
        self.SECRET_KEY = "\\xfcU\\xf4@\\xa5\\xfc\\\\\\xb71u"
        self.ENDPOINT_HOST = "http://localhost:5000"
        self.REDIRECT_URI = self.ENDPOINT_HOST + "/auth/authenticated"
        self.LOGOUT_URI = self.ENDPOINT_HOST + "/auth/logout"

        from base64 import b64encode
        from uuid import uuid4
        self.NOISE = secrets.token_hex(64)
        self.TOKEN_NOISE = secrets.token_hex(64)


class BaseConfig(System, ProductionConfig, DevelopmentConfig):
    '''
    Base config environment configuration.
    '''
    def __init__(self):
        # Generic information
        #--------------------
        self.DEBUG = True
        # Configuration
        System.__init__(self)
        # When debug is False, load production environment
        if not self.DEBUG: ProductionConfig.__init__(self)
        # When debug is True, load development environment
        else: DevelopmentConfig.__init__(self)