class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:root@localhost:5432/blog_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'my-secret-key'