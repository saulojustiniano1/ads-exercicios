import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Quantos livros você quer inserir? ");
        int quantidadeDeLivros = input.nextInt();

        Livro[] livros = new Livro[quantidadeDeLivros];

        for(int i=0; i<quantidadeDeLivros; i++){
            System.out.println("===< Inserir >===");
            livros[i] = new Livro();
            input.nextLine();
            System.out.println("Insira o nome do livro: ");
            livros[i].setNome(input.nextLine());
            System.out.println("Insira o autor do livro: ");
            livros[i].setAutor(input.nextLine());
            System.out.println("Insira o ano do livro: ");
            livros[i].setAno(input.nextInt());
            System.out.println("Insira o preço do livro: ");
            livros[i].setPreco(input.nextDouble());
        }

        System.out.println(" "); // Pular linha

        for(int i=0; i< quantidadeDeLivros; i++) {
            System.out.println("===< Livro >===");
            livros[i].exibir();
        }

    }
}