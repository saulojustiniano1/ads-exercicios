import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        Professor professor1 = new Professor();
        Disciplina disciplina1 = new Disciplina();
        ArrayList<Aluno> arrayAlunos = new ArrayList<Aluno>();

        System.out.println("Nome do professor: ");
        String p1 = input.nextLine();
        professor1.setNome(p1);

        System.out.println("Nome da diciplina: ");
        String d1 = input.nextLine();
        disciplina1.setNome(d1);
        disciplina1.setProfessor(professor1);

        System.out.println("Número da matricula: ");
        String mP1 = input.nextLine();
        professor1.setMatricula(mP1);

        System.out.println("Quantos alunos vc quer cadastrar? ");
        int quantidadeDeAlunos = input.nextInt();

        for(int i=0; i<quantidadeDeAlunos; i++){
            if(i==0){
                input.nextLine();
            }

            System.out.println("Nome do aluno: ");
            String a1 = input.nextLine();

            System.out.println("Número da matricula: ");
            String mA1 = input.nextLine();

            Aluno aluno1 = new Aluno(a1, mA1);
            disciplina1.setAlunos(aluno1);
        }

        arrayAlunos = disciplina1.getAlunos();

        System.out.println("=-=-=-=-=-=-=- Alunos =-=-=-=-=-=-=-=-=");
        for(Aluno a: arrayAlunos){
            System.out.println("Aluno: "+a.getNome());
            System.out.println("Matricula: "+a.getMatricula());
        }

        System.out.println("=-=-=-=-=-=-=-=-= Professor =-=-=-=-=-=-=-=-=-=");
        System.out.println("Professor: "+disciplina1.getProfessor().getNome());
        System.out.println("Diciplina: "+disciplina1.getNome());
        System.out.println("Matricula: "+disciplina1.getProfessor().getMatricula());
    }
}