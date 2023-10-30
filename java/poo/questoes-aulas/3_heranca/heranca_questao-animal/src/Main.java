public class Main {

    public static void main(String[] args) {

        Cachorro cachorro = new Cachorro("Teo", 2);
        Gato gato = new Gato("Leo", 3);

        System.out.println("Nome do cachorro: "+cachorro.getNome()+"\n"+"Idade: "+cachorro.getIdade());
        System.out.println("Nome do gato: "+gato.getNome()+"\n"+"Idade: "+gato.getIdade());



        System.out.println("-----------------------------------");
        cachorro.emitir_som();
        cachorro.latir();
        System.out.println("-----------------------------------");
        gato.emitir_som();
        gato.miar();
    }
}