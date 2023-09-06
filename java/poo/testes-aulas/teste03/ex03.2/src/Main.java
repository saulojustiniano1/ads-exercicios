import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        Professor professor1 = new Professor();
        Diciplina diciplina1 = new Diciplina();

        System.out.println("Nome do professor: ");
        String p1 = input.nextLine();
        professor1.setNome(p1);

        System.out.println("Nome da diciplina: ");
        String d1 = input.nextLine();
        diciplina1.setNome(d1);
        diciplina1.setProfessor(professor1);

        System.out.println("Número da matricula: ");
        String m1 = input.nextLine();
        professor1.setMatricula(m1);

        System.out.println("Professor: "+diciplina1.getProfessor().getNome());
        System.out.println("Diciplina: "+diciplina1.getNome());
        System.out.println("Número da matricula: "+diciplina1.getProfessor().getMatricula());
    }
}