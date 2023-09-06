import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        // A IDE sugeriu que eu alterasse de "int vetor[] | int[] vetor"
        int[] vetor = new int[10];

        System.out.println("Entrada de valores");
        for(int i=0; i<10; i++){
            System.out.print(">>> ");
            vetor[i] = input.nextInt();
        }

        System.out.println("Print dos valores digitados");
        for(int i=0; i<10; i++) {
            System.out.print(i==0?vetor[i]: " "+vetor[i]);
        }

        int aux;
        for(int j=0; j<10; j++) {
            for (int i = 0; i < 10-1; i++) {
                if (vetor[i] > vetor[i+1]) {
                    aux = vetor[i];
                    vetor[i] = vetor[i+1];
                    vetor[i+1] = aux;
                }
            }
        }

        System.out.println(" ");
        System.out.println("Print do vetor ordenado");
        for(int i=0; i<10; i++){
            System.out.print(i == 0 ? vetor[i]: " "+vetor[i]);
        }

    }
}