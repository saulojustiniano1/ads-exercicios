import java.util.ArrayList;

public class ListaDeTarefas {

    ArrayList<Tarefa> tarefas = new ArrayList<>();

    public void adicionarTarefas(Tarefa tarefas) {
        this.tarefas.add(tarefas);
    }

    public boolean removerTarefas(String referencia){
        for(Tarefa t: this.tarefas){
            if(t.getReferencia().equals(referencia)){
                this.tarefas.remove(referencia);
                return true;
            }
        }
        return false;
    }

    public ArrayList<Tarefa> listarTarefas() {
        return this.tarefas;
    }
}
