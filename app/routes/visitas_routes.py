from flask import Blueprint, request, jsonify
from ..services.visitas_service import VisitasService
from ..schemas.visitas_schema import VisitaSchema
import xmltodict

visitas_bp = Blueprint('visitas', __name__)
visita_schema = VisitaSchema()

@visitas_bp.route('/paciente/<int:id>/visitas', methods=['POST'])
def adicionar_visita(id):
    
    if request.content_type == 'application/json':
        data = request.get_json()
    elif request.content_type == 'application/xml':
        data = xmltodict.parse(request.data)
        data = data.get('visita', {})
    else:
        return jsonify({'error': 'Unsupported Media Type'}), 415

   
    errors = visita_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    try:
        visita = VisitasService.create_visita(id, data)
        return jsonify({'message': 'Visita adicionada com sucesso!', 'id': visita.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@visitas_bp.route('/paciente/<int:id>/visitas', methods=['GET'])
def get_visitas(id):
    visitas = VisitasService.get_visitas_by_paciente_id(id)
    return jsonify(visita_schema.dump(visitas, many=True)), 200