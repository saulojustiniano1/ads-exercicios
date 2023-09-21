import java.util.ArrayList;

public class Pokeagenda {
    ArrayList<Pokemon> pokemons = new ArrayList<>();

    public void receberPokemon(Pokemon pokemon){
        this.pokemons.add(pokemon);
    }

    public ArrayList<Pokemon> exibirPokemon(){
        return this.pokemons;
    }

    public boolean buscarPokemons(String pokemon){
        for (Pokemon p : this.pokemons) {
            if(p.getNome().equals(pokemon)){
                return true;
            }
        }
        return false;
    }

    public boolean excluirPokemon(String pokemon){
        for(Pokemon p : this.pokemons){
            if(p.getNome().equals(pokemon)){
                this.pokemons.remove(p);
                return true;
            }
        }
        return false;
    }
}
