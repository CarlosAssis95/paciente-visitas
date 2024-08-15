from marshmallow import Schema, fields

class PacienteSchema(Schema):
    nome = fields.Str(required=True)
    data_nascimento = fields.Date(required=True)
    sexo = fields.Str(required=True, validate=lambda s: s in ['M', 'F'])