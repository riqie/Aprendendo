package edu.rique.Operadores;

public class operadoresUnarios {
    public static void main(String[] args) {
        int numero = 5;

        System.out.println(- numero);
        System.out.println(numero);
        System.out.println(numero --);
        System.out.println(numero ++);
        System.out.println(-- numero);
        System.out.println(++ numero );
        
        boolean variavel = true;

        System.out.println(!variavel);
        System.out.println(variavel);
        variavel = !variavel;
        
        System.out.println(variavel);
    }
}
