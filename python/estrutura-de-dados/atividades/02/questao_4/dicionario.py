class Contatos:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self, nome, telefone):
        self.contatos[nome] = telefone
        print(f"Contato {nome} adicionado.")

    def exibir_contatos(self):
        print("<--- Contatos --->")
        print(self.contatos)
        for nome, telefone in self.contatos.items():  # .items() returns a list of tuples
            print(f"{nome}: {telefone}")


contatos = Contatos()

contatos.adicionar_contato("João", "1234-5678")
contatos.adicionar_contato("Maria", "8765-4321")
contatos.adicionar_contato("José", "4321-5678")

contatos.exibir_contatos()
