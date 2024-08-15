from app import db
from datetime import datetime

class Visitas(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    data_visita = db.Column(db.Date, nullable=False)
    paciente_id = db.Column(db.Integer, db.ForeignKey('pacientes.id'), nullable=False)


