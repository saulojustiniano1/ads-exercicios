class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None


class FilaEncadeada:
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__tamanho = 0

    def __len__(self):
        return self.__tamanho

    def __str__(self):
        return f'Fila Encadeada: [{self.__str_recursivo(self.__inicio)}]'

    def __str_recursivo(self, no):
        if no is None:
            return ""
        return (
            f"{no.dado},{self.__str_recursivo(no.proximo)}"
            if no.proximo is not None
            else f"{no.dado}"
        )

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        self.__iter_no = self.__inicio
        return self

    def __next__(self):
        if self.__iter_no is None:
            raise StopIteration
        dado = self.__iter_no.dado
        self.__iter_no = self.__iter_no.proximo
        return dado

    def enfileirar(self, dado):
        novo_no = No(dado)
        if self.__inicio is None:
            self.__inicio = novo_no
        else:
            self.__fim.proximo = novo_no
        self.__fim = novo_no
        self.__tamanho += 1

    def desenfileirar(self):
        if self.__inicio is None:
            raise IndexError("A fila está vazia")
        dado = self.__inicio.dado
        self.__inicio = self.__inicio.proximo
        self.__tamanho -= 1
        if self.__inicio is None:
            self.__fim = None
        return f'Desenfileirando -> {dado}'

    def primeiro(self):
        if self.__inicio is None:
            raise IndexError("A fila está vazia")
        return self.__inicio.dado

    def vazia(self):
        return self.__tamanho == 0

    def limpar(self):
        self.__inicio = None
        self.__fim = None
        self.__tamanho = 0


fila_encadeada = FilaEncadeada()
fila_encadeada.enfileirar(1)
fila_encadeada.enfileirar(2)
fila_encadeada.enfileirar(3)
print(fila_encadeada)
print(fila_encadeada.desenfileirar())
print(fila_encadeada.desenfileirar())
print(fila_encadeada)
