from models import Autor, Livro


def popular_banco(session):
    """Cadastre autores e livros iniciais para testar a aplicação."""
    autor1 = Autor(nome="Autor1", pais="País 1")
    autor2 = Autor(nome="Autor2", pais="País 2")         # TODO: crie pelo menos 3 autores.
    autor3 = Autor(nome="Autor3", pais="País 3") 

    session.add_all([autor1, autor2, autor3])

    livro1 = Livro(nome="livro1", autor = autor1)
    livro2 = Livro(nome="livro2", autor = autor1)         
    livro3 = Livro(nome="livro3", autor = autor2)
    livro4 = Livro(nome="livro4", autor = autor2)         # TODO: crie pelo menos 6 livros.
    livro5 = Livro(nome="livro5", autor = autor3)         
    livro6 = Livro(nome="livro6", autor = autor3)

    livro3.disponivel = False         # TODO: inclua livros disponíveis e indisponíveis.
    livro5.disponivel = False

    session.add_all([livro1, livro2, livro3,  livro4,  livro5,  livro6])

    session.commit()          # TODO: use session.add ou session.add_all e finalize com session.commit().

    pass
