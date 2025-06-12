
from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []

    #criando um construtor/ self -> referencia da instancia == this
    def __init__(self, nome, categoria):
        #o ".title()" faz com que a primeira letra vinda do atributo seja maiuscula
        self._nome = nome.title()
        # ".upper()" deixa todas as letras maiusculas
        self.categoria = categoria.upper()
        #com o "_" deixa o nosso atributo privado
        self._ativo = False
        self._avaliacao = []
        self._cardapio = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
         return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome} | {restaurante.categoria} | {restaurante.media_avaliacoes} | {restaurante.ativo} | ')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'        
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return ' '
        soma_das_notas = sum (avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media
    
    #def adicionar_bebida_no_cardapio(self, bebida):
     #   self._cardapio.append(bebida)

    #def adicionar_prato_no_cardapio(self, prato):
     #   self._cardapio.append(prato)

    def adicionar_no_cardapio(self, item):
        if isinstance(item, ItemCardapio): #esse "isinstance mostra se tem criado algum item para add no cardapio"
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        print(f'Cardápio do restaurante {self._nome}\n')
        for i, item in enumerate(self._cardapio, start=1):
            if hasattr(item, 'descricao'):
                mensagem = f'{i}. Nome: {item._nome} | Preço: ${item._preco} | Descrição: {item.descricao}'
            else:
                mensagem = f'{i}. Nome: {item._nome} | Preço: ${item._preco} | Tamanho: {item.tamanho}'
            print(mensagem)


#restaurante_praca = Restaurante('Praça', 'Gourmet')
#restaurante_praca.alternar_estado()
#restaurante_pizza = Restaurante('Pizza Express', 'Italiano')

##restaurantes = [restaurante_praca, restaurante_pizza]
#print(restaurante_praca)
#Restaurante.listar_restaurantes()