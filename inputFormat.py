#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  6 10:09:38 2021

@author: nnyimc
"""

# * - multiplication
print(2*3);

# ** - exposant
print(2**3);

# * - Initialiser une lsite
liste_test = [2] * 10;
print(liste_test);

# input - saisie clavier
prenom = input("Qui êtes-vous ??: ");
print("Bonjour", prenom);

age = int(input("Quel âge avez vous ?: "));
print ("Vous avez", age , "ans");

a, b, c = 2, 9, 4;
print("{}, {} et {}".format( a, b, c**a));

stock1 = ["papier", "encre", "buvard", "cahier", "crayon"];
stock2 = ["bmw", "audi", "tesla", "ford", "mercedes"];
print("Nous avons de l'{0[1]} et du {0[2]} \n livrés par {1[2]}".format(stock1, stock2));

