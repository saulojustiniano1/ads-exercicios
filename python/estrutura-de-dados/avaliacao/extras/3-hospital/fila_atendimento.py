class FilaAtendimento:
    def __init__(self):
        self.fila_de_atendimento = {}

    def adicionar_paciente(self, registro, nome, idade, prioridade):
        self.fila_de_atendimento[registro] = {
            "nome": nome, "idade": idade, "prioridade": prioridade}

    def remover_proximo_paciente(self):
        if len(self.fila_de_atendimento) > 0:
            registro = min(self.fila_de_atendimento.keys())
            paciente = self.fila_de_atendimento.pop(registro)
            return paciente

    def listar_pacientes(self):
        return self.fila_de_atendimento


fila_atendimento = FilaAtendimento()
fila_atendimento.adicionar_paciente(1, "João", 30, False)
fila_atendimento.adicionar_paciente(2, "Maria", 25, True)
fila_atendimento.adicionar_paciente(3, "José", 40, False)
fila_atendimento.adicionar_paciente(4, "Ana", 35, True)
fila_atendimento.adicionar_paciente(5, "Pedro", 20, False)
print(fila_atendimento.listar_pacientes())
print(fila_atendimento.remover_proximo_paciente())
print(fila_atendimento.remover_proximo_paciente())
print(fila_atendimento.listar_pacientes())
