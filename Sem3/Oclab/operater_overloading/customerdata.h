#ifndef CUSTOMERDATA_H_INCLUDED
#define CUSTOMERDATA_H_INCLUDED

#include <iostream>
#include <string>
#include "PersonData.h"
using namespace std;
class CustomerData:public PersonData
{
private:
    int customerNumber;
    bool mailingList;
public:
    void setCustomerNumber(int cno);
    void setMailingList(bool ans);
    int getCustomerNumber();
    bool getMailingList();
CustomerData();
CustomerData(int cno, bool ans, string lname, string fname, string a, string s, string c, string z, string ph);
};


#endif // CUSTOMERDATA_H_INCLUDED
