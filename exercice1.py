#!/usr/bin/env python3
# -*- coding: utf-8 -*-
maPhrase = "bonjour tout le monde";
print(maPhrase);
print(maPhrase[0]);
print(maPhrase[-1]);
print(maPhrase[1:4]);
print(maPhrase[3:]);
print(maPhrase.startswith("bon"));
print(maPhrase.endswith("monde"));

maListe = ["a", "b", "c", "d"];
print(maListe);
print("Le premier élément de la liste est: " + maListe[0]);
print("Le dernier élément est: " + maListe[-1]);
print("L'avant dernier élément de la liste est: " + maListe[-2]);
del maListe[1];
maListe.remove("d");
print(maListe);
#Inverser les éléments de la liste
maListe.reverse();
print("Taille: " + str(len(maListe)));
print(maListe.count("a"));
print(""" Afficher tout type de caractères !*$⁾)ààç:çé""'c""");