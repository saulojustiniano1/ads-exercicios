import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        // A IDE recomendou usar o int[][] matriz ao invez de int matriz[][]
        int[][] matriz = new int[3][2];

        for(int i=0; i<3; i++) {
            for(int j=0; j<2; j++) {
                matriz[i][j] = input.nextInt();
            }
        }

        System.out.println("Matriz:");
        for(int i=0; i<3; i++) {
            for(int j=0; j<2; j++){
                System.out.print(matriz[i][j] + " ");
            }
            System.out.println();
        }

        // Quando for fazer a matrix transposta lembre de alterar o indice[i][j] para indice[j][i]
        System.out.println("Matriz transposta:");
        for(int i=0; i<2; i++) {
            for(int j=0; j<3; j++){
                System.out.print(matriz[j][i] + " ");
            }
            System.out.println();
        }
    }
}

