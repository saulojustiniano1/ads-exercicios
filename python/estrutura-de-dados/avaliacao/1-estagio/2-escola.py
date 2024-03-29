class RegistroAlunos:
    def __init__(self):
        self.alunos = {}

    def adicionar_aluno(self, matricula, nome, idade, nota):
        self.alunos[matricula] = {"nome": nome, "idade": idade, "nota": nota}

    def remover_aluno(self, matricula):
        if matricula in self.alunos:
            del self.alunos[matricula]
        else:
            print("Aluno não encontrado")

    # def buscar_aluno(self, matricula):
    #     if matricula in self.alunos:
    #         return self.alunos[matricula]
    #     else:
    #         print("Aluno não encontrado")

    def buscar_alunoBinario(self, matricula):
        disc_ordenado = sorted(self.alunos.keys())
        inicio = 0
        fim = len(disc_ordenado) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if disc_ordenado[meio] == matricula:
                return self.alunos[matricula]
            elif disc_ordenado[meio] < matricula:
                inicio = meio + 1
            else:
                fim = meio - 1
        print("Aluno não encontrado")

    def buscar_alunoSeq(self, matricula):
        for aluno in self.alunos:
            if aluno == matricula:
                return self.alunos[matricula]
        print("Aluno não encontrado")

    def listar_alunos(self):
        for matricula, aluno in self.alunos.items():
            print(
                f"Matrícula: {matricula}, Nome: {aluno['nome']}, Idade: {aluno['idade']}, Nota: {aluno['nota']}")


escola = RegistroAlunos()
escola.adicionar_aluno(123, "Maria", 20, 9.5)
escola.adicionar_aluno(456, "João", 21, 8.5)
escola.adicionar_aluno(789, "José", 22, 7.5)
escola.adicionar_aluno(101, "Ana", 23, 6.5)
escola.adicionar_aluno(112, "Pedro", 24, 5.5)
escola.listar_alunos()
print(escola.buscar_alunoBinario(101))
print(escola.buscar_alunoSeq(789))
escola.remover_aluno(123)
escola.remover_aluno(456)
escola.listar_alunos()
