public class Personagem {
    private String nome;
    private Kart motortista;
    private int moedas = 0;
    private int posicao = 10;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public Kart getMotortista() {
        return motortista;
    }

    public void setMotortista(Kart motortista) {
        this.motortista = motortista;
    }

    public int getMoedas() {
        return moedas;
    }

    public int getPosicao() {
        return posicao;
    }

    public void pegarMoedas() {
        moedas++;
    }

    public void perderMoeda(){
        if(moedas != 0){
            moedas--;
        }
    }

    public void perderPosicao(){
        posicao++;
    }

    public void ultrapassa(){
        if(posicao != 1){
            posicao--;
        }
    }
}
