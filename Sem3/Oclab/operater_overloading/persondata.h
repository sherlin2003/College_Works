#ifndef PERSONDATA_H_INCLUDED
#define PERSONDATA_H_INCLUDED

#include <string>
#include <iostream>
using namespace std;
class PersonData{
   private:
            string lastName;
            string firstName;
            string address;
            string city;
            string state;
            string zip;
            string phone;
    public:
            PersonData();
            PersonData(string,string,string,string,string,string,string);
            string getLastName() const;
            string getFirstName() const;
            string getAddress() const;
            string getCity() const;
            string getState() const;
            string getZIP() const;
            string getPhoneNumber() const;
            void setLastName(string n);
            void setFirstName(string n);
            void setAddress(string a);
            void setCity(string c);
            void setState(string s);
            void setZIP(string z);
            void setPhoneNumber(string p);
};



#endif // PERSONDATA_H_INCLUDED
