from ..models.visitas import Visitas
from ..repositories.visitas_repository import VisitasRepository
from datetime import datetime

class VisitasService:
    @staticmethod
    def create_visita(paciente_id, data):
        visita = Visitas(
            data_visita=datetime.strptime(data['data_visita'], '%Y-%m-%d').date(),
            paciente_id=paciente_id
        )
        VisitasRepository.add_visita(visita)
        return visita
    

    @staticmethod
    def get_visitas_by_paciente_id(paciente_id):
        return VisitasRepository.get_visitas_by_paciente_id(paciente_id)