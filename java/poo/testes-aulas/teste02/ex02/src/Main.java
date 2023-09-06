public class Main {
    public static void main(String[] args) {

        Encontro e1 = new Encontro();

        e1.setDia(18);
        e1.setMes(1);
        e1.setDescricao("Dia da Universidade");

        System.out.println("Dia: "+e1.getDia());
        System.out.println("Mês: "+e1.getMes());
        System.out.println("Descrição: "+e1.getDescricao());

    }
}