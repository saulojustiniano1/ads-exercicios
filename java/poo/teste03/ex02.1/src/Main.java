import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        Agenda a1 = new Agenda();

        System.out.println("Nome: ");
        a1.setNome(input.nextLine());
        System.out.println("Telefone: ");
        a1.setTelefone(input.nextLine());

        String num = a1.getNome();
        String tel = a1.getTelefone();

        System.out.println("Nome: "+num);
        System.out.println("Telefone: "+tel);
    }
}