import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);

        Scanner input = new Scanner(System.in);

        double valor = input.nextDouble();

        // Notas

        double nota100 = valor / 100;
        double resto100Notas = valor % 100;
        int nota100Int = (int) nota100;

        double nota50 = resto100Notas / 50;
        double resto50Notas = resto100Notas % 50;
        int nota50Int = (int) nota50;

        double nota20 = resto50Notas / 20;
        double resto20 = resto50Notas % 20;
        int nota20Int = (int) nota20;

        double nota10 = resto20 / 10;
        double resto10Notas = resto20 % 10;
        int nota10Int = (int) nota10;

        double nota5 = resto10Notas / 5;
        double resto5 = resto10Notas % 5;
        int nota5Int = (int) nota5;

        double nota2 = resto5 / 2;
        double resto2Notas = resto5 % 2;
        int nota2Int = (int) nota2;

        // Moedas

        double resto1Moeda = resto2Notas % 1;
        int moeda1Int = (int) resto2Notas;

        double moeda50 = resto1Moeda / 0.50;
        double resto50Moeda = resto1Moeda % 0.50;
        int moeda50Int = (int) moeda50;

        double moeda25 = resto50Moeda / 0.25;
        double resto25Moeda = resto50Moeda % 0.25;
        int moeda25Int = (int) moeda25;

        double moeda10 = resto25Moeda / 0.10;
        double resto10Moeda = resto25Moeda % 0.10;
        int moeda10Int = (int) moeda10;

        double moeda5 = resto10Moeda / 0.05;
        double resto5Moeda = resto10Moeda % 0.05;
        int moeda5Int = (int) moeda5;

        double moeda01 = resto5Moeda / 0.01;
        int moeda01Int = (int) Math.floor(moeda01);

        System.out.println(moeda5);
        System.out.println(moeda01);

        System.out.println("NOTAS:");
        System.out.println(nota100Int + " nota(s) de R$ 100.00");
        System.out.println(nota50Int + " nota(s) de R$ 50.00");
        System.out.println(nota20Int + " nota(s) de R$ 20.00");
        System.out.println(nota10Int + " nota(s) de R$ 10.00");
        System.out.println(nota5Int + " nota(s) de R$ 5.00");
        System.out.println(nota2Int + " nota(s) de R$ 2.00");
        System.out.println("MOEDAS:");
        System.out.println(moeda1Int + " moeda(s) de R$ 1.00");
        System.out.println(moeda50Int + " moeda(s) de R$ 0.50");
        System.out.println(moeda25Int + " moeda(s) de R$ 0.25");
        System.out.println(moeda10Int + " moeda(s) de R$ 0.10");
        System.out.println(moeda5Int + " moeda(s) de R$ 0.05");
        System.out.println(moeda01Int + " moeda(s) de R$ 0.01");
    }
}