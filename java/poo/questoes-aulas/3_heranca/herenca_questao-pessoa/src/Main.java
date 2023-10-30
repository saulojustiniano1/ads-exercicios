public class Main {
    public static void main(String[] args) {

        Cliente cliente = new Cliente("Jonatan", 27, 1,"Rua A, 123");
        Funcionario funcionario = new Funcionario("Saulo", 23, 1, "Analista de sistemas");
        Cadastro cadastro = new Cadastro();


        cadastro.setPessoa(funcionario); // Polimorfismo
        cadastro.setPessoa(cliente); // Polimorfismo
        cadastro.getPessoa().setNome("Joao"); // Polimorfismo

        System.out.println("Nome: "+cadastro.getPessoa().getNome());

//        System.out.println("============== DADOS PESSOAIS ==================");
//        System.out.println("Cliente: "+cliente.getNome());
//        System.out.println("Idade: "+cliente.getIdade());
//        System.out.println("ID: "+cliente.getIdCliente());
//        System.out.println("Endereço: "+cliente.getEndereco());
//
//        System.out.println(" ");
//
//        System.out.println("==================== FUNCIONÁRIO =================");
//        System.out.println("Funcionário: "+funcionario.getNome());
//        System.out.println("Idade: "+funcionario.getIdade());
//        System.out.println("ID: "+funcionario.getIdFuncionario());
//        System.out.println("Cargo: "+funcionario.getCargo());




    }
}