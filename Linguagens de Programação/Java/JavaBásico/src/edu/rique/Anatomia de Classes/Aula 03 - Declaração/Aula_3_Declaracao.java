package edu.rique.Anatomia de Classes;
public class Aula_3_Declaracao {

public static void main(String[] args) {
        
    // declarar uma variável em Java sempre seguirá esta estrutura:
    // <tipo> <nome da variável> = <valor>

    String primeiroNome = "Henrique";
    String segundoNome = "Carvalho";

    String nomeCompleto = nomeCompleto(primeiroNome, segundoNome);

    System.out.println(nomeCompleto);

    // declarar um método, uma função ao meu código:
    // é comum que o nome dos métodos sejam escritos no infinitivo. 
}

public static String nomeCompleto (String primeiroNome, String segundoNome) {
    return "Resultado do método: " + primeiroNome.concat(" ").concat(segundoNome);


}
    






}


