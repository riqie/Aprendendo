package edu.rique.Operadores;

public class operadores2 {
    public static void main(String[] args) {
        String concatenacao = "?";

        concatenacao = 1+1+1+"1";
        System.out.println(concatenacao);
        
        concatenacao = 1+"1"+1+1;
        System.out.println(concatenacao);
        
        concatenacao= 1+"1"+1+"1";
        System.out.println(concatenacao);
        
        concatenacao = "1"+1+1+1;
        System.out.println(concatenacao);
        
        concatenacao= "1"+(1+1+1);
        System.out.println(concatenacao);
        
        // perceba que a partir do momento que ele entende um texto, ele começa a concatenar, ele para de realizar as operações aritméticas.
    }
}
