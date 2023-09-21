import javax.swing.*;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) throws UnsupportedLookAndFeelException, ClassNotFoundException, InstantiationException, IllegalAccessException {

        Biblioteca livraria = new Biblioteca();
        ArrayList<Livro> arrayLivros = new ArrayList<>();
        boolean b = true;
        Object[] newop = {"cadastrar", "visualizar livros", "quantos de livros na livraria", "escolher livro pelo autor", "remover livro pelo autor", "sair do programa"};
        Object[] objetoQuantidade = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"};

//        UIManager.setLookAndFeel("com.sun.java.swing.plaf.gtk.GTKLookAndFeel"); GTK GNOME
//        UIManager.setLookAndFeel("com.sun.java.swing.plaf.windows.WindowsLookAndFeel"); WINDOWS
        UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());

        while(b){
            String op;
            Object menu = JOptionPane.showInputDialog(null, "Escolha uma opção", "Livraria", JOptionPane.PLAIN_MESSAGE, null, newop, newop[0]);

            try {
                op = menu.toString();
                switch (op) {
                    case "cadastrar" -> {
                        Object quantidadeDeLivros = JOptionPane.showInputDialog(null, "Informe quantos livros deseja cadastrar", null, JOptionPane.PLAIN_MESSAGE, null, objetoQuantidade, objetoQuantidade[0]);

                        String newQntDeLivros = quantidadeDeLivros.toString();

                        int qntDeLivros = Integer.parseInt(newQntDeLivros);

                        for (int i = 0; i < qntDeLivros; i++) {
                            Object nomeDoLivro = JOptionPane.showInputDialog(null, "Nome do livro: ");
                            String inputLivro = nomeDoLivro.toString();

                            Object autorDoLivro = JOptionPane.showInputDialog(null, "Autor do livro: ");
                            String inputAutorDoLivro = autorDoLivro.toString();

                            Livro livros = new Livro(inputLivro, inputAutorDoLivro);
                            livraria.adicionarLivro(livros);
                        }
                        JOptionPane.showMessageDialog(null, "Cadastro realizado com sucesso!" ,null, JOptionPane.PLAIN_MESSAGE);
                        arrayLivros = livraria.mostrarLivros();
                    }
                    case "visualizar livros" -> {
                        StringBuilder listaDeLivros = new StringBuilder();

                        for (Livro l : arrayLivros) {
                            String news;
                            news = ("\n Nome: " + l.getTitulo());
                            listaDeLivros.append(news);
                            news = ("\n Autor: " + l.getAutor()+"\n ---------------");
                            listaDeLivros.append(news);
                        }

                        JOptionPane.showMessageDialog(null, listaDeLivros.toString());
                    }
                    case "quantos de livros na livraria" -> {
                        JOptionPane.showMessageDialog(null, "Na livraria tem "+livraria.tamanhoDaLivraria()+" Livros");
                    }
                    case "escolher livro pelo autor"-> {

                        Object inputAutor = JOptionPane.showInputDialog(null, "Informe o nome do autor: ");

                        Livro livroAutor = livraria.buscarLivro(inputAutor.toString());

                        if (livroAutor != null) {
                            JOptionPane.showMessageDialog(null, "Nome: " + livroAutor.getTitulo()+"\nAutor: " + livroAutor.getAutor());
                        } else {
                            JOptionPane.showMessageDialog(null, "Livro não encontrado!");
                        }
                    }
                    case "remover livro pelo autor" -> {
                        Object inputRemoverAutor = JOptionPane.showInputDialog(null, "Digite o autor para ser removido: ");


                        if(livraria.removerLivros(inputRemoverAutor.toString())){
                            JOptionPane.showMessageDialog(null, "Livro removido com sucesso!");
                        } else {
                            JOptionPane.showMessageDialog(null, "Livro NÃO encontrado!");
                        }

                    }
                    case "sair do programa" -> {
                        JOptionPane.showMessageDialog(null, "Volte sempre!");
                        b = false;
                    }
                }
            } catch (NullPointerException e){
                JOptionPane.showMessageDialog(null, "Programa finalizado!");
                b = false;
            }
        }
    }
}