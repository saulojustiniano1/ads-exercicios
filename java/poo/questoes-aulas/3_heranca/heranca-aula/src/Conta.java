public class Conta {
    protected int num;
    protected double saldo;


    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public void credita(double valor){
        System.out.println("valor: "+valor);
        this.saldo += valor;
    }

    public void debita(double valor){
        this.saldo -= valor;
    }
}