#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 13:17:24 2022

@author: alexandre
"""
import copy
import random

class Hat:

    contents = dict()

    def __init__(self, **balls):

        self.contents = balls
        
        self.content = [[key]*value for key, value in self.contents.items()]
        
        self.contents = [item for sublist in self.content for item in sublist]
      
    def __str__(self):
        
        string =  f"This hat contains {self.contents}"
        
        return string
    
    def draw(self, number):
        
        liste_nombres = list()
        
        if number>=len(self.contents):
            
            liste_nombres = self.contents
        
        else:
        
            j=0
            
            while j<number:
                
               liste_nombres.append(self.contents.pop(random.randrange(len(self.contents))))
               
               j+=1
               
        return liste_nombres
          
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    
    liste_original = hat.contents
    
    #print("liste_original",liste_original)
    
    #print("hat_original", hat)
    
    count_final = 0
    
    j=0
    
    while j<num_experiments:
        
        hat1 = copy.deepcopy(hat)
        
        liste_balls = hat1.draw(num_balls_drawn)
        
        #print("hat", hat)
        
        #print("liste_balls_boucle", liste_balls)
        
        #print("expected balls", expected_balls)
    
        count = 0
        
        for key, value in expected_balls.items():
            
            if key in liste_balls and liste_balls.count(key) >= value:
                
                count+=1
                
                #print("count", count)
            
        if count==len(list(expected_balls.keys())):
            
            count_final+=1
            
            #print("count_final", count_final)
        
        j+=1
        
    probability = count_final/num_experiments
    
    #print(probability)
    
    return probability
            
            
        
        
      
hat1 = Hat(yellow=3, blue=2, green=6)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)

experience = experiment(hat1, {'blue':2, 'green':1}, 4, 50)

