#ifndef PREFERREDCUSTOMER_H_INCLUDED
#define PREFERREDCUSTOMER_H_INCLUDED

#include "CustomerData.h"
#include <iostream>
using namespace std;

class PreferredCustomer : public CustomerData{
private:
    double purchasesAmount;
    double discountLevel;

public:
    PreferredCustomer();
    PreferredCustomer(double);
    double getDiscount(double);
    //accessor functions
    double getPurchasesAmount() const;
    double getDiscountLevel() const;

    //mutator functions
    void setPurchasesAmount(double);
    void increasePurchases(double i);

};


#endif // PREFERREDCUSTOMER_H_INCLUDED
