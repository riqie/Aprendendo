public class TiposVariaveis {
    public static void main(String[] args) throws Exception {
        double salarioMinimo = 2500;

        short numeroCurto = 1;
        int numeroNormal = numeroCurto;
        //short numeroCurto = numeroNormal;  --> Erro!
        short numeroCurto2 = (short) numeroNormal; // Casting!

        int numero = 1;

        numero = 2;
        
        final double VALOR_DE_PI = 3.14;
        // esta constante não pode ser alterada ao longo do código
        System.out.println(salarioMinimo);
        System.out.println(numeroCurto);
        System.out.println(numeroNormal);
        System.out.println(numeroCurto2);
        System.out.println(numero);
        System.out.println(VALOR_DE_PI);
    }
}
