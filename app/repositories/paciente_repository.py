from .. models.paciente import Paciente
from .. import db

class PacienteRepository:
    @staticmethod
    def add_paciente(paciente):
        db.session.add(paciente)
        db.session.commit()

    @staticmethod
    def get_paciente_by_id(paciente_id):
        return Paciente.query.get(paciente_id)
    
    @staticmethod
    def get_all_pacientes():
        return Paciente.query.all()