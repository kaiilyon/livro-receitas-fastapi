from database import get_session
from models import Categoria

novas_categorias = ["Bebidas", "Massas", "Carnes", "Saladas"]

session = next(get_session())

for nome in novas_categorias:
    existe = session.query(Categoria).filter_by(nome=nome).first()

    if not existe:
        session.add(Categoria(nome=nome))

session.commit()

print("Categorias criadas!")