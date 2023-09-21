public class Banco {
    private String nomeDoTitular;
    private String numeroDaConta;
    private double saldo;

    public String getNomeDoTitular() {
        return nomeDoTitular;
    }

    public void setNomeDoTitular(String nomeDoTitular) {
        this.nomeDoTitular = nomeDoTitular;
    }

    public String getNumeroDaConta() {
        return numeroDaConta;
    }

    public void setNumeroDaConta(String numeroDaConta) {
        this.numeroDaConta = numeroDaConta;
    }

    public void depositarDinheiro(double saldo){
        this.saldo = saldo;
    }

    public void sacarDinheiro(double saldo){
        this.saldo -= saldo;
    }

    public double saldoAtual(){
        return this.saldo;

    }

    public void informacoesPessoais(){
        System.out.println("Nome do Titular: "+getNomeDoTitular());
        System.out.println("Número da conta: "+getNumeroDaConta());
    }
}
