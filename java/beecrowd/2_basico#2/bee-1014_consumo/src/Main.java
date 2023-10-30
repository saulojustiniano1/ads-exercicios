import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);

        Scanner input = new Scanner(System.in);

        int distanciaTotalPercorrida = input.nextInt();
        double totalDoCombustivelGasto = input.nextDouble();

        double consumoMedio = distanciaTotalPercorrida / totalDoCombustivelGasto;

        System.out.printf("%.3f km/l%n", consumoMedio);

    }
}