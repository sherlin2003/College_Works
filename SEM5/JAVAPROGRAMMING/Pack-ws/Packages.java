package MyPackage;

public class Packages {
    double weight;
    char shippingMethod;
    double shippingCost;

    static int[] weightRange;
    static char[] modes;
    static double[][] cost;

    public Packages() {}

    public Packages(double w, char sm) {
        weight = w;
        shippingMethod = sm;
        shippingCost = calculateCost(w, sm);
    }

    double calculateCost(double w, char sm) {
        int i, j;
        if(w >= weightRange[0] && w <= weightRange[1]-1)
            i = 0;
        else if (w >= weightRange[1] && w <= weightRange[2]-1)
            i = 1;
        else
            i = 2;

        if(sm == modes[0])
            j = 0;
        else if(sm == modes[1])
            j = 1;
        else
            j = 2;

        return cost[i][j];
    }

    public void display() {
        System.out.print("Weight (oz.)\tAir ($)\tTruck ($)\tAil ($)");
        for(int i=0; i<weightRange.length; i++) {
            if(i!=weightRange.length-1) {
                int end = weightRange[i+1]-1;
                System.out.print("\n"+weightRange[i] + " to " +end);
            }
            else
                System.out.print("\n"+weightRange[i]+" +");

            for(int j=0; j<modes.length; j++){
                System.out.print("\t\t\t"+cost[i][j]);
            }
        }
    }

    public double getShippingCost() {
        return shippingCost;
    }

    static {
        weightRange = new int[]{1, 9, 17};
        modes = new char[]{'A', 'T', 'M'};
        cost = new double[][]{{2.00, 1.50, 0.50}, {3.00, 2.35, 1.50}, {4.50, 3.25, 2.15}};
    }
}

