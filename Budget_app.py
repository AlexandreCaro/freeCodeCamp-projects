#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 20:18:05 2022

@author: alexandre
"""

import math

class Category:

    def __init__(self, name):

        self.name = name
        self.ledger = []

    def deposit(self, amount, des = ""):

        self.ledger.append({"amount":amount, "description": des})
    
        #print(self.ledger)

    def withdraw(self, amount, des = ""):

        if self.check_funds(amount)==False:
            return False
    
        elif self.check_funds(amount)==True:
            self.ledger.append({"amount":-1*amount, "description":des})
            #print(self.ledger)
            return True

    def get_balance(self):

        quantite_positive = [self.ledger[i]["amount"] for i in range(len(self.ledger)) if self.ledger[i]["amount"]>0]

        quantite_negative = [self.ledger[i]["amount"] for i in range(len(self.ledger)) if self.ledger[i]["amount"]<0]

        total_positif = sum(quantite_positive)
        total_negatif = sum(quantite_negative)

        balance = total_positif + total_negatif

        return balance
    
    def transfer(self, amount, categorie):
        
        if self.check_funds(amount):
        
            self.withdraw(amount, des="Transfer to {}".format(categorie.name))
        
            categorie.deposit(amount, des="Transfer from {}".format(self.name))
            
            return True
        
        else:
            
            return False
        
    def check_funds(self, amount):
        
        if self.get_balance() - amount >= 0:
            
            return True
        
        elif self.get_balance() - amount < 0:
            
            return False
      
    def __str__(self):
        
        string = "{:*^30}".format(self.name) + "\n"
        
        for i in range(len(self.ledger)):
            
            string += "{:<23.23}{:>7}".format(self.ledger[i]["description"], self.ledger[i]["amount"]) + "\n"
            
        string += "Total: {}".format(self.get_balance())
        
        return string
    
    def __repr__(self):
        
        string = "{:*^30}".format(self.name) + "\n"
        
        for i in range(len(self.ledger)):
            
            string += "{:<23.23}{:>7}".format(self.ledger[i]["description"], self.ledger[i]["amount"]) + "\n"
            
        string += "Total: {}".format(self.get_balance())
        
        return string
    

def create_spend_chart(categories):
    
    pourcentage = dict()
    
    for i in range(len(categories)):
        
        quantite_negative = [categories[i].ledger[j]["amount"] for j in range(len(categories[i].ledger)) if categories[i].ledger[j]["amount"]<0]
        
        total_negatif = sum(quantite_negative)
        
        pourcentage[categories[i].name] = total_negatif
        
    somme = 0
    
    for value in pourcentage.values():
        
        somme += value
    
    for keys in pourcentage.keys():
        
        pourcentage[keys] = (pourcentage[keys]/somme) * 100
        
        #print(pourcentage)
        
        pourcentage[keys] = int(math.floor(pourcentage[keys]/10.0))*10
        
    lst = list(range(0,10+1))
    
    lst.reverse()
    
    lst = [str(lst[i]*10) for i in range(len(lst))]
    
    lst[-1] = " 0"

    dict_list = dict()
    
    values = list(pourcentage.values())
    
    keys = list(pourcentage.keys())
    
    #print("values", values)
    
    for i in range(len(pourcentage.keys())):
        
        dict_list["lst_{}".format(keys[i])] = [" "] * (10-values[i]//10) + ['o']*((values[i]//10)+1)
        
    string = "Percentage spent by category" + "\n"
    
    #print("dict_list[lst_Food]",dict_list["lst_Food"])
    
    dict_name = dict()
    
    for i in range(len(keys)):
        
        dict_name["lst_{}".format(keys[i])] = [keys[i] + " "*(max([len(keys[j]) for j in range(len(keys))])-len(keys[i]))]
    
    #print("dict_name", dict_name)
    
    for i in range(len(lst)):
        
        if i==0:
            
            string += "{}|".format(str(lst[i]))
        
        else:
        
            string += " {}| ".format(str(lst[i]))
        
        for j in range(len(keys)):
        
            string += dict_list["lst_{}".format(keys[j])][i] + "  "
            
        string += "\n"
        
    string += 4*" " + "-"*(1 + 3*len(keys)) + "\n"
    
    len_string = max([len(keys[j]) for j in range(len(keys))])
    
    #print(len_string)

    for i in range(len_string):
        
        string += 5*" "
        
        for j in range(len(keys)):
        
            string += dict_name["lst_{}".format(keys[j])][0][i] + "  "
        
        string += "\n"
        
    return string

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
#print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)
print(food)
print(clothing)
print(auto)
print(create_spend_chart([food, clothing, auto]))
