import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        Banco banco1 = new Banco();
        boolean parar = true;

        System.out.println("Nome do titular: ");
        String nomeDotitular = input.nextLine();
        banco1.setNomeDoTitular(nomeDotitular);

        System.out.println("Número da conta: ");
        String numeroDaConta = input.nextLine();
        banco1.setNumeroDaConta(numeroDaConta);

        while(parar){
            System.out.println("Digite [1] para depositar");
            System.out.println("Digite [2] para sacar");
            System.out.println("Digite [3] para sair");
            int op = input.nextInt();

            switch (op){
                case 1 -> {
                    System.out.println("Valor para depositar: R$");
                    double depositar = input.nextDouble();
                    banco1.depositarDinheiro(depositar);
                }
                case 2 -> {
                    System.out.println("Valor para sacar: R$");
                    double sacar = input.nextDouble();
                    banco1.sacarDinheiro(sacar);
                }
                case 3 -> {
                    parar = false;
                }
            }
        }

        banco1.informacoesPessoais();
        System.out.println("===================");
        System.out.println("Saldo Atual: "+banco1.saldoAtual());
    }
}