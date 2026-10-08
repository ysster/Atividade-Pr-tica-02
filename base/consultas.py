from sqlalchemy import select

from models import Autor, Livro


def listar_livros(session):
    """Liste todos os livros com o nome do autor e o status de disponibilidade."""
    resultado = session.execute(select(Livro)). all()
    return resultado                                             # TODO: use select(Livro) e acesse livro.autor.nome.

def listar_livros_disponiveis(session):
    """Liste apenas os livros disponíveis."""
    resultado = session.execute(
        select(Livro).Where(Livro.disponivel == True)
    ).all  
    return resultado                                                             # TODO: filtre Livro.disponivel igual a True.


def buscar_livros_por_titulo(session, trecho):
    """Busque livros por parte do título."""
    resultado = session.execute(
        select(Livro).where(Livro.titulo(f"%{trecho}%"))
    ).all
    return resultado
    
def listar_livros_por_autor(session, nome_autor):
    """Liste os livros de um autor informado pelo nome."""
    pass

