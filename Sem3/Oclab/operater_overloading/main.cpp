#include <iostream>
using namespace std;
#include <iostream>
#include <iomanip>
#include "PersonData.h"
#include "CustomerData.h"
#include "PreferredCustomer.h"
using namespace std;
int main()
{
    PreferredCustomer customer1;
    cout << "\nLast Name: " << customer1.getLastName();
    cout << "\nFirst Name: " << customer1.getFirstName();
    cout << "\nAddress: " << customer1.getAddress();
    cout << "\nCity: " << customer1.getCity();
    cout << "\nState: " << customer1.getState();
    cout << "\nZIP Code: " << customer1.getZIP();
    cout << "\nPhone Number: " << customer1.getPhoneNumber();
    cout << "\nCustomer Number: " << customer1.getCustomerNumber();
    customer1.setLastName("SWETHA");
    customer1.setFirstName("SHERLIN");
    customer1.setAddress("NO18,CHERAN GARDEN,BALAGI NAGAR");
    customer1.setCity("COIMBATORE");
    customer1.setState("TAMIL NADU");
    customer1.setZIP("641048");
    customer1.setPhoneNumber("9994287171");
    customer1.setCustomerNumber(3572);
    customer1.setMailingList(true);
    customer1.setPurchasesAmount(10000000);
    cout << "\nLast Name: " << customer1.getLastName();
    cout << "\nFirst Name: " << customer1.getFirstName();
    cout << "\nAddress: " << customer1.getAddress();
    cout << "\nCity: " << customer1.getCity();
    cout << "\nState: " << customer1.getState();
    cout << "\nZIP Code: " << customer1.getZIP();
    cout << "\nPhone Number: " << customer1.getPhoneNumber();
    cout << "\nCustomer Number: " << customer1.getCustomerNumber();
}
