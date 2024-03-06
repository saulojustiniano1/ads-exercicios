# Dicionário

```python
def adicionar_contato(self, nome, telefone):
    self.contatos[nome] = telefone
    print(f"Contato {nome} adicionado.")
```

linha específica **self.contatos[nome] = telefone**

Essa linha está adicionando uma entrada ao dicionário contatos da instância da classe.
**Vamos analisar cada parte:**

**self:** Este é um parâmetro especial que representa a instância da classe.
Dentro de métodos de classe, self é usado para acessar atributos e métodos da própria instância.

**self.contatos:** Isso está acessando o atributo contatos da instância da classe.
Presumivelmente, em algum lugar anterior na definição da classe, você teria algo
como self.contatos = {} para inicializar o dicionário.

**[nome]:** Isso usa o valor da variável nome como chave para acessar ou criar
uma entrada no dicionário contatos. Se já houver uma entrada com a chave igual a
nome, o valor associado a essa chave será substituído pelo novo valor de telefone.

**= telefone:** Isso atribui o valor da variável telefone à entrada do dicionário
com a chave nome.
