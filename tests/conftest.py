
import sys
import os
import pytest


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from app import create_app, db

@pytest.fixture(scope='module')
def test_client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  
    with app.test_client() as client:
        with app.app_context():
            db.create_all()  
        yield client  
        with app.app_context():
            db.drop_all()  
