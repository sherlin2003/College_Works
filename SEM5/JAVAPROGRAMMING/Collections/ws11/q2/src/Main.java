import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.Scanner;

class Stall{
    private String name, detail, type, ownerName;

    public Stall(){

    }

    public Stall(String name, String detail, String type, String ownerName) {
        this.name = name;
        this.detail = detail;
        this.type = type;
        this.ownerName = ownerName;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDetail() {
        return detail;
    }

    public void setDetail(String detail) {
        this.detail = detail;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getOwnerName() {
        return ownerName;
    }

    public void setOwnerName(String ownerName) {
        this.ownerName = ownerName;
    }

    @Override
    public String toString() {
        return String.format("%-15s %-20s %-15s %s", name, detail, type, ownerName);
    }
}
public class Main {
    public static void main(String[] args) {
        Scanner in  = new Scanner(System.in);
        List<Stall> stallDetails = new ArrayList<Stall>();
        System.out.println("Enter the number of stall details");
        int n = in.nextInt();
        in.nextLine();
        for(int i=0; i<n; i++){
            System.out.printf("Enter the stall %d detail\n", i+1);
            String[] details = in.nextLine().split(",");
            stallDetails.add(new Stall(details[0], details[1], details[2], details[3]));
        }

        Iterator<Stall> iterator= stallDetails.iterator();
        while(iterator.hasNext()){
            Stall s = iterator.next();
            if(s.getName().startsWith("test")){
                iterator.remove();
            }
        }

        System.out.println(String.format("%-15s %-20s %-15s %s", "Name", "Detail", "Type", "Owner Name"));
        for(Stall s: stallDetails){
            System.out.println(s.toString());
        }
    }
}
