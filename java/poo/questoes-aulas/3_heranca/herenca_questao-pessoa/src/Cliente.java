public class Cliente extends Pessoa {

    private int idCliente;
    private String endereco;

    public Cliente(String nome, int idade, int idCliente, String endereco) {
        super(nome, idade);
        this.idCliente = idCliente;
        this.endereco = endereco;
    }

    public int getIdCliente() {
        return idCliente;
    }

    public void setIdCliente(int idCliente) {
        this.idCliente = idCliente;
    }

    public String getEndereco() {
        return endereco;
    }

    public void setEndereco(String endereco) {
        this.endereco = endereco;
    }
}
