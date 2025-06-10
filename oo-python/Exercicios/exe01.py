class Pessoa: 

    def __init__(self, nome ='', idade=0, profissao=''):
        self._nome = nome
        self._idade = idade
        self._profissao = profissao

    def __str__(self):
        return f'Nome: {self._nome} -- Idade: {self._idade} -- Profissão: {self._profissao}'

    def aniversario(self):
        self._idade +=1   

    @property
    def saudacao(self):
        if self._profissao:
            return f'Olá, sou {self._nome}! Trabalho como {self._profissao}.'
        else:
            return f'Olá, sou {self._nome}!'
        

pessoa1 = Pessoa(nome='A', idade =2, profissao='Atriz')
print(pessoa1)
pessoa1.aniversario()

print("Informações após aniversário:")
print(pessoa1)
print(pessoa1.saudacao)