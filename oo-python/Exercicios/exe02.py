class Conta:

    def __init__(self, nome='', saldo =0, ativo= False):
        self.nome = nome
        self.saldo = saldo
        self.ativo = ativo

    def __str__(self):
        return f'Titular da conta: {self.nome} | Saldo da conta: {self.saldo} | Estado: {self.ativo}'
    
    def ativar_conta(self):
        #return 'Não ativo' if self.ativo else 'Ativo'
        self.ativo = True

titular1 = Conta(nome='Amanda', saldo=100)
print(titular1)
Conta.ativar_conta(titular1)
print(titular1)