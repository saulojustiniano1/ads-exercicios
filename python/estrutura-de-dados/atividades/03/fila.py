class Fila:
    def __init__(self):
        self.fila = []

    def enfileirar(self, valor):
        self.fila.append(valor)
        print(f'Enfileirando -> {valor}')

    def desenfileirar(self):
        if not self.vazia():
            return f'Desenfileirando -> {self.fila.pop(0)}'

    def vazia(self):
        return len(self.fila) == 0

    def __str__(self):
        return f'Fila: {self.fila}'


fila = Fila()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)
print(fila)
print(fila.desenfileirar())
print(fila.desenfileirar())
print(fila)
