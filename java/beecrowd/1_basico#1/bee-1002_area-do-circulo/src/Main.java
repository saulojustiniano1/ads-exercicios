import java.util.Scanner;
import java.util.Locale;

public class Main {
    public static void main(String[] args) {

        final var localeBrazil = new Locale("en", "US");
        Locale.setDefault(localeBrazil);

        Scanner input = new Scanner(System.in);
        input.useLocale(Locale.ENGLISH);

        double pi = 3.14159;

        double raio = input.nextDouble();

        double area = pi * (raio * raio);

        System.out.printf("A=%.4f",area);

    }
}