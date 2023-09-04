import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.println("Nome: ");
        String a = input.nextLine();
        System.out.println("Telefone: ");
        String b = input.nextLine();

        Agenda a1 = new Agenda(a, b);

        a1.exibir();
    }
}