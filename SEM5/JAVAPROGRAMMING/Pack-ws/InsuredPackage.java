package InsuredPackage;
import MyPackage.*;

public class InsuredPackage extends Packages {

    double insuranceCost;

    static double additionalCost[] = {2.45, 3.95, 5.55};
    static double insuranceRange[] = {0, 1.01, 3.01};

    public InsuredPackage() {}

    public InsuredPackage(double w, char sm) {
        super(w, sm);
        insuranceCost = calcInsuranceCost();
    }

    double calcInsuranceCost() {
        int index;
        if(this.getShippingCost() >= insuranceRange[0] && this.getShippingCost() <= insuranceRange[1]-0.01)
            index = 0;
        else if(this.getShippingCost() >= insuranceRange[1] && this.getShippingCost() <= insuranceRange[2]-0.01)
            index = 1;
        else
            index = 2;
        return additionalCost[index];
    }

    public double getInsuranceCost() {
        return insuranceCost;
    }
}
