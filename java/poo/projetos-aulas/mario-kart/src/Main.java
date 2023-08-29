import java.util.Scanner;
import java.util.Random;

public class Main {
    public static void main(String[] args) {

        Kart k1 = new Kart();
        Personagem p1 = new Personagem();
        Scanner input = new Scanner(System.in);
        Random random = new Random();

        boolean b = true;

        System.out.println("==-==-==-==-== Bem Vindo ao Super Lírios Kart ==-==-==-==-==");

        System.out.println("Digite [1] para iniciar o jogo");
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
                int op;
                int escolhe;

                System.out.println("Digite [1] para acelerar");
                System.out.println("Digite [2] para frear");
                System.out.println("Digite qualquer outra coisa para sair");
                System.out.println("========================================");

                op = input.nextInt();

                switch (op) {
                    case 1:
                        System.out.println("Apareceram 3 caixas surpresas");

                        escolhe = random.nextInt(3);

                        System.out.println("============================================");

                        switch (escolhe) {
                            case 0:
                                p1.ultrapassa();
                                System.out.println("O kart ultrapassou!");
                                System.out.println("Posição Atual: "+p1.getPosicao());

                                if(p1.getPosicao() == 1){
                                    System.out.println("PARABÉNS VOCÊ GANHOU!!!!");
                                    b = false;
                                }
                            break;
                            case 1:
                                p1.pegarMoedas();
                                System.out.println("O personagem pegou uma moeda!");
                                System.out.println("Quantidade de moedas: "+p1.getMoedas());
                            break;
                            case 2:
                                k1.bateKart();
                                System.out.println("O kart bateu!");
                                System.out.println("Você PERDEU uma moeda!!");
                                System.out.println("Moedas: "+p1.getMoedas());
                                System.out.println("Vida do kart: "+k1.getVidaKart()+"%");

                                if(k1.getVidaKart() == 0){
                                    System.out.println("O carro explodiu!");
                                    b = false;
                                }
                            break;
                        }
                    break;

                    case 2:
                        System.out.println("Você freou o kart");
                        k1.freaKart();
                    break;

                }

            }
        }
        System.out.println("=-=-=-=-=-=- Stats da partida =-=-=-=-=-=");
        System.out.println("Posição: "+p1.getPosicao());
        System.out.println("Vida do kart: "+k1.getVidaKart()+"%");
        System.out.println("Quantidade de moedas totais: "+p1.getMoedas());
        System.out.println("Personagem: "+p1.getNome());
        System.out.println("Cor do kart: "+k1.getCor());


    }
}