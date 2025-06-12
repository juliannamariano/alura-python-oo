# Importando o outro arquivo para poder utilizar as informações que estão dentro dele
from modelos.restaurante import Restaurante 
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'grande')
prato_paozinho = Prato('Paozinho', 2.00,'O melhor pão da cidade')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_paozinho)


#restaurante_praca.receber_avaliacao('Gui', 10)
##restaurante_praca.receber_avaliacao('Emy', 5)
#restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
#restaurante_japones = Restaurante('Japa', "Japonesa")

def main():
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
 