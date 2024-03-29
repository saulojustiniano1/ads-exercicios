class Clinica:
    def __init__(self):
        self.lista_de_espera = []
        self.pacientes_atendidos = []

    def adicionar_paciente(self, paciente):
        self.lista_de_espera.append(paciente)

    def atender_proximo(self):
        if len(self.lista_de_espera) > 0:
            paciente = self.lista_de_espera.pop(0)
            self.pacientes_atendidos.append(paciente)

    def listar_pacientes(self):
        return self.lista_de_espera

    def pacientes_atendidos(self):
        return self.pacientes_atendidos


clinica = Clinica()
clinica.adicionar_paciente("João")
clinica.adicionar_paciente("Maria")
clinica.adicionar_paciente("José")
clinica.atender_proximo()
clinica.atender_proximo()
print(clinica.listar_pacientes())
print(clinica.pacientes_atendidos)
