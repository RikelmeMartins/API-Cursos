from api import db
from datetime import date
from sqlalchemy import Integer, String, Date
from sqlalchemy.orm import Mapped, mapped_column

class Formacao(db.Model):
    __tablename__ = 'formacao'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    nome:Mapped[str] = mapped_column(String(100), nullable=False)
    descricao:Mapped[str] = mapped_column(String(250), nullable=False)