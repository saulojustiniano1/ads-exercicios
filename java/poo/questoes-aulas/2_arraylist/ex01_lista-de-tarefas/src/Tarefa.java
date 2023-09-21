public class Tarefa {
    private String tarefa;
    private String referencia;

    public Tarefa(String tarefa, String referencia){
        this.tarefa = tarefa;
        this.referencia = referencia;
    }

    public String getTarefa() {
        return tarefa;
    }

    public String getReferencia() {
        return referencia;
    }
}
