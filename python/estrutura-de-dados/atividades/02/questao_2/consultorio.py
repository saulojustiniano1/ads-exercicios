class Consultorio:
    def __init__(self):
        self.pacientes = []

    def adicionar_paciente(self, paciente):
        self.pacientes.append(paciente)
        print(f"{paciente} adicionado à lista de espera do consultório.")

    def lista_espera(self):
        print("Lista de espera do consultório:")
        for indice, paciente, in enumerate(self.pacientes):
            print(f"{indice + 1} - {paciente}")

    def atentimento(self):
        paciente = self.pacientes.pop(0)
        print(f"{paciente} foi atendido(a).")


consultorio = Consultorio()

consultorio.adicionar_paciente("José")
consultorio.adicionar_paciente("Saulo")
consultorio.adicionar_paciente("Thiago")
consultorio.adicionar_paciente("Patrick")
consultorio.adicionar_paciente("Gian")

consultorio.lista_espera()
consultorio.atentimento()
consultorio.lista_espera()
consultorio.atentimento()
consultorio.lista_espera()
