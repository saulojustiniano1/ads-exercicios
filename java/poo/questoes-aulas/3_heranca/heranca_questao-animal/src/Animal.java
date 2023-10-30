public class Animal {

    private String nome;
    private int idade;

    public Animal(String nome, int idade) {
        this.nome = nome;
        this.idade = idade;
    }

    public void emitir_som() {
        System.out.println("Som de animal");
    }

    public String getNome() {
        return nome;
    }

    public int getIdade() {
        return idade;
    }

}
