from api import ma
from ..models import professor_model
from marshmallow import fields

class ProfessorSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = professor_model.Professor
        _load_instance = True
        _declared_fields = ("id", "nome", "idade")

    nome = fields.String(required=True)
    idade = fields.Integer(required=True)