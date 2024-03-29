import java.util.ArrayList;

public class Biblioteca {

    ArrayList<Livro> livros = new ArrayList<>();

    public void adicionarLivro(Livro livro){
        this.livros.add(livro);
    }

    public boolean removerLivros(String autor){
        for(Livro livro: this.livros){
            if(livro.getAutor().equals(autor)){
                this.livros.remove(livro);
                return true;
            }
        }
        return false;
    }

    public Livro buscarLivro(String autor){
        for(Livro livro: this.livros){
            if(livro.getAutor().equals(autor)){
                return livro;
            }
        }
        return null;
    }
    public int tamanhoDaLivraria(){
        return this.livros.size();
    }

    public ArrayList<Livro> mostrarLivros() {
        return this.livros;
    }
}
