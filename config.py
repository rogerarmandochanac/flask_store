class Config:
    SECRET_KEY = "SDDẞÆÐÐẞĐDSF@S€¶~{@|@}"


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOTS = 'localhost'
    MYSQL_USER = 'admin'
    MYSQL_PASSWORD = 'admin'
    MYSQL_DB = 'tienda'


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}
