public class Usuario {
    public static void main(String[] args) throws Exception {
        
        SmartTv smartTv = new SmartTv();

        System.out.println("\nTv ligada? "+ smartTv.ligada);

        System.out.println("\nCanal atual: " +smartTv.canal);

        System.out.println("\nVolume da Tv: " + smartTv.volume);
        
        smartTv.ligar();
        System.out.println("\nTv ligada? "+ smartTv.ligada);
        
        smartTv.desligar();
        System.out.println("\nTv ligada? "+ smartTv.ligada);
        
        smartTv.aumentarVolume();
        smartTv.aumentarVolume();
        smartTv.aumentarVolume();
        System.out.println("\nVolume da Tv: " + smartTv.volume);
        
        smartTv.diminuirVolume();
        smartTv.diminuirVolume();
        System.out.println("\nVolume da Tv: " + smartTv.volume);
        
        System.out.println("\nCanal Atual: "+ smartTv.canal);
        
        smartTv.mudarCanal(21);
        
        System.out.println("\nCanal Atual: "+ smartTv.canal);

        System.out.println();
    }
}
