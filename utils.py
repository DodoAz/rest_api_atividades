from models import Pessoas, Usuarios


# Insere Dados na tabela pessoas
def insere_pessoas():
    pessoa = Pessoas(nome='Diogo', idade=25)
    print(pessoa)
    pessoa.save()


# Consulta Dados na tabela pessoas
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    pessoa = Pessoas.query.filter_by(nome='Diogo').first()
    print(pessoas, pessoa.idade)


# Altera Dados na tabela pessoas
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Douglas').first()
    pessoa.nome = 'Azevedo'
    pessoa.save()


# Exclui Dados na tabela pessoas
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Douglas').first()
    pessoa.delete()

# Insere Usuarios na tabela usuarios
def insere_usuario(login, senha):
    usuario = Usuarios(login=login, senha=senha)
    usuario.save()

# Consulta todos os Usuarios na tabela usuarios
def consulta_todos_usuarios():
    usuarios = Usuarios.query.all()
    print(usuarios)

if __name__ == '__main__':
    #insere_usuario('douglas', "1234")
    #insere_usuario('diogo', '4321')
    #consulta_todos_usuarios()
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    #consulta_pessoas()
    pass
