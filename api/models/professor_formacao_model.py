from api import db
from sqlalchemy import ForeignKey, Column, Integer
from sqlalchemy.orm import Mapped, mapped_column

professor_formacao = db.Table(
    "professor_formacao",
    Column(
        "professor_id",
        Integer,
        ForeignKey("professor.id"),
        primary_key=True,
        nullable=False
    ),
    Column(
            "formcao_id",
            Integer,
            ForeignKey("formacao.id"),
            primary_key=True,
            nullable=False
    )
)