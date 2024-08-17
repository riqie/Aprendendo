package edu.rique.AnatomiaClasses;

// arquivo de exemplo para identação;
// perceba que a identação facilita a visualização do programa, e para programas mais complexos, a identação é essencial.

public class Aula_4_Identacao {

// ========= Sem identação:

    // public static void main(String[] args) {

    //     int mediaFinal = 7;

    //     if (mediaFinal<6)
    //     System.out.println("Reprovado.");

    //     else if (mediaFinal == 6)
    //     System.out.println("Prova Minerva.");

    //     else
    //     System.out.println("Aprovado!");

    // }

// ========= Com identação:
    public static void main(String[] args) {
        int mediaFinal = 5;

        if (mediaFinal<6)
            System.out.println("Reprovado.");

        else if (mediaFinal == 6)
            System.out.println("Prova Minerva.");

        else
            System.out.println("Aprovado!");
    }

}
