class Restaurante:
    #criando um construtor/ self -> referencia da instancia == this
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
         return f'{self.nome} | {self.categoria}'
    
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiano')

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurante_praca)
