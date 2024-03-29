class FilaEspera:
    def __init__(self):
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def proximo_paciente(self):
        if len(self.pacientes) > 0:
            return self.pacientes.pop(0)

    def tamanho(self):
        if len(self.pacientes) == 0:
            return "Não há ninguém na fila de espera"
        elif len(self.pacientes) == 1:
            return "Há uma pessoa na fila de espera"
        else:
            return f"O tamanho da fila de espera é de {len(self.pacientes)} pessoas"


class Clinica:
    def __init__(self):
        self.pacientes_atendidos = []  # Atributo de instância
        self.fila_espera = FilaEspera()  # Composição de objetos (FilaEspera)

    def atender_proximo(self):
        paciente = self.fila_espera.proximo_paciente()
        self.pacientes_atendidos.append(paciente)

    def pacientes_atendidos(self):
        if len(self.pacientes_atendidos) == 0:
            return "Não há pacientes atendidos"
        elif len(self.pacientes_atendidos) == 1:
            return "Há um paciente atendido"
        else:
            return f"O número de pacientes atendidos é de {len(self.pacientes_atendidos)}"


clinica = Clinica()
clinica.fila_espera.adicionar_paciente("Maria")
clinica.fila_espera.adicionar_paciente("João")
clinica.fila_espera.adicionar_paciente("José")
clinica.fila_espera.adicionar_paciente("Ana")
clinica.fila_espera.adicionar_paciente("Pedro")
clinica.atender_proximo()
print(clinica.fila_espera.tamanho())
print(clinica.pacientes_atendidos)
clinica.atender_proximo()
clinica.atender_proximo()
print(clinica.pacientes_atendidos)
print(clinica.fila_espera.tamanho())
