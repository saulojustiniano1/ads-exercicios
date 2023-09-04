public class Agenda {
    String nome;
    String telefone;

    public Agenda(String nome, String telefone){
        this.nome = nome;
        this.telefone = telefone;
    }

    public void exibir(){
        System.out.println("Nome: "+this.nome);
        System.out.println("Telefone: "+this.telefone);
    }
}