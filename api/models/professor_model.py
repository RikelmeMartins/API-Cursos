from api import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class Professor(db.Model):
    __tablename__ = 'professor'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    nome:Mapped[str] = mapped_column(String(100), nullable=False)
    idade:Mapped[int] = mapped_column(Integer, nullable=False)