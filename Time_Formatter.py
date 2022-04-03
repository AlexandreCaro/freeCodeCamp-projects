#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 20:06:18 2022

@author: alexandre
"""

def add_time(start, *duree):
    
    duration = duree[0]
    
    liste_temps = start.split()
    
    liste_heure = liste_temps[0].split(':')
    
    liste_heure = [int(i) for i in liste_heure]
    
    part_of_day = liste_temps[1]
    
    days = ""
    
    if len(duree)>1:
        
        jour = duree[1]
    
    if liste_temps[1] == 'PM':
        liste_heure[0] += 12
        
    else:
        pass
    
    liste_duree = duration.split(':')
    liste_duree = [int(i) for i in liste_duree]
    
    liste_somme = [liste_heure[i] + liste_duree[i] for i in range(len(liste_heure))]
    
    if liste_somme[1] >= 60:
        liste_somme[0] += 1
        liste_somme[1] -= 60
    else:
        pass
    
    heure_totale = liste_somme[0]
    heure_corrigee = heure_totale//24 #Cela compte le nombre de jours.
    heure_restante = heure_totale%24
    
    """
    ensemble_heure = [24*i for i in range(heure_corrigee+1)] #La longueur de cette liste compte le nombre de jours écoulés.
    ensemble_part_of_day = [12*j for j in range(heure_corrigee*2)] #Si c'est entre un index divisible par 2
    # et non divisible par 2 c'est AM et si c'est entre un index non divisible par 2 et
    #divisible par 2 c'est PM.
    
    #heure_restante = heure_totale - ensemble_heure[-1]
    print("heure_restante",heure_restante)
    print(ensemble_part_of_day)
    print(len(ensemble_heure))
    print(len(ensemble_part_of_day))
    """
    
    jours_semaine = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    num_of_days = liste_somme[0]//24
    
    if len(duree)>1:
    
        final_index = jours_semaine.index(jour.lower()) + num_of_days
        
        if final_index > 6:
            final_index = final_index // 7 - 3
    
        jour = jours_semaine[final_index]
    
        jour = jour[0].upper() + jour[1:]
    
    if num_of_days == 1:
        days = " (next day)"
    elif num_of_days > 1:
        days = " ({} days later)".format(num_of_days)
        
    
    liste_AM = [0,1,2,3,4,5,6,7,8,9,10,11, 24]
    liste_PM = [i for i in range(12, 24)]
    
    if heure_restante in liste_AM:
        part_of_day = 'AM'
    elif heure_restante in liste_PM:
        part_of_day = 'PM'
        heure_restante -= 12
        
    if heure_restante == 0:
        heure_restante = 12
    elif heure_restante == 24:
        heure_restante = 12
    elif heure_restante in liste_PM:
        heure_restante -= 12
    
    
        
    if len(duree)>1:
        if len(str(liste_somme[1]))==1:
            string = str(heure_restante) + ":" + "0" + str(liste_somme[1]) + " " + part_of_day + "," + " " + jour + days
        else:
            string = str(heure_restante) + ":" + str(liste_somme[1]) + " " + part_of_day + "," + " " + jour + days
    else:
        if len(str(liste_somme[1]))==1:
            string = str(heure_restante) + ":"+ "0" + str(liste_somme[1]) + " " + part_of_day + days
        else:
            string = str(heure_restante) + ":" + str(liste_somme[1]) + " " + part_of_day + days
    
    
    #print(heure_restante)
    #print(liste_somme)
    #print(liste_PM)
    print(string)
    
    return string


add_time("3:30 PM", "2:12")
add_time("11:55 AM", "3:12")
add_time("9:15 PM", "5:30")
add_time("11:40 AM", "0:25")
add_time("2:59 AM", "24:00")
add_time("11:59 PM", "24:05")
add_time("8:16 PM", "466:02")
add_time("5:01 AM", "0:00")
add_time("3:30 PM", "2:12", "Monday")
add_time("2:59 AM", "24:00", "saturDay")
add_time("11:59 PM", "24:05", "Wednesday")
add_time("8:16 PM", "466:02", "tuesday")