import MyPackage.*;
import InsuredPackage.*;

public class Main {
    public static void main(String[] args) {

        Packages P = new Packages(2.7, 'A');
        P.display();
        System.out.println("\n\nShipping Cost: "+P.getShippingCost());

        InsuredPackage I = new InsuredPackage(18, 'M');
        System.out.println("\n\nShipping Cost: "+I.getShippingCost());
        System.out.println("Insurance Cost: "+I.getInsuranceCost());
    }
}