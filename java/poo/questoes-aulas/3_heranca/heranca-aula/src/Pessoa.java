public class Pessoa {
    private String nome;
    private Conta conta;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Conta getConta() {
        return conta;
    }

    public void setConta(Conta conta) {
        this.conta = conta;
    }

    public void sacar(double valor){
        conta.debita(valor);
    }

    public void depositar(double valor){
        conta.credita(valor);
    }

    public void transfere(double valor, Pessoa pessoa){
        Conta contaDestino = pessoa.getConta();

        this.conta.debita(valor);
        contaDestino.credita(valor);

    }
}