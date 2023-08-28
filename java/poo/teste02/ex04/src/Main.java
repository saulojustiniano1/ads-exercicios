public class Main {
    public static void main(String[] args) {

        Encontro e1 = new Encontro();
        Encontro e2 = new Encontro();
        Agenda a1 = new Agenda();

        e1.setDia(10);
        e1.setMes(8);
        e1.setDescricao("Dia da universidade!");

        e2.setDia(3);
        e2.setMes(10);
        e2.setDescricao("Dia da programador!");

        int dia = e1.getDia();
        int mes = e1.getMes();

        boolean validar = e1.validarData(dia, mes);

        if(validar){
            System.out.println("Dia: "+e1.getDia());
            System.out.println("Mês: "+e1.getMes());
            System.out.println("Descrição: "+e1.getDescricao());
        } else{
            System.out.println("Data Inválida!");
        }

        a1.addEncontro(e1);
        a1.addEncontro(e2);

        a1.exibir();

    }
}