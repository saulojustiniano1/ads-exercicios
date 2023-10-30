import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int a, b, soma;

        a = input.nextInt();
        b = input.nextInt();

        soma = a + b;

        System.out.println("X = " + soma);

    }
}