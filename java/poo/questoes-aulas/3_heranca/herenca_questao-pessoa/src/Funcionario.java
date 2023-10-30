public class Funcionario extends Pessoa {

    private int idFuncionario;
    private String cargo;

    public Funcionario(String nome, int idade, int idFuncionario, String cargo) {
        super(nome, idade);
        this.idFuncionario = idFuncionario;
        this.cargo = cargo;
    }

    public int getIdFuncionario() {
        return idFuncionario;
    }

    public void setIdFuncionario(int idFuncionario) {
        this.idFuncionario = idFuncionario;
    }

    public String getCargo() {
        return cargo;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }
}
