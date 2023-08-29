public class Kart {
    private String cor;
    private Personagem personagem;
    private int vidaKart = 100;

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public Personagem getPersonagem() {
        return personagem;
    }

    public void setPersonagem(Personagem personagem) {
        this.personagem = personagem;
    }

    public int getVidaKart() {
        return vidaKart;
    }

    public void bateKart(){
        vidaKart = vidaKart - 10;
        personagem.perderMoeda();
    }

    public void freaKart(){
        personagem.perderPosicao();
    }
}
