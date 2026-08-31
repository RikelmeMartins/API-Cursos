from api import db
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from passlib.hash import pbkdf2_sha256

class Usuario(db.Model):
    __tablename__ = 'usuario'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    nome:Mapped[str] = mapped_column(String(100), nullable=False)
    email:Mapped[str] = mapped_column(String(100), nullable=False)
    senha:Mapped[str] = mapped_column(String(255), nullable=False)

    def encriptar_senha(self):
        self.senha = pbkdf2_sha256.hash(self.senha)

    def ver_senha(self, senha):
        return pbkdf2_sha256.verify(senha, self.senha)