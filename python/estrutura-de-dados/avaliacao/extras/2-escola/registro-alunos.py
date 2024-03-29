class RegistroAlunos:
    def __init__(self):
        self.alunos = {}

    def adicionar_aluno(self, matriculo, nome, idade, nota):
        self.alunos[matriculo] = {"nome": nome, "idade": idade, "nota": nota}

    def remover_aluno(self, matriculo):
        if matriculo in self.alunos:
            self.alunos.pop(matriculo)
        else:
            return "Aluno não encontrado"

    def buscar_aluno(self, matriculo):
        if matriculo in self.alunos:
            return self.alunos[matriculo]
        else:
            return "Aluno não encontrado"

    def buscar_alunoBinario(self, matriculo):
        chaves_ordenadas = sorted(self.alunos.keys())
        inicio = 0
        fim = len(self.alunos) - 1
        while inicio <= fim:
            meio = (inicio + fim) // 2
            if chaves_ordenadas[meio] == matriculo:
                return self.alunos[meio]
            elif chaves_ordenadas[meio] < matriculo:
                inicio = meio + 1
            else:
                fim = meio - 1
        return "Aluno não encontrado"

    def buscar_alunoSequencial(self, matriculo):
        for aluno in self.alunos:
            if aluno == matriculo:
                return self.alunos[aluno]
        return "Aluno não encontrado"

    def listar_alunos(self):
        return self.alunos


registro_alunos = RegistroAlunos()

registro_alunos.adicionar_aluno(1, "João", 20, 8)
registro_alunos.adicionar_aluno(2, "Maria", 22, 9)
registro_alunos.adicionar_aluno(3, "José", 21, 10)
registro_alunos.adicionar_aluno(4, "Ana", 19, 7)
registro_alunos.adicionar_aluno(5, "Carlos", 23, 6)
registro_alunos.adicionar_aluno(6, "Mariana", 24, 5)
registro_alunos.adicionar_aluno(7, "Pedro", 25, 4)
registro_alunos.adicionar_aluno(8, "Paula", 26, 3)
registro_alunos.adicionar_aluno(9, "Lucas", 27, 2)
registro_alunos.adicionar_aluno(10, "Luciana", 28, 1)

print(registro_alunos.listar_alunos())
print(registro_alunos.buscar_aluno(2))
print(registro_alunos.remover_aluno(2))
print(registro_alunos.listar_alunos())

print(registro_alunos.buscar_alunoBinario(3))
print(registro_alunos.buscar_alunoSequencial(5))
