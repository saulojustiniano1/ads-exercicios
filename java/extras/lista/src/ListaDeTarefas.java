import java.util.ArrayList;

public class ListaDeTarefas {
    private ArrayList<String> tarefas;

    public ListaDeTarefas() {
        tarefas = new ArrayList<>();
    }

    public void adicionarTarefa(String tarefa) {
        tarefas.add(tarefa);
    }

    public void removerTarefa(String tarefa) {
        tarefas.remove(tarefa);
    }

    public void listarTarefas() {
        System.out.println("Lista de Tarefas:");
        for (String tarefa : tarefas) {
            System.out.println(tarefa);
        }
    }
}