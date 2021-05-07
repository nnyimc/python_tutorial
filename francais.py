#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Francais:    
    @staticmethod
    def afficheNationalite():
        print("Français");
    
# Appel de la méthode statique
print(Francais.afficheNationalite());

# Constructeur non obligatoire
unFrancais = Francais();
print(unFrancais.afficheNationalite());

#class Toulousain(Francais):
#   pass #classe  vide

class Toulousain(Francais):
    @staticmethod  # doit être reprécisé dans la classe fille
    def afficheNationalite():
        print("Toulouse");
        
Toulousain.afficheNationalite();
unToulousain = Toulousain();
unToulousain.afficheNationalite();