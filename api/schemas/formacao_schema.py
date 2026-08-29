from api import ma
from ..models import formacao_model
from marshmallow import fields
from ..schemas import curso_schema, professor_schema

class FormacaoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = formacao_model.Formacao
        _load_instance = True
        _declared_fields = ("id", "nome", "descricao", "cursos", "professores")

    nome = fields.String(required=True)
    descricao = fields.String(required=True)
    cursos = fields.List(fields.Nested(curso_schema.CursoSchema, only=('id', 'nome')))
    professores_ids = fields.List(fields.Integer(), load_only=True)
    professores = fields.List(
        fields.Nested(
            professor_schema.ProfessorSchema,
            only=('id', 'nome'),
            dump_only=True
        )
    )