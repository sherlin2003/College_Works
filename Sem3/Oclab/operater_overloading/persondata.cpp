#include <iostream>
#include <string>
#include "PersonData.h"
using namespace std;
PersonData::PersonData()
{
    lastName = "";
    firstName = "";
    address = "";
    city = "";
    state = "";
    zip = "";
    phone = "";
}
PersonData::PersonData(string ln, string fn, string add, string c, string s, string z, string p)
{
    lastName = ln;
    firstName = fn;
    address = add;
    city = c;
    state = s;
    zip = z;
    phone = p;
}
string PersonData::getLastName() const
{
    return lastName;
}
string PersonData::getFirstName() const
{
    return firstName;
}
string PersonData::PersonData::getAddress() const
{
    return address;
}
string PersonData::PersonData::getCity() const
{
    return city;
}
string PersonData::getState() const
{
    return state;
}
string PersonData::getZIP() const
{
    return zip;
}
string PersonData::getPhoneNumber() const
{
    return phone;
}
void PersonData::setLastName(string n)
{
    lastName = n;
}
void PersonData::setFirstName(string n)
{
    firstName = n;
}
void PersonData::setAddress(string a)
{
    address = a;
}
void PersonData::setCity(string c)
{
    city = c;
}
void PersonData::setState(string s)
{
    state = s;
}
void PersonData::setZIP(string z)
{
    zip = z;
}
void PersonData::setPhoneNumber(string p)
{
    phone = p;
}
