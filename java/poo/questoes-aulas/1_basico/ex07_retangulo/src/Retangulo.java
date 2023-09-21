public class Retangulo {
    private int comprimento;
    private int largura;

    public int getComprimento() {
        return comprimento;
    }

    public void setComprimento(int comprimento) {
        this.comprimento = comprimento;
    }

    public int getLargura() {
        return largura;
    }

    public void setLargura(int largura) {
        this.largura = largura;
    }

    public int areaDoRetangulo(){
        final int comprimento = getComprimento();
        final int largura = getLargura();

        return comprimento * largura;
    }

    public int perimetroDoRetangulo(){
        final int comprimento = getComprimento();
        final int largura = getLargura();

        return 2*(comprimento+largura);
    }
}
