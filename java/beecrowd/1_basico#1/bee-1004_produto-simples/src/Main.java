import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int a, b, prod;

        a = input.nextInt();
        b = input.nextInt();

        prod = a * b;

        System.out.println("PROD = "+prod);

    }
}