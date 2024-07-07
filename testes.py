from comunidadeimpressionadora import app, db
from comunidadeimpressionadora.models import Usuario, Post


with app.app_context():
    db.drop_all()
    db.create_all()


# with app.app_context():
#     usuario = Usuario.query.filter_by(email='k4du.abraao@gmail.com').first()

# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo="Primeiro Post", corpo="Kdu voando" )