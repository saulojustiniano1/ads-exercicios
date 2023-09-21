public class Circulo {
    final double PI = 3.14;

    private double raio;

    public Circulo(double raio){
        this.raio = raio;
    }

    public double getRaio() {
        return raio;
    }

    public void setRaio(double raio) {
        this.raio = raio;
    }

    public double calcularArea(){
        return PI * Math.pow(this.raio, 2);
    }

    public double calcularPerimetro(){
        return 2 * PI * this.raio;
    }

    public void exibirResultado(){
        System.out.println("Área do círculo: "+this.calcularArea()+"cm2");
        System.out.println("Perímetro do círculo: "+this.calcularPerimetro()+"cm2");
    }
}
