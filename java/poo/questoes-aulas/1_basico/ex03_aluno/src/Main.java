import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.println("Nome do aluno: ");
        String nomeDoAluno = input.nextLine();

        System.out.println("Matricula do aluno: ");
        String matriculaDoAluno = input.nextLine();

        System.out.println("Nota do Aluno: ");
        double notaDoAluno = input.nextDouble();

        Aluno aluno1 = new Aluno(nomeDoAluno, matriculaDoAluno, notaDoAluno);

        if(aluno1.estaAprovado()){
            System.out.println("Aluno está APROVADO!");
        } else {
            System.out.println("Aluno está REPROVADO!");
        }
    }
}