import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);

        Scanner input = new Scanner(System.in);

        int tempoGastoDaViagem = input.nextInt();
        int velocidadeMedia = input.nextInt();

        double distanciaPercorrida = tempoGastoDaViagem * velocidadeMedia;

        double quantidadeDeLivrosNecessarios = distanciaPercorrida / 12;

        System.out.printf("%.3f%n",quantidadeDeLivrosNecessarios);

    }
}