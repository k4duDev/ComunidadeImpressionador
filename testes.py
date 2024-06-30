from comunidadeimpressionadora.routes import app, db
from comunidadeimpressionadora.models import Usuario, Post

if not 'comunidade.db':
    with app.app_context():
        db.create_all()


# with app.app_context():
#     usuario = Usuario.query.filter_by(email='k4du.abraao@gmail.com').first()

# with app.app_context():
#     meu_post = Post(id_usuario=1, titulo="Primeiro Post", corpo="Kdu voando" )