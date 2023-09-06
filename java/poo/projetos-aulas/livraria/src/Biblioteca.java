import java.util.ArrayList;

public class Biblioteca {

    ArrayList<Livro> livros = new ArrayList<>();

    public void adicionarLivro(Livro livro){
        this.livros.add(livro);
    }

    public ArrayList<Livro> mostrarLivros() {
        return livros;
    }

    public int tamanhoDaLivraria(){
        return livros.size();
    }

    public Livro buscarLivro(String autor){
        for(Livro l: livros){
            if(l.getAutor().equals(autor)){
                return l;
            }
        }
        return null;
    }

    public boolean removerLivros(String autor){
        for(Livro l: livros){
            if(l.getAutor().equals(autor)){
                livros.remove(l);
                return true;
            }
        }
        return false;
    }
}
