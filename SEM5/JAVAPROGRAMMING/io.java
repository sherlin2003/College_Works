import java.io.*;
import java.util.*;

class Employee
{
    private String empno;
    private String ename;
    private String address;

    public Employee() {}

    public Employee(String empno, String ename, String address) {
        this.empno = empno;
        this.ename = ename;
        this.address = address;
    }

    public void setEmpno(String empno) {
        this.empno = empno;
    }

    public void setEname(String ename) {
        this.ename = ename;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    @Override
    public String toString() {
        return "Emp No: "+empno+"\nEmp Name: "+ename+"\nAddress: "+address;
    }
}

class EmployeeWriter implements Serializable
{
    public void write(String fileName) {
        try {

            FileOutputStream fos = new FileOutputStream(fileName);

            ObjectOutputStream oos = new ObjectOutputStream(fos);

            Employee E = new Employee("E1001", "Anonymous", "10A, Nehru Street, Trichy, Tamil Nadu");

            oos.writeObject(E);

        }
        catch(IOException ex) {
            System.out.println("write");
            ex.printStackTrace();
        }
    }
}

class EmployeeReader
{
    public Employee read(String fileName) {

        Employee E = new Employee();

        try {

            FileInputStream fis = new FileInputStream(fileName);

            ObjectInputStream ois = new ObjectInputStream(fis);

            try {
                E = (Employee) ois.readObject();
            }
            catch (Exception e) {
                System.out.println(e);
            }

        }
        catch(IOException ex) {
            ex.printStackTrace();
        }

        return E;
    }
}

public class Main {
    public static void main(String[] args) {

        EmployeeWriter EW = new EmployeeWriter();

        EmployeeReader ER = new EmployeeReader();

        EW.write("file.txt");
        Employee E = ER.read("file.txt");
        System.out.println(E.toString());
    }
}