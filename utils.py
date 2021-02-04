from models import Pessoas


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

if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    #exclui_pessoa()
    consulta_pessoas()
