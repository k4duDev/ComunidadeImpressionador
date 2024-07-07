from comunidadeimpressionadora import db, login_manager
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def Load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(db.Model, UserMixin):
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(nullable=False)
    foto_perfil: Mapped[str] = mapped_column(nullable=False, default='default.jpg')
    posts: Mapped["Post"] = relationship(backref="autor", lazy=True)
    cursos: Mapped[str] = mapped_column(nullable=False, default='Não Informado')


class Post(db.Model):
    
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    corpo: Mapped[str] = mapped_column(nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)
    id_usuario: Mapped[int] = mapped_column(ForeignKey('usuario.id'), nullable=False)    

