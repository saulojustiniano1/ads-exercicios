import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        Biblioteca livraria = new Biblioteca();
        ArrayList<Livro> arrayLivros = new ArrayList<>();
        boolean b = true;

        System.out.println("=-=-=-=-=--=-=-= Livraria =-=-=-=-=-=-=-=-=-=-=-");

        while(b){
            int op;

            System.out.println("=-=-=-=-=-=-=-= Interface =-=-=-=-=-=-=-=-=");
            System.out.println("Digite [1] para cadastrar");
            System.out.println("Digite [2] para visualizar os livros");
            System.out.println("Digite [3] para saber quantos livros tem na livraria");
            System.out.println("Digite [4] buscar livro pelo autor");
            System.out.println("Digite [5] remover livro pelo autor");
            System.out.println("Digite [6] para sair");
            System.out.println("==================================");

            op = input.nextInt();

            switch (op) {
                case 1 -> {
                    System.out.println("Informe quantos livros deseja cadastrar: ");
                    int quantidadeDeLivros = input.nextInt();
                    for (int i=0; i<quantidadeDeLivros; i++) {
                        if (i==0) {
                            input.nextLine();
                        }
                        System.out.println("Nome do livro: ");
                        String nomeDoLivro = input.nextLine();

                        System.out.println("Autor do livro: ");
                        String autorDoLivro = input.nextLine();

                        Livro livros = new Livro(nomeDoLivro, autorDoLivro);
                        livraria.adicionarLivro(livros);
                    }
                    System.out.println("_____ Cadastro realizado com sucesso! _____");
                    arrayLivros = livraria.mostrarLivros();
                }
                case 2 -> {
                    for (Livro l : arrayLivros) {
                        System.out.println("Nome: " + l.getTitulo());
                        System.out.println("Autor: " + l.getAutor());
                        System.out.println("________________________");
                    }
                }
                case 3 -> System.out.println("Na livraria tem " + livraria.tamanhoDaLivraria() + " Livros");
                case 4 -> {
                    input.nextLine();
                    System.out.println("Informe o nome do autor: ");
                    String autor = input.nextLine();

                    Livro livroAutor = livraria.buscarLivro(autor);

                    if (livroAutor != null) {
                        System.out.println("Nome: " + livroAutor.getTitulo());
                        System.out.println("Autor: " + livroAutor.getAutor());
                    } else {
                        System.out.println("Livro não encontrado!");
                    }
                }
                case 5 -> {
                    input.nextLine();
                    System.out.println("Digite o autor para ser removido: ");
                    String removeAutor = input.nextLine();

                    if(livraria.removerLivros(removeAutor)){
                        System.out.println("Livro removido com sucesso!");
                    } else {
                        System.out.println("Livro NÃO encontrado!");
                    }
                }
                case 6 -> {
                    System.out.println("Volte sempre!");
                    b = false;
                }
            }
        }
    }
}