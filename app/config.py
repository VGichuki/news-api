class Config:
    '''
    General Configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/'

class ProdConfig(Config):
    '''
    Production Configuration child class
    '''
    pass

class DevConfig(Config):
    '''
    Development Configuration child class
    '''
    DEBUG = True