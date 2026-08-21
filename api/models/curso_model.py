from api import db
from datetime import date
from sqlalchemy import Integer, String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..models import formacao_model

class Curso(db.Model):
    __tablename__ = 'curso'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    nome:Mapped[str] = mapped_column(String(100), nullable=False)
    descricao:Mapped[str] = mapped_column(String(250), nullable=False)
    data_publicacao:Mapped[date] = mapped_column(Date, nullable=False)

    formacao_id:Mapped[int] = mapped_column(ForeignKey("formacao.id"))
    formacao = relationship(formacao_model.Formacao, backref="cursos")
    