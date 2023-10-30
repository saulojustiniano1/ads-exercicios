public class Carro extends Veiculo{

    private int ano;

    public Carro(String marca, String modelo, int ano) {
        super(marca, modelo);
        this.ano = ano;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public void exibir(String marca, String modelo, int ano) {
        System.out.println("Marca: " + marca);
        System.out.println("Modelo: " + modelo);
        System.out.println("Ano: " + ano);
    }
}
