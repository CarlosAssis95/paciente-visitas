from flask import Blueprint, request, jsonify
from ..services.paciente_service import PacienteService
from ..schemas.paciente_schema import PacienteSchema
import xmltodict

paciente_bp = Blueprint('paciente', __name__)
paciente_schema = PacienteSchema()

@paciente_bp.route('/paciente', methods=['POST'])
def adicionar_paciente():
    
    if request.content_type == 'application/json':
        data = request.get_json()
    elif request.content_type == 'application/xml':
        data = xmltodict.parse(request.data)
        data = data.get('paciente', {})
    else:
        return jsonify({'error': 'Unsupported Media Type'}), 415

    
    errors = paciente_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    try:
        paciente = PacienteService.create_paciente(data)
        return jsonify({'message': 'Paciente adicionado com sucesso!', 'id': paciente.id}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@paciente_bp.route('/paciente/<int:id>', methods=['GET'])
def get_paciente(id):
    paciente = PacienteService.get_paciente_by_id(id)
    if not paciente:
        return jsonify({'error': 'Paciente não encontrado'}), 404
    return jsonify(paciente_schema.dump(paciente)), 200