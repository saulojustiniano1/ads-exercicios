class Instrumento:  # Classe pai
    def __init__(self, cor, tamanho):  # Método construtor
        self.cor = cor
        self.tamanho = tamanho

    def tocar(self):  # Método
        print('Tocando o instrumento genérico')
        print(f'Tocando o instrumento {self.cor} de tamanho {self.tamanho}')


class Violino(Instrumento):  # Herança
    def __init__(self, cor, tamanho, tipo):  # Método construtor
        super().__init__(cor, tamanho)
        self.tipo = tipo

    def tocar(self):  # Polimorfismo
        print('Produzindo som de violino')
        print(
            f'tocado o instrumento {self.cor} de tamanho {self.tamanho} do tipo {self.tipo}')


class Guitarra(Instrumento):  # Herança
    def __init__(self, cor, tamanho, cordas):  # Método construtor
        super().__init__(cor, tamanho)
        self.cordas = cordas

    def tocar(self):  # Polimorfismo
        print('Produzindo som de guitarra')
        print(
            f'tocado o instrumento {self.cor} de tamanho {self.tamanho} com {self.cordas} cordas')


class Piano(Instrumento):  # Herança
    def __init__(self, cor, tamanho, teclas):  # Método construtor
        super().__init__(cor, tamanho)
        self.teclas = teclas

    def tocar(self):  # Polimorfismo
        print(
            f'tocado o instrumento {self.cor} de tamanho {self.tamanho} com {self.teclas} teclas')
        print('Produzindo som de piano')


instrumento1 = Instrumento('Marrom', 'Grande')
instrumento1.tocar()

violino1 = Violino('Vermelho', 'Pequeno', 'Aço')
violino1.tocar()

guitarra1 = Guitarra('Preta', 'Médio', 6)
guitarra1.tocar()

piano1 = Piano('Branco', 'Grande', "Grande")
piano1.tocar()
