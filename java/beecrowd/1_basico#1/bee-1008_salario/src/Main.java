import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Locale.setDefault(Locale.US);

        Scanner input = new Scanner(System.in);

        int numeroDeFuncionarios, numeroDeHorasTrabalhadas;
        double horasDeTrabalhaDoFuncionario, salarioDoFuncionario;

        numeroDeFuncionarios = input.nextInt();
        numeroDeHorasTrabalhadas = input.nextInt();
        horasDeTrabalhaDoFuncionario = input.nextDouble();

        salarioDoFuncionario = numeroDeHorasTrabalhadas * horasDeTrabalhaDoFuncionario;

        System.out.println("NUMBER = "+numeroDeFuncionarios);
        System.out.printf("SALARY = U$ %.2f%n",salarioDoFuncionario); // %.2f%n = duas casas decimais // %n = quebra de linha

    }
}