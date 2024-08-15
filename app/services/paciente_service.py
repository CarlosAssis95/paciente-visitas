from ..models.paciente import Paciente
from ..repositories.paciente_repository import PacienteRepository
from datetime import datetime

class PacienteService:
    @staticmethod
    def create_paciente(data):
        paciente = Paciente(
            nome=data['nome'],
            data_nascimento=datetime.strptime(data['data_nascimento'], '%Y-%m-%d').date(),
            sexo=data['sexo']
        )
        PacienteRepository.add_paciente(paciente)
        return paciente
    

    @staticmethod
    def get_paciente_by_id(paciente_id):
        return PacienteRepository.get_paciente_by_id(paciente_id)