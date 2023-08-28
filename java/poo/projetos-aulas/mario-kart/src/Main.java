import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Kart k1 = new Kart();
        Personagem p1 = new Personagem();
        Scanner input = new Scanner(System.in);

        boolean b = true;

//        System.out.println("Personagem: "+p1.getNome());
//        System.out.println("Cor do kart ("+p1.getNome()+"): "+k1.getCor());
//        System.out.println("Posição Atual: "+p1.getPosicao());
//        System.out.println("Quantidade de moedas: "+p1.getMoedas());
//
//        System.out.println("Digite 1 para acelerar.");
//        System.out.println("Digite 2 para frear.");

        System.out.println("========= Bem vindo ao Super lírios kart =======");

        System.out.println("Digite 1 para iniciar o jogo");
        System.out.println("Digite qualquer outra coisa para sair do jogo");

        int opcao = input.nextInt();

        if(opcao == 1){
            input.nextLine();
            System.out.println("Digite o nome do personagem: ");
            p1.setNome(input.nextLine());
            p1.setMotortista(k1);
            System.out.println("Digite a cor do kart desejado: ");
            k1.setCor(input.nextLine());
            k1.setPersonagem(p1);

            while(b){
                int op = 0;

                System.out.println("Digite 1 para acelerar");
                System.out.println("Digite 2 para frear");
                System.out.println("Digite qualquer outra coisa para sair");

                switch (op) {
                    case 1:
                        System.out.println("Apareceram 3 caixas surpresas");
                        System.out.println("Digite 1, 2 ou 3 para abrir elas");
//                        switch (op) {
//                            case 1:
//
//                        }

                }

            }
        }

//        int op = 0;
//
//        switch (op){
//            case 1:
//
//                switch (op) {
//
//                }
//            break;
//            case 2:
//                k1.freaKart();
//            break;
//            default:
//                System.out.println("Digite um número válido.");
//        }

    }
}