public class Pokemon {
    private String nome;
    private String tipo;
    private int nivel;

    public Pokemon(String nome, String tipo, int nivel) {
        this.nome = nome;
        this.tipo = tipo;
        this.nivel = nivel;
    }

    public String getNome() {
        return nome;
    }

    public String getTipo() {
        return tipo;
    }

    public int getNivel() {
        return nivel;
    }

    @Override // Sobrescreve o método toString() da classe Object
    public String toString() { // Retorna uma String com os atributos do objeto
        return "=========== Pokemon =============" + "\n"
                + "nome: " + nome + "\n"
                + "tipo: " + tipo + "\n"
                + "nivel: " + nivel;
    }
}
