import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        Retangulo retangulo1 = new Retangulo();

        System.out.println("Comprimento: ");
        int comprimento = input.nextInt();
        retangulo1.setComprimento(comprimento);

        System.out.println("Largura: ");
        int largura = input.nextInt();
        retangulo1.setLargura(largura);

        System.out.println("Àrea do Retângulo: "+retangulo1.areaDoRetangulo()+"m2");
        System.out.println("Perímetro do Retângulo: "+retangulo1.perimetroDoRetangulo()+"m");
    }
}