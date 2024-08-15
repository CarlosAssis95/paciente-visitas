from .. models.visitas import Visitas
from .. import db

class VisitasRepository:
    @staticmethod
    def add_visita(visita):
        db.session.add(visita)
        db.session.commit()

    @staticmethod
    def get_visitas_by_paciente_id(paciente_id):
        return Visitas.query.filter_by(paciente_id = paciente_id).all()
    
    @staticmethod
    def get_all_visitas():
        return Visitas.query.all()