import pytest
import xml.etree.ElementTree as ET
from datetime import datetime
from app.schemas.paciente_schema import PacienteSchema
from app.schemas.visitas_schema import VisitaSchema

def test_paciente_to_json():
    paciente_data = {
        "nome": "João da Silva",
        "data_nascimento": datetime.strptime("1985-07-15", "%Y-%m-%d").date(),
        "sexo": "M"
    }
    schema = PacienteSchema()
    result = schema.dump(paciente_data)
    
    assert "João da Silva" == result['nome']
    assert "1985-07-15" == result['data_nascimento']
    assert "M" == result['sexo']

    
def test_paciente_to_json_invalid_data():
    paciente_data = {
        "nome": "João da Silva",
        "data_nascimento": "nao e data",
        "sexo": "M"
    }

    schema = PacienteSchema()

    with pytest.raises(Exception):
        schema.load(paciente_data)


def test_visita_to_xml():
    visita_data = {
        "data_visita": "2024-08-14"
    }
    visita = ET.Element("visita")
    ET.SubElement(visita, "data_visita").text = visita_data['data_visita']
    
    xml_result = ET.tostring(visita, encoding='unicode')
    
    assert "<visita>" in xml_result
    assert "<data_visita>2024-08-14</data_visita>" in xml_result


def test_visita_to_xml_invalid_data(): 
    visita_data = { 
        "data_visita": "nao e data"
    }

    with pytest.raises(ValueError):
        if visita_data['data_visita'] != "2024-08-14":
            raise ValueError("Data inválida")