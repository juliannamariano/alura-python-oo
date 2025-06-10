class Restaurante:
    restaurantes = []

    #criando um construtor/ self -> referencia da instancia == this
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        #com o "_" deixa o nosso atributo privado
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
         return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'        


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiano')

##restaurantes = [restaurante_praca, restaurante_pizza]
#print(restaurante_praca)

Restaurante.listar_restaurantes()