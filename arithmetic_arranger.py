#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 11 20:13:38 2022

@author: alexandre
"""

def arithmetic_arranger(problems):
    
    condition = False
    
    if True in problems:
        condition = problems[1]
        problemes = problems[0].copy()
    elif True not in problems and isinstance(problems[0],list):
        problemes = problems[0].copy()
        print("problems", problemes)
    else:
        problemes = problems.copy()
    
    #print("problems", problems)
    print('type',type(problems[0]))
    print('problems0', problems[0])
    
    liste_nombre = list()
    string = ""
    
    if len(problemes)> 5:
        return "Error: Too many problems."
    
    for problem in problemes:
        
        liste_nombre.append(problem.split())

    liste_operande_gauche = [liste_nombre[i][0] for i in range(len(liste_nombre))]

    liste_operateur = [liste_nombre[i][1] for i in range(len(liste_nombre))]
    
    if '/' in liste_operateur or '*' in liste_operateur:
        return "Error: Operator must be '+' or '-'."

    liste_operande_droite = [liste_nombre[i][2] for i in range(len(liste_nombre))]
    
    for i in liste_operande_gauche:
        for j in liste_operande_droite:
            if len(i) > 4 or len(j) > 4:
                return "Error: Numbers cannot be more than four digits."
            elif i.islower() == True or j.islower() == True:
                return "Error: Numbers must only contain digits."
                

    for i in range(len(liste_operande_gauche)):
        
        if i < len(liste_operande_gauche)-1:

            string += " "*(max(len(liste_operande_gauche[i]),len(liste_operande_droite[i]))-len(liste_operande_gauche[i]) + 2) + liste_operande_gauche[i] + 4*" "
        
        else:
            
            string += " "*(max(len(liste_operande_gauche[i]),len(liste_operande_droite[i]))-len(liste_operande_gauche[i]) + 2) + liste_operande_gauche[i]
            
    string += "\n"

    for i in range(len(liste_operateur)):
        
        if i < len(liste_operateur)-1:

            string += liste_operateur[i] + " "*(max(len(liste_operande_gauche[i]),len(liste_operande_droite[i]))-len(liste_operande_droite[i]) + 1) + liste_operande_droite[i] + 4*" "
        
        else:
            string += liste_operateur[i] + " "*(max(len(liste_operande_gauche[i]),len(liste_operande_droite[i]))-len(liste_operande_droite[i]) + 1) + liste_operande_droite[i]
            
    string += "\n"

    for i in range(len(liste_operateur)):
        
        if i < len(liste_operateur)-1:

            string += (max(len(liste_operande_gauche[i]),len(liste_operande_droite[i]))+2)*"-" + 4* " "
        
        else:
            
            string += (max(len(liste_operande_gauche[i]),len(liste_operande_droite[i]))+2)*"-"
            
    if condition==False:
        pass
    else:
        liste_resultat = [eval(problem) for problem in problemes]
        
        print("liste_resultat", liste_resultat)
        string += '\n'
        
        for i in range(len(liste_resultat)):
            
            if i < len(liste_resultat)-1:
            
                string += " "*(max(len(liste_operande_gauche[i]),len(liste_operande_droite[i]))-len(str(liste_resultat[i]))+2) + str(liste_resultat[i]) + 4*" "
                
            else:
                
                string += " "*(max(len(liste_operande_gauche[i]),len(liste_operande_droite[i]))-len(str(liste_resultat[i]))+2) + str(liste_resultat[i])
                
    print(string)
    return string
    
test1 = ['32 + 698', '3801 - 2', '45 + 43', '123 + 49']
test2 = [['3801 - 2','123 + 49']]
test3 = [['1 + 2', '1 - 9380']]
testtrue = [['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True]
testTrue2 = [['3 + 855', '988 + 40'], True]
testError = [['3 / 855', '3801 - 2', '45 + 43', '123 + 49']]
testdigit = [['24 + 85215', "3801 - 2", "45 + 43", "123 + 49"]]
testNumber = [['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']]
testProblems = [['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']]