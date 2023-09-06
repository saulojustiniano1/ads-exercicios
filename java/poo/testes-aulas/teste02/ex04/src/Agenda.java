import java.util.*;

public class Agenda {
    Vector<Encontro> encontros = new Vector<>(); // um vetor do tipo encontro que só entra objeto do tipo encontro

    public void exibir(){
        for(Encontro listaEncontro: encontros){ // foreach
            System.out.println("Encontro dia: "+listaEncontro.getDia()+"\nEncontro mês: "+listaEncontro.getMes()+"\nEncontro descrição: "+listaEncontro.getDescricao());
            System.out.println();
        }
    }

    public void addEncontro(Encontro e) {
        encontros.add(e);
    }
}
