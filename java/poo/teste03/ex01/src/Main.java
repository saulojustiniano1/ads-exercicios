import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Calculo c1 = new Calculo();
        Scanner input = new Scanner(System.in);

        System.out.print("A: ");
        c1.setA(input.nextInt());

        System.out.print("B: ");
        c1.setB(input.nextInt());

        int a = c1.getA();
        int b = c1.getB();
        int s = c1.soma(a, b);

        if(s == 8) {
            System.out.println("A soma é 8!");
        } else{
            System.out.println("A soma não é 8!");
        }
    }
}