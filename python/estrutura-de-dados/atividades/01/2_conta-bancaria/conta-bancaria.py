class ContaBancaria:
    def __init__(self, saldo):  # Método construtor
        self.__saldo = saldo  # Atributo privado

    def get_saldo(self):
        return self.__saldo  # Retorna o saldo

    def set_saldo(self, novo_saldo):
        if novo_saldo >= 0:
            self.__saldo = novo_saldo  # Atualiza o saldo
        else:
            print('Saldo inválido')

    def depositar(self, valor_depositado):
        if valor_depositado > 0:  # Verifica se o valor depositado é válido
            novo_saldo = self.get_saldo() + valor_depositado  # Calcula o novo saldo
            self.set_saldo(novo_saldo)  # Atualiza o saldo
            print(f"Saldo: {self.get_saldo()}")
            print("Depósito realizado com sucesso")
        else:
            print('Valor inválido (deve ser maior que 0)')

    def sacar(self, valor_sacado):
        if valor_sacado > 0 and valor_sacado <= self.__saldo:  # Verifica se o valor sacado é válido
            novo_saldo = self.get_saldo() - valor_sacado  # Calcula o novo saldo
            self.set_saldo(novo_saldo)  # Atualiza o saldo
            print(f"Saldo: {self.get_saldo()}")
            print("Saque realizado com sucesso")
        else:
            print('Valor inválido (deve ser maior que 0 e menor ou igual ao saldo)')


conta_bancaria1 = ContaBancaria(1412)  # Cria um objeto da classe ContaBancaria
conta_bancaria1.depositar(50)  # Deposita 50 reais
conta_bancaria1.sacar(1000)  # Tenta sacar 1000 reais
