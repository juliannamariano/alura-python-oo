# Importando o outro arquivo para poder utilizar as informações que estão dentro dele
from modelos.restaurante import Restaurante 

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', "Japonesa")

def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
 