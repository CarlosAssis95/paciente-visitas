from marshmallow import Schema, fields

class VisitaSchema(Schema):
    data_visita = fields.Date(required=True)