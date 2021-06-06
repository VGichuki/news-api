class Config:
    '''
    General Configuration parent class
    '''
    NEWS_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'

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