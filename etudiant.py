#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class etudiant:
    nbEtudiants = 0;
    
    def __init__(self, nom, age, sexe="M"):
        self.__Nom = nom;
        self.__Age = age;
    
    def get_age(self):
        return self.__Age;
    
    def set_age(self, nouvAge):
        self.__Age = nouvAge;
    
    def get_nom(self):
        return self.__Nom;
    
    def set_nom(self, nouvNom):
        self.__Nom = nouvNom;

class master(etudiant):
    def __init__(self, nom, section):
        etudiant.__init__(self, nom, section)
        self.nom = nom;
        self.section = section;
    
    def get_section(self):
        print("Section:", self.section)

E1 = etudiant("Jean", 34);
E2 = etudiant("Inès", 42, "F");
print("Age: ", E1.get_age());
print("Age: ", E2.get_age());

EM = master("Morin", "Data Science");
print(EM.get_section());
