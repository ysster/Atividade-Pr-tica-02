# Atividade Prática 02 - Biblioteca Persistente

Complete os arquivos da base usando SQLAlchemy ORM.

## Como executar

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Defesa escrita

Responda ao final:

1. Para que serve o campo `disponivel` em `Livro`?
   Serve para indicar se o livro esta disponivel
2. Por que é necessário chamar `session.commit()` após emprestar ou devolver?
   Serve para salvar as alterações
3. Em qual consulta você usa o relacionamento entre `Livro` e `Autor`?
   É usado em Autor e Livro ligando eles
