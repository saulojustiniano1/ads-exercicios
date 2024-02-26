class Veiculo:  # Classe pai
    def __init__(self, marca, modelo):  # Método construtor
        self.marca = marca
        self.modelo = modelo

    def ligar_motor(self):
        print('Motor ligado')

    def desligar_motor(self):
        print('Motor desligado')


class Carro(Veiculo):  # Herança
    def __init__(self, marca, modelo, cor):  # Método construtor
        super().__init__(marca, modelo)
        self.cor = cor

    def ligar_motor(self):  # Polimorfismo
        print('Ligando o motor do carro')

    def desligar_motor(self):  # Polimorfismo
        print('Desligando o motor do carro')

    def ligar_radio(self):
        print('Rádio ligado')

    def desligar_radio(self):
        print('Rádio desligado')


class Moto(Veiculo):  # Herança
    def __init__(self, marca, modelo, cilindradas):  # Método construtor
        super().__init__(marca, modelo)
        self.cilindradas = cilindradas

    def ligar_motor(self):
        print('Ligando o motor da moto')

    def desligar_motor(self):
        print('Desligando o motor da moto')

    def ligar_farol(self):
        print('Farol ligado')

    def desligar_farol(self):
        print('Farol desligado')


veiculo1 = Veiculo('Volkswagen', 'Gol')  # Instanciando um objeto
veiculo1.ligar_motor()
veiculo1.desligar_motor()

carro1 = Carro('Volkswagen', 'Gol', 'Preto')  # Instanciando um objeto
carro1.ligar_motor()
carro1.ligar_radio()
carro1.desligar_radio()
carro1.desligar_motor()

moto1 = Moto('Honda', 'CG 125', 125)  # Instanciando um objeto
moto1.ligar_motor()
moto1.ligar_farol()
moto1.desligar_farol()
moto1.desligar_motor()
