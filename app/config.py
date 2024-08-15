import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:password@localhost/paciente')
    SQLALCHEMY_TRACK_MODIFICATIONS = False