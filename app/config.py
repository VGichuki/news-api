class Config:
    '''
    General Configuration parent class
    '''

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