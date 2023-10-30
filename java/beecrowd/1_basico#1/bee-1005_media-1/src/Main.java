import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);

        Scanner input = new Scanner(System.in);

        double notaA, notaB, media;

        notaA = input.nextDouble();
        notaB = input.nextDouble();

        media = (notaA * 3.5 + notaB * 7.5) / (3.5 + 7.5);

        System.out.printf("MEDIA = %.5f%n", media); // %.5f = 5 casas decimais // %n = quebra de linha

    }
}