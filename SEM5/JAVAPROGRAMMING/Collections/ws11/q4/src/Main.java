import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

class Address implements Comparable<Address>{
    private String username, addressLine1, addressLine2;
    private Integer pinCode;

    public Address(){

    }
    public Address(String username, String addressLine1, String addressLine2, Integer pinCode) {
        this.username = username;
        this.addressLine1 = addressLine1;
        this.addressLine2 = addressLine2;
        this.pinCode = pinCode;
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getAddressLine1() {
        return addressLine1;
    }

    public void setAddressLine1(String addressLine1) {
        this.addressLine1 = addressLine1;
    }

    public String getAddressLine2() {
        return addressLine2;
    }

    public void setAddressLine2(String addressLine2) {
        this.addressLine2 = addressLine2;
    }

    public Integer getPinCode() {
        return pinCode;
    }

    public void setPinCode(Integer pinCode) {
        this.pinCode = pinCode;
    }

    @Override
    public String toString() {
        return "Address{" +
                "username='" + username + '\'' +
                ", addressLine1='" + addressLine1 + '\'' +
                ", addressLine2='" + addressLine2 + '\'' +
                ", pinCode=" + pinCode +
                '}';
    }

    @Override
    public int compareTo(Address o) {
        if(pinCode == o.pinCode){
            return o.addressLine1.compareTo(addressLine1);
        }
        else{
            return Integer.compare(pinCode, o.pinCode);
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner in  = new Scanner(System.in);
        List<Address> addressDetails = new ArrayList<Address>();
        System.out.println("Enter the number of address details");
        int n = in.nextInt();
        in.nextLine();
        for(int i=0; i<n; i++){
            String[] details = in.nextLine().split(",");
            addressDetails.add(new Address(details[0], details[1], details[2], Integer.parseInt(details[3])));
        }

        Collections.sort(addressDetails);
        System.out.println("Sorted Order");
        for(int i=0; i<addressDetails.size(); i++){
            System.out.println(addressDetails.get(i).toString());
        }
    }
}
