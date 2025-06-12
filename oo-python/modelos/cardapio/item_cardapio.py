#import para classe abstrata
from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    # Montando uma classe abstrata tirando a repetição de código, lembrando que essa classe não pode ser instanciada
    @abstractmethod
    def aplicar_desconto(self):
        pass