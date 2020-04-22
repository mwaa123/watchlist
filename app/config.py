class Config:
    '''
    General configuration parent class
    '''
    # MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/550?api_key=20f30dc208f1cd4818dd004a1f1d0b51{}?api_key={}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True
