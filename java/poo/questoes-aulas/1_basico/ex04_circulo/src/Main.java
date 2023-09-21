import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.println("Informe a raio do circulo: ");
        double inputRaio = input.nextDouble();

        Circulo circulo1 = new Circulo(inputRaio);

        circulo1.exibirResultado();
    }
}