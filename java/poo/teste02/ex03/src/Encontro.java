public class Encontro {
    final int DIA_INICIAL = 1; // "final" é uma constante
    final int DIA_FINAL = 31;
    final int MES_INICIAL = 1;
    final int MES_FINAL = 12;

    private int dia, mes;
    private String descricao;

    public int getDia() {
        return dia;
    }

    public void setDia(int dia) {
        this.dia = dia;
    }

    public int getMes() {
        return mes;
    }

    public void setMes(int mes) {
        this.mes = mes;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public boolean validarData(int dia, int mes){
        if((dia >= DIA_INICIAL && dia <= DIA_FINAL) && (mes >= MES_INICIAL && mes <= MES_FINAL)){
            return true;
        } else {
            return false;
        }

    }
}
