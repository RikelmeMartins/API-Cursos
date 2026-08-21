from api import ma
from ..models import formacao_model
from marshmallow import fields

class FormacaoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = formacao_model.Formacao
        _load_instance = True
        _declared_fields = ("id", "nome", "descricao")

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    