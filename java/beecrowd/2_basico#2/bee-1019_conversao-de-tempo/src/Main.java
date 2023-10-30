import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        int segundos = input.nextInt();

        int hora = segundos / 3600;
        int minuto = (segundos % 3600) / 60;
        int segundo = segundos % 60;

        System.out.println(hora + ":" + minuto + ":" + segundo);

    }
}