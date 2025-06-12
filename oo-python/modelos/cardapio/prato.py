from modelos.cardapio.item_cardapio import ItemCardapio

#Com esse parametro passado dentro dos parenteses indica que tem uma relação de herança entre as classes
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        #Reutilizando o construtor com atributos iguais
        super().__init__(nome, preco)
        self.descricao = descricao

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
       self._preco -= (self._preco * 0.05)