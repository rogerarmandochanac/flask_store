class Config:
    SECRET_KEY = "SDDẞÆÐÐẞĐDSF@S€¶~{@|@}"


class DevelopmentConfig(Config):
    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig,
}
