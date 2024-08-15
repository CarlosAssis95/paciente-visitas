import requests
import xml.etree.ElementTree as ET

class ClientePacientes:
    def __init__(self, base_url):
        self.base_url = base_url

    def adicionar_paciente_json(self, nome, data_nascimento, sexo):
        
        data = {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "sexo": sexo
        }
        response = requests.post(f"{self.base_url}/paciente", json=data)
        return response.json()  

    def adicionar_paciente_xml(self, nome, data_nascimento, sexo):
        
        paciente = ET.Element("paciente")
        ET.SubElement(paciente, "nome").text = nome
        ET.SubElement(paciente, "data_nascimento").text = data_nascimento
        ET.SubElement(paciente, "sexo").text = sexo

        xml_data = ET.tostring(paciente, encoding='utf-8', method='xml')
        headers = {'Content-Type': 'application/xml'}
        response = requests.post(f"{self.base_url}/paciente", data=xml_data, headers=headers)
        return response.json()  

    def adicionar_visita_json(self, paciente_id, data_visita):
        data = {
            "data_visita": data_visita
        }
        response = requests.post(f"{self.base_url}/paciente/{paciente_id}/visitas", json=data)
        return response.json() 

    def adicionar_visita_xml(self, paciente_id, data_visita):
        visita = ET.Element("visita")
        ET.SubElement(visita, "data_visita").text = data_visita

        xml_data = ET.tostring(visita, encoding='utf-8', method='xml')
        headers = {'Content-Type': 'application/xml'}
        response = requests.post(f"{self.base_url}/paciente/{paciente_id}/visitas", data=xml_data, headers=headers)
        return response.json() 

    def obter_paciente(self, paciente_id):
        response = requests.get(f"{self.base_url}/paciente/{paciente_id}")
        return response.json()  

    def obter_visitas(self, paciente_id):
        response = requests.get(f"{self.base_url}/paciente/{paciente_id}/visitas")
        return response.json() 


if __name__ == "__main__":
    
    cliente = ClientePacientes("http://127.0.0.1:5000")

    resultado_paciente = cliente.adicionar_paciente_json(
        nome="João da Silva",
        data_nascimento="1985-07-15",
        sexo="M"
    )
    print("Resultado da adição do paciente (JSON):", resultado_paciente)

    if 'id' in resultado_paciente:
        paciente_id = resultado_paciente['id']
        resultado_visita = cliente.adicionar_visita_json(paciente_id, "2024-08-14")
        print("Resultado da adição da visita (JSON):", resultado_visita)

    if 'id' in resultado_paciente:
        paciente_id = resultado_paciente['id']
        paciente = cliente.obter_paciente(paciente_id)
        print("Detalhes do paciente:", paciente)

    if 'id' in resultado_paciente:
        visitas = cliente.obter_visitas(paciente_id)
        print("Visitas do paciente:", visitas)
