import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);

        Scanner input = new Scanner(System.in);

        String nomeDoVendedor;
        double salarioFixo, totalDeVendasEfetuadas, salarioComBonus;

        nomeDoVendedor = input.nextLine();
        salarioFixo = input.nextDouble();
        totalDeVendasEfetuadas = input.nextDouble();

        salarioComBonus = salarioFixo + (totalDeVendasEfetuadas * 0.15);

        System.out.printf("TOTAL = R$ %.2f%n",salarioComBonus);

    }
}