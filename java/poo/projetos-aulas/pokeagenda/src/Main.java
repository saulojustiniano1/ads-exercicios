import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Pokeagenda pokeagenda = new Pokeagenda();
        Scanner input = new Scanner(System.in);
        ArrayList<Pokemon> arrayPokemons;
        boolean sair = true;

        while(sair){
            System.out.println("Digite [1] Receber Pokemon");
            System.out.println("Digite [2] Exibir Pokemons");
            System.out.println("Digite [3] Buscar Pokemon");
            System.out.println("Digite [4] Remover Pokemon");
            System.out.println("Digite [5] Sair");
            System.out.println("Digite uma opção: ");
            int opcao = input.nextInt();

            switch (opcao){
                case 1 -> {
                    System.out.println("Digite o nome do Pokemon: ");
                    String nome = input.next();
                    System.out.println("Digite o tipo do Pokemon: ");
                    String tipo = input.next();
                    System.out.println("Digite o nivel do Pokemon: ");
                    int nivel = input.nextInt();

                    Pokemon pokemon = new Pokemon(nome, tipo, nivel); // Instancia um novo Pokemon // Cria um novo objeto Pokemon
                    pokeagenda.receberPokemon(pokemon); // Adiciona o objeto Pokemon no ArrayList de Pokemons
                }
                case 2 -> {
                    arrayPokemons = pokeagenda.exibirPokemon(); // Recebe o ArrayList de Pokemons
                    for (Pokemon p : arrayPokemons) { // Percorre o ArrayList de Pokemons
                        System.out.println(p); // Imprime o Pokemon
                    }
                }
                case 3 -> {
                    System.out.println("Digite o nome do Pokemon: ");
                    String nomePokemon = input.next();
                    if (pokeagenda.buscarPokemons(nomePokemon)) {
                        System.out.println("Pokemon encontrado!");
                    } else {
                        System.out.println("Pokemon não encontrado!");
                    }
                }
                case 4 -> {
                    System.out.println("Digite o nome do Pokemon: ");
                    String nomePokemonRemover = input.next();
                    if (pokeagenda.excluirPokemon(nomePokemonRemover)) {
                        System.out.println("Pokemon removido!");
                    } else {
                        System.out.println("Pokemon não encontrado!");
                    }
                }
                case 5 -> {
                    sair = false;
                }
                default -> {
                    System.out.println("Valor invalido");
                }
            }
        }
    }
}