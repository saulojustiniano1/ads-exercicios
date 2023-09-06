public class Livro {
    private String nome;
    private String autor;
    private int ano;
    private double preco;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    public void exibir() {
        System.out.println("Nome: "+getNome());
        System.out.println("Autor: "+getAutor());
        System.out.println("Ano: "+getAno());
        System.out.println("Preço: R$"+getPreco());
    }
}
