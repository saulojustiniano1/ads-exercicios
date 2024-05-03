class Node:
    def __init__(self, reserva):
        self.reserva = reserva
        self.next = None


class PilhaEncadeadaComoFila:
    def __init__(self):
        self.cabeca = None
        self.cauda = None

    def vazio(self):
        return self.cabeca is None

    def adicionar(self, reserva):
        novo_node = Node(reserva)
        if self.vazio():
            self.cabeca = novo_node
            self.cauda = novo_node
        else:
            self.cauda.next = novo_node
            self.cauda = novo_node

    def remover(self):
        if self.vazio():
            raise Exception("Fila vazia")

        reserva_topo = self.cabeca.reserva
        self.cabeca = self.cabeca.next
        if self.cabeca is None:
            self.cauda = None
        return reserva_topo

    def olhar_pilha(self):
        if self.vazio():
            raise Exception("Fila vazia")

        return self.cabeca.reserva

    def __str__(self):
        if self.vazio():
            return "Fila vazia"

        string_fila = ""
        node_atual = self.cabeca
        while node_atual:
            string_fila += f"{node_atual.reserva}\n"
            node_atual = node_atual.next

        return string_fila.strip()


fila_reservas = PilhaEncadeadaComoFila()

reserva1 = "Charles Oliveira", 2, "2024-05-05", "19:00"
reserva2 = "Fernando Neto", 4, "2024-05-06", "21:30"
reserva3 = "Saulo Justiniano", 3, "2024-05-05", "18:00"

fila_reservas.adicionar(reserva1)
fila_reservas.adicionar(reserva2)
fila_reservas.adicionar(reserva3)

print("======================== Fila de Reservas =====================")
print(fila_reservas)
print()

proxima_reserva = fila_reservas.remover()
print("======================= Próxima reserva ========================")
print(proxima_reserva)
print()

proxima_reserva_sem_remover = fila_reservas.olhar_pilha()
print("=================== Próxima reserva (sem remover) ==============")
print(proxima_reserva_sem_remover)
print()

print("========================= Fila de Reservas =====================")
print(fila_reservas)
