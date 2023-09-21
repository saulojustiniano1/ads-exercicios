import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.println("Informe a marca do carro: ");
        String marcaDoCarro = input.nextLine();

        System.out.println("Informe o modelo do carro: ");
        String modeloDoCarro = input.nextLine();

        System.out.println("Qual o ano do carro: ");
        int anoDoCarro = input.nextInt();

        Carro carro1 = new Carro(marcaDoCarro, modeloDoCarro, anoDoCarro);

        carro1.imprimirDetalhes();
    }
}