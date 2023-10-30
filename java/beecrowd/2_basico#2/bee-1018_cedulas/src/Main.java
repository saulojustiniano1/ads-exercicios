import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int valor = input.nextInt();

        int nota100 = valor / 100; // 576 / 100 = 5
        int resto100 = valor % 100; // 576 % 100 = 76

        int nota50 = resto100 / 50; // 76 / 50 = 1
        int resto50 = resto100 % 50; // 76 % 50 = 26

        int nota20 = resto50 / 20; // 26 / 20 = 1
        int resto20 = resto50 % 20; // 26 % 20 = 6

        int nota10 = resto20 / 10; // 6 / 10 = 0
        int resto10 = resto20 % 10; // 6 % 10 = 6

        int nota05 = resto10 / 5; // 6 / 5 = 1
        int resto05 = resto10 % 5; // 6 % 5 = 1

        int nota02 = resto05 / 2; // 1 / 2 = 0

        int nota01 = resto05 % 2; // 1 / 1 = 1

        System.out.println(valor);
        System.out.println(nota100 + " nota(s) de R$ 100,00");
        System.out.println(nota50 + " nota(s) de R$ 50,00");
        System.out.println(nota20 + " nota(s) de R$ 20,00");
        System.out.println(nota10 + " nota(s) de R$ 10,00");
        System.out.println(nota05 + " nota(s) de R$ 5,00");
        System.out.println(nota02 + " nota(s) de R$ 2,00");
        System.out.println(nota01 + " nota(s) de R$ 1,00");

    }
}