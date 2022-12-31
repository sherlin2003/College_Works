import java.util.Date;
import java.util.Locale;
import java.util.Scanner;
import java.util.Vector;

class Customer{
    private String name;
    private boolean member=false;
    private String memberType;

    public Customer(){}

    public Customer(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public String getMemberType() {
        return memberType;
    }

    public boolean isMember() {
        return member;
    }

    public void setMember(boolean member) {
        this.member = member;
    }

    public void setMemberType(String memberType) {
        this.memberType = memberType;
    }

    @Override
    public String toString(){
        return "Name: " + name + "\nMembership: " + member + " \nMember Type: " + memberType + "\n";
    }
}

class Visit{
    private Customer customer;
    private Date date;
    private double serviceExpense;
    private double productExpense;

    public Visit(){};

    public Visit(Customer c, Date date){
        this.customer = c;
        this.date = date;
    }

    public String getName(){
        return customer.getName();
    }

    public double getServiceExpense() {
        return serviceExpense;
    }

    public double getProductExpense() {
        return productExpense;
    }

    public double getTotalExpense(){
        return productExpense*(1 - DiscountRate.getProductDiscountRate(customer.getMemberType())) + serviceExpense*(1 - DiscountRate.getServiceDiscountRate(customer.getMemberType()));
    }

    public void setServiceExpense(double serviceExpense) {
        this.serviceExpense = serviceExpense;
    }

    public void setProductExpense(double productExpense) {
        this.productExpense = productExpense;
    }

    @Override
    public String toString(){
        return customer.toString() + "\nDate: " + date.toString() + "\nService Expense: " + serviceExpense + "\nProduct Expense: " + productExpense + "\nTotal Expense: " + this.getTotalExpense() + "\n";
    }
}

class DiscountRate{
    private static double serviceDiscountPremium = 0.2;
    private static double serviceDiscountGold = 0.15;
    private static double serviceDiscountSilver = 0.1;
    private static double productDiscountPremium = 0.1;
    private static double productDiscountGold = 0.1;
    private static double productDiscountSilver = 0.1;

    public static double getServiceDiscountRate(String type){
        if(type.equals("Premium")){
            return serviceDiscountPremium;
        } else if (type.equals("Gold")) {
            return serviceDiscountGold;
        } else if (type.equals("Silver")) {
            return serviceDiscountSilver;
        } else {
            return 0.0;
        }
    }
    public static double getProductDiscountRate(String type){
        if(type.equals("Premium")){
            return productDiscountPremium;
        } else if (type.equals("Gold")) {
            return productDiscountGold;
        } else if (type.equals("Silver")) {
            return productDiscountSilver;
        } else {
            return 0.0;
        }
    }
}
public class Main {
    static Vector<Visit> visits = new Vector<Visit>();
    static Vector<Customer> customers = new Vector<Customer>();

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        boolean on = true;
        while(on){
            System.out.print("1. Insert customer \n2. Insert visit \n3. View all visits \nother. Exit \nEnter choice: ");
            int choice = in.nextInt();
            switch (choice){
                case 1:
                    insertCustomer();
                    break;
                case 2:
                    in.nextLine();
                    System.out.print("Enter name: ");
                    String name = in.nextLine();
                    Customer c = null;
                    for(Customer cus : customers){
                        if(cus.getName().equals(name)){
                            c = cus;
                            break;
                        }
                    }
                    if(c==null){
                        System.out.println("No customer by the name " + name);
                    }
                    else{
                        insertVisit(c);
                    }
                    break;
                case 3:
                    for(Visit v : visits){
                        System.out.println(v.toString());
                    }
                    break;
                default:
                    on=false;
                    break;
            }
        }
    }
    public static void insertCustomer(){
        Scanner in = new Scanner(System.in);

        System.out.print("Customer name: ");
        String name = in.nextLine();

        System.out.print("Want membership? (yes or no): ");
        String choice = in.nextLine();

        Customer c= new Customer(name);
        if(choice.toLowerCase().equals("yes")){
            c.setMember(true);
            System.out.println("Types: \n1. Premium \n2. Gold \n3. Silver\nOther: Cancel membership\nChoose wisely");
            int type = in.nextInt();
            switch (type){
                case 1:
                    c.setMemberType("Premium");
                    break;
                case 2:
                    c.setMemberType("Gold");
                    break;
                case 3:
                    c.setMemberType("Silver");
                    break;
                default:
                    c.setMember(false);
            }
        }
        customers.add(c);
    }

    public static void insertVisit(Customer c){
        Visit v = new Visit(c, new Date());

        Scanner in = new Scanner(System.in);

        System.out.print("Enter service expenses: ");
        v.setServiceExpense(in.nextDouble());

        System.out.print("Enter product expenses: ");
        v.setProductExpense(in.nextDouble());

        visits.add(v);
    }
}
