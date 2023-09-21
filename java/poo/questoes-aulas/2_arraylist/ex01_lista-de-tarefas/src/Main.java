import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);
        ListaDeTarefas listaTarefas = new ListaDeTarefas();
        ArrayList<Tarefa> arrayListaDeTarefa = new ArrayList<>();

        boolean parar = true;

        while(parar) {
            System.out.println("Digite [1] para adicionar uma tarefa");
            System.out.println("Digite [2] para visualizar as tarefas");
            System.out.println("Digite [3] para remover uma tarefa");
            System.out.println("Digite [4] para sair");
            int opcao = input.nextInt();

            switch(opcao){
                case 1 -> {
                    input.nextLine();
                    System.out.println("Número da tarefa: ");
                    String inputReferenciaTarefa = input.nextLine();

                    System.out.println("Digite sua tarefa: ");
                    String inputTarefa = input.nextLine();

                    Tarefa tarefa = new Tarefa(inputTarefa, inputReferenciaTarefa);
                    listaTarefas.adicionarTarefas(tarefa);

                    arrayListaDeTarefa = listaTarefas.listarTarefas();
                }
                case 2 -> {
                    for(Tarefa t: arrayListaDeTarefa){
                        System.out.println("Nº de referencia: "+t.getReferencia());
                        System.out.println("Tarefa: "+t.getTarefa());
                        System.out.println("_______________________");
                    }
                }
                case 3 -> {
                    input.nextLine();
                    System.out.println("Informe a referencia da tarefa: ");
                    String removerTarefa = input.nextLine();

                    if(listaTarefas.removerTarefas(removerTarefa)){
                        System.out.println("Tarefa removida!");
                    } else {
                        System.out.println("Tarefa já removida!");
                    }
                }
                case 4 -> {
                    System.out.println("Tarefas colocadas com sucesso!");
                    parar = false;
                }
            }
        }


    }
}