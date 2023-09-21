public class Main {
    public static void main(String[] args) {
            ListaDeTarefas lista = new ListaDeTarefas();

            lista.adicionarTarefa("Fazer compras");
            lista.adicionarTarefa("Estudar para a prova");
            lista.adicionarTarefa("Lavar o carro");

            System.out.println("Tarefas adicionadas:");
            lista.listarTarefas();

            lista.removerTarefa("Fazer compras");

            System.out.println("\nTarefa removida:");
            lista.listarTarefas();
    }
}