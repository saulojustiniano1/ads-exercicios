public class Main {

    public static void main(String[] args) {

        Poupanca c1 = new Poupanca(1,60);
        Poupanca c2 = new Poupanca(2,700);

        PessoaFisica p1 = new PessoaFisica();
        PessoaFisica p2 = new PessoaFisica();

        p1.setConta(c1);
        p2.setConta(c2);

        p1.setNome("Pedro");
        p2.setNome("Ester");

        System.out.println("Nome: "+p1.getNome()+" saldo: "+p1.getConta().getSaldo());
        System.out.println("Nome: "+p2.getNome()+" saldo: "+p2.getConta().getSaldo());
        System.out.println("-----------------------------------------------");

        p1.depositar(50); // p1 deposita 50
        p2.depositar(400); // p2 deposita 400

        System.out.println("Nome: "+p1.getNome()+" saldo: "+p1.getConta().getSaldo());
        System.out.println("Nome: "+p2.getNome()+" saldo: "+p2.getConta().getSaldo());
        System.out.println("-----------------------------------------------");

        p2.transfere(60, p1); // p2 transfere 60 para p1

        System.out.println("Nome: "+p1.getNome()+" saldo: "+p1.getConta().getSaldo());
        System.out.println("Nome: "+p2.getNome()+" saldo: "+p2.getConta().getSaldo());
        System.out.println("-----------------------------------------------");
    }
}