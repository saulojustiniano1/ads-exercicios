import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.println("Digite a marca do carro: ");
        String marcaDoCarro = input.nextLine();

        System.out.println("Digite o modelo do carro: ");
        String modeloDoCarro = input.nextLine();

        System.out.println("Digite o ano do carro: ");
        int anoDoCarro = input.nextInt();

        Carro carro1 = new Carro(marcaDoCarro, modeloDoCarro, anoDoCarro);

        carro1.exibir(marcaDoCarro, modeloDoCarro, anoDoCarro);
    }
}