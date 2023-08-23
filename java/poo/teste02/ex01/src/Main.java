public class Main {
    public static void main(String[] args) {
        Encontro e1 = new Encontro();

        e1.dia = 18;
        e1.mes = 1;
        e1.descricao = "Dia da Universidade";

        System.out.println("Dia: "+e1.dia);
        System.out.println("Mês: "+e1.mes);
        System.out.println("Descrição: "+e1.descricao);
    }
}