import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Qual o tamanho do vetor desejado? ");
        int tamanhoDoVetor = input.nextInt();

        // A IDE sugeriu que eu alterasse
        int[] vetor = new int[tamanhoDoVetor];

        System.out.println("Entrada de "+ tamanhoDoVetor +" valores");
        for(int i=0; i<tamanhoDoVetor; i++){
            System.out.print("Valor: ");
            vetor[i] = input.nextInt();
        }

        System.out.println("Print dos "+ tamanhoDoVetor +" valores digitados");
        for(int i=0; i<tamanhoDoVetor; i++) {
            System.out.print(i==0?vetor[i]: " "+vetor[i]);
        }

        int aux;
        for(int j=0; j<tamanhoDoVetor; j++) {
            for (int i = 0; i < tamanhoDoVetor-1; i++) {
                if (vetor[i] > vetor[i+1]) {
                    aux = vetor[i];
                    vetor[i] = vetor[i+1];
                    vetor[i+1] = aux;
                }
            }
        }

        System.out.println(" ");
        System.out.println("Print do vetor ordenado");
        for(int i=0; i<tamanhoDoVetor; i++){
            System.out.print(i == 0 ? vetor[i]: " "+vetor[i]);
        }

    }
}
