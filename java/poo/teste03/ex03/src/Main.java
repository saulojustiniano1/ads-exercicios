import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        Professor professor1 = new Professor();

        System.out.println("Nome do professor: ");
        professor1.setNome(input.nextLine());

        System.out.println("Número da matricula: ");
        professor1.setMatricula(input.nextInt());

        System.out.println("Professor: "+professor1.getNome());
        System.out.println("Número da matricula: "+professor1.getMatricula());
    }
}