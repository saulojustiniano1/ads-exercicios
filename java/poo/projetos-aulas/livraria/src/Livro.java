public class Livro {
    private String titulo;
    private String autor;

    public Livro(String titulo, String autor){
        this.titulo = titulo;
        this.autor = autor;
    }

    public Livro(){}

    public String getTitulo() {
        return titulo;
    }

    public String getAutor() {
        return autor;
    }
}
