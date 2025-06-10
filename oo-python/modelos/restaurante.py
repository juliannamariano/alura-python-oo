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
        Restaurante.restaurantes.append(self)

    def __str__(self):
         return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome} | {restaurante.categoria} | {restaurante.ativo}')

    @property
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'false'        
    
    def alternar_estado(self):
        self._ativo = not self._ativo

#restaurante_praca = Restaurante('Praça', 'Gourmet')
#restaurante_praca.alternar_estado()
#restaurante_pizza = Restaurante('Pizza Express', 'Italiano')

##restaurantes = [restaurante_praca, restaurante_pizza]
#print(restaurante_praca)

Restaurante.listar_restaurantes()