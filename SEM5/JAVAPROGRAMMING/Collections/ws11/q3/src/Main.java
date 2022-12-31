import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

class Hall implements Comparable<Hall>{
    private String name, contactnumber, ownerName;
    private Double costPerDay;
    public Hall() {
    }

    public Hall(String name, String contactnumber, Double costPerDay, String ownerName) {
        this.name = name;
        this.contactnumber = contactnumber;
        this.costPerDay = costPerDay;
        this.ownerName = ownerName;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getContactnumber() {
        return contactnumber;
    }

    public void setContactnumber(String contactnumber) {
        this.contactnumber = contactnumber;
    }

    public Double getCostPerDay() {
        return costPerDay;
    }

    public void setCostPerDay(Double costPerDay) {
        this.costPerDay = costPerDay;
    }

    public String getOwnerName() {
        return ownerName;
    }

    public void setOwnerName(String ownerName) {
        this.ownerName = ownerName;
    }
    @Override
    public String toString() {
        return String.format("%-15s %-15s %-15s %-15s", name, contactnumber, costPerDay, ownerName);
    }

    @Override
    public int compareTo(Hall o) {
        return Double.compare(costPerDay, o.costPerDay);
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner in  = new Scanner(System.in);
        List<Hall> hallDetails = new ArrayList<Hall>();
        System.out.println("Enter the number of hall details");
        int n = in.nextInt();
        in.nextLine();
        for(int i=0; i<n; i++){
            System.out.printf("Enter the hall %d detail\n", i+1);
            String[] details = in.nextLine().split(",");
            hallDetails.add(new Hall(details[0], details[1], Double.parseDouble(details[2]), details[3]));
        }

        Collections.sort(hallDetails);
        System.out.println("Sorted Order");
        System.out.println(String.format("%-15s %-15s %-15s %-15s", "Name", "Contactnumber", "CostPerDay", "OwnerName"));
        for(int i=0; i<hallDetails.size(); i++){
            System.out.println(hallDetails.get(i).toString());
        }
    }
}
