class FilaEspera:
    def __init__(self):
        self.fila_de_espera = []

    def adicionar_paciente(self, paciente):
        self.fila_de_espera.append(paciente)

    def proximo_paciente(self):
        if len(self.fila_de_espera) > 0:
            paciente = self.fila_de_espera.pop(0)
            return paciente

    def tamanho(self):
        if len(self.fila_de_espera) == 0:
            return "Não há ninguém na fila de espera"
        elif len(self.fila_de_espera) == 1:
            return "Há uma pessoa na fila de espera"
        else:
            return f"O tamanho da fila de espera é de {len(self.fila_de_espera)} pessoas"


fila_de_espera = FilaEspera()
fila_de_espera.adicionar_paciente("João")
fila_de_espera.adicionar_paciente("Maria")
fila_de_espera.adicionar_paciente("José")
print(fila_de_espera.tamanho())
print(fila_de_espera.proximo_paciente())
print(fila_de_espera.proximo_paciente())
print(fila_de_espera.tamanho())
print(fila_de_espera.proximo_paciente())
print(fila_de_espera.tamanho())
