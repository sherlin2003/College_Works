import java.util.*;
import java.lang.*;

class Hall implements Comparable<Hall>
{
    String name;
    String contactNumber;
    double costPerDay;
    String ownerName;

    public Hall(String name, String contactNumber, double costPerDay, String ownerName) {
        this.name = name;
        this.contactNumber = contactNumber;
        this.costPerDay = costPerDay;
        this.ownerName = ownerName;
    }

    public String getName() {
        return name;
    }

    public String getContactNumber() {
        return contactNumber;
    }

    public double getCostPerDay() {
        return costPerDay;
    }

    public String getOwnerName() {
        return ownerName;
    }

    @Override
    public int compareTo(Hall H) {
        if(this.costPerDay - H.costPerDay > 0.0)
            return 1;
        else if(this.costPerDay - H.costPerDay < 0.0)
            return -1;
        else
            return 0;
    }
}

public class Main {
    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        System.out.println("Enter the number of halls:");
        int num = scan.nextInt();
        scan.nextLine();

        List<Hall> LH = new ArrayList<Hall>();

        for(int i=1; i<=num; i++) {
            System.out.println("Enter the details of hall "+i);
            String details = scan.nextLine();
            String arr[] = details.split(",");
            LH.add(new Hall(arr[0], arr[1], Double.parseDouble(arr[2]), arr[3]));
        }

        Collections.sort(LH);

        System.out.println("Sorted Order (from the least expensive to the most):");

        System.out.printf("%-15s%-15s%-15s%-15s", "Name", "Contact Number", "Cost per day", "Owner Name");
        for(Hall H: LH) {
            System.out.printf("\n%-15s%-15s%-15s%-15s", H.getName(), H.getContactNumber(), H.getCostPerDay(), H.getOwnerName());
        }
    }
}