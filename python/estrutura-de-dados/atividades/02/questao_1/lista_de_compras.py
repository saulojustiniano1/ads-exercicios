class ListaDeCompras:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"{item} adicionado à lista de compras.")

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            print(f"{item} removido da lista de compras.")
        else:
            print(f"{item} não encontrado na lista de compras.")

    def verificar_item(self, item):
        if item in self.itens:
            print(f"{item} está na lista de compras.")
        else:
            print(f"{item} não está na lista de compras.")

    def exibir_lista(self):
        print("Lista de compras:")
        for item in self.itens:
            print("-", item)


lista_compras = ListaDeCompras()

lista_compras.adicionar_item("Maçã")
lista_compras.adicionar_item("Leite")
lista_compras.adicionar_item("Pão")
lista_compras.adicionar_item("Banana")

lista_compras.exibir_lista()

lista_compras.verificar_item("Leite")
lista_compras.verificar_item("Arroz")

lista_compras.remover_item("Pão")
lista_compras.remover_item("Café")

lista_compras.exibir_lista()
