import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        Animal cachorro = new Cachorro();
        Animal gato = new Gato();

        gato.emitirSom(); // Som de gato
        cachorro.emitirSom(); // Som de cachorro
    }
}