class FilaAtentimento:
    def __init__(self):
        self.info_pacientes = {}
        self.ordem_atendimento = []

    def adicionar_paciente(self, registro, nome, idade, prioridade):
        self.info_pacientes[registro] = {
            "nome": nome, "idade": idade, "prioridade": prioridade}
        self.ordem_atendimento.append(registro)

    def remover_proximo_paciente(self):
        if len(self.ordem_atendimento) > 0:
            registro = self.ordem_atendimento.pop(0)
            del self.info_pacientes[registro]
            return registro

    def listar_pacientes(self):
        for registro, paciente in self.info_pacientes.items():
            print(
                f"Registro: {registro}, Nome: {paciente['nome']}, Idade: {paciente['idade']}, Prioridade: {paciente['prioridade']}")


hospital = FilaAtentimento()
hospital.adicionar_paciente(123, "Maria", 20, "Alta")
hospital.adicionar_paciente(456, "João", 21, "Média")
hospital.adicionar_paciente(789, "José", 22, "Baixa")
hospital.adicionar_paciente(101, "Ana", 23, "Alta")
hospital.adicionar_paciente(112, "Pedro", 24, "Média")
hospital.listar_pacientes()
print(hospital.remover_proximo_paciente())
print(hospital.remover_proximo_paciente())
hospital.listar_pacientes()
