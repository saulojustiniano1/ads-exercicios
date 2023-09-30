public class Poupanca extends Conta {

    public Poupanca(int num, double saldo){
        super.num = num;
        super.saldo = saldo;
    }

    public void credita(double valor){ // alterar credita para juros
        double calculo = valor * 0.1;
        super.saldo += calculo;
    }
}
