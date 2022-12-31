# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
import pandas as pd
from texttable import Texttable


def get_sorted_list_of_country_names(countries):
    countries_list  = list(countries.keys())
    countries_list.sort()
    return countries_list


def sort_countries_by_medal_type_ascending(countries, medal_type):
    if medal_type in ["gold", "silver", "bronze", "total"]:
        countryMedals_list = list(countries.values())
        return sorted(countryMedals_list, key=lambda x: x.get_medals(medal_type))
    else:
        return None


def sort_countries_by_medal_type_descending(countries, medal_type):
    if medal_type in ["gold", "silver", "bronze", "total"]:
        countryMedals_list = list(countries.values())
        return sorted(countryMedals_list, key=lambda x: x.get_medals(medal_type), reverse=True)
    else:
        return None


def read_positive_integer():
    while True:
        try:
            n = int(input(">> Enter the threshold (a positive integer): "))
            if isinstance(n, int) and n>=0:
                break
        except:
            pass
    return n


def read_country_name():
    countries_list = get_sorted_list_of_country_names(countries)
    while True:
        country = input(">> Insert a country name: ")        
        if country in countries_list:
            return country
        else:
            print("Type one from:")
            for country in countries_list:
                print(country)
               

def read_medal_type():
    accepted = ["gold", "silver", "bronze", "total"]
    while True:
        medal_type = input(">> Insert a medal type: ")        
        if medal_type in accepted:
            return medal_type
        else:
            print("Type one from:")
            for medal_type in accepted:
                print(medal_type)
                
class CountryMedals:
    def __init__(self, name, gold, silver, bronze):
        self.name = name
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
    
    def to_json(self):
        return json.dumps(self.__dict__)
    
    def get_medals(self, medal_type):
        if medal_type == "gold":
            return self.gold
        elif medal_type == "silver":
            return self.silver
        elif medal_type == "bronze":
            return self.bronze
        elif medal_type == "total":
            return self.gold + self.bronze + self.silver
        else:
            return None
    
    def print_summary(self):
        print(f'{self.name} received {self.get_medals("total")} medals in total; {self.gold} gold, {self.silver} silver, and {self.bronze} bronze.')
    
    def compare(self, country2):
        total1 = self.get_medals("total")
        total2 = country2.get_medals("total")
        t = Texttable()
        t.add_row(["",self.name,country2.name])
        t.add_row(["Total",total1,total2])
        t.add_row(["Gold",self.gold,country2.gold])
        t.add_row(["silver",self.silver,country2.silver])
        t.add_row(["bronze",self.bronze,country2.bronze])
        print(t.draw())
    
    

# germany = CountryMedals("Germany", 17, 19, 10)

# print(germany.to_json())
# print(germany.get_medals("total"))
# germany.print_summary()


countries = dict()
medals_data = pd.read_csv("Medals.csv")
# print(medals_data.columns)

for row in medals_data.itertuples():
    countries[row.Country] = CountryMedals(row.Country, row.Gold, row.Silver, row.Bronze)
    
# for key, val in countries.items():
#     print(key,"--->", val.to_json())


# print(get_sorted_list_of_country_names(countries))


while True:
    c = input("Insert a command ( Type 'H' for help ): ")
    
    if c=="l" or c=="L":
        countries_list = get_sorted_list_of_country_names(countries)
        print(f"The dataset contains {len(countries_list)} countries: ", end="")
        for country in countries_list:
            print(country, end=", ")
        print()
     
    elif c=="S" or c=="s":
        country_name = read_country_name()
        countries[country_name].print_summary()
    
    elif c=="C" or c=="c":
        print("Compare countries")
        country1 = read_country_name()
        print(f"Insert the name of the country you want to compare against {country1}")
        country2 = read_country_name()
        countries[country1].compare(countries[country2])
    
    elif c=="M" or c=="m":
        print("Given a medal type, lists all the countries that received more medals than a threshold")
        medal_type = read_medal_type()
        n = read_positive_integer()
        
        countryMedals_list = sort_countries_by_medal_type_descending(countries, medal_type)
        
        print(f"Countries that received more than {n} {medal_type} medals:")
        for i in countryMedals_list:
            if i.get_medals(medal_type) <=n:
                break
            else:
                print(f"- {i.name} received {i.get_medals(medal_type)}")
                
    elif c=="F" or c=="f":
        print("Given a medal type, lists all the countries that received fewer medals than a threshold")
        medal_type = read_medal_type()
        n = read_positive_integer()
        
        countryMedals_list = sort_countries_by_medal_type_ascending(countries, medal_type)
        
        print(f"Countries that received fewer than {n} {medal_type} medals:")
        for i in countryMedals_list:
            if i.get_medals(medal_type) >=n:
                break
            else:
                print(f"- {i.name} received {i.get_medals(medal_type)}")
    
    elif c=="E" or c=="e":
        with open("countries.json", "w") as outfile:
            outfile.write("{\n")
            for i in countries.values():
                outfile.write(f"{i.name}: ")
                outfile.write(i.to_json())
            outfile.write("\n}")
        
        
        
    
# l1 = sort_countries_by_medal_type_ascending(countries, "gold")
# for i in l1:
#     i.print_summary()

# l2 = sort_countries_by_medal_type_descending(countries, "gold")
# for i in l2:
#     i.print_summary()

x = read_positive_integer()
cntry = read_country_name()
medal_t = read_medal_type()