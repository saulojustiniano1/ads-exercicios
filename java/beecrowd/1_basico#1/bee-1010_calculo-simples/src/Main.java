import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);

        Scanner input = new Scanner(System.in);

        int codigoDaPeca1, numeroDaPecas1, codigoDaPeca2, numeroDaPecas2;
        double valorUnitarioDaPeca1, valorUnitarioDaPeca2, valorPago;

        codigoDaPeca1 = input.nextInt();
        numeroDaPecas1 = input.nextInt();
        valorUnitarioDaPeca1 = input.nextDouble();

        codigoDaPeca2 = input.nextInt();
        numeroDaPecas2 = input.nextInt();
        valorUnitarioDaPeca2 = input.nextDouble();

        valorPago = (numeroDaPecas1 * valorUnitarioDaPeca1) + (numeroDaPecas2 * valorUnitarioDaPeca2);

        System.out.printf("VALOR A PAGAR: R$ %.2f%n",valorPago);

    }
}