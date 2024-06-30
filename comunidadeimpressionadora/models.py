from comunidadeimpressionadora import db
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime


class Usuario(db.Model):
    # id = db.column(db.Integer, primary_key=True)
    # username = db.column(db.DateTime, nullable=False)
    # email = db.column(db.String, nullable=False, unique=True)
    # senha = db.column(db.String, nullable=False)
    # foto_perfil = db.column(db.String, default='default.jpg')
    # posts = db.relationship('Post', backref='autor', lazy=True)
    # cursos = db.column(db.String, nullable=False, default='Não Informado')

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(nullable=False)
    fotos_perfil: Mapped[str] = mapped_column(default='default.jpg')
    posts: Mapped["Post"] = relationship(backref="autor", lazy=True)
    cursos: Mapped[str] = mapped_column(nullable=False, default='Não Informado')


class Post(db.Model):
    # id = db.column(db.Integer, primary_key=True)
    # titulo = db.column(db.String, nullable=False)
    # corpo = db.column(db.Text, nullable=False)
    # data_criacao = db.column(db.DateTime, nullable=False, default=datetime.utcnow)
    # id_usuario = db.column(db.Integer, db.ForeingKey('usuario.id'), nullable=False)

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(nullable=False)
    corpo: Mapped[str] = mapped_column(nullable=False)
    data_criacao: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)
    id_usuario: Mapped[int] = mapped_column(ForeignKey('usuario.id'), nullable=False)    

