from api import db
from datetime import date
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .professor_formacao_model import professor_formacao
class Formacao(db.Model):
    __tablename__ = 'formacao'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    nome:Mapped[str] = mapped_column(String(100), nullable=False)
    descricao:Mapped[str] = mapped_column(String(250), nullable=False)
    professores = relationship(
        "Professor",
        secondary=professor_formacao,
        back_populates="formacoes"
    )