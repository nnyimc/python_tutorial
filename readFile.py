#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Ouvrir un fichier
#Le lire ligne par ligne
#Afficher chaque mot de la ligne
f = open("copyExercice.py", "r", encoding="utf-8");
listeMots = [];

for ligne in f: 
    for mot in ligne.split():
        if mot not in listeMots:
            listeMots.append(mot);
f.close();

listeMots.sort();
print(listeMots);

# using with
with open("copyExercice.py", encoding="utf-8") as f:
    listeMots = [];

    for ligne in f: 
        for mot in ligne.split():
            if mot not in listeMots:
                listeMots.append(mot);
listeMots.sort();
print(listeMots);
