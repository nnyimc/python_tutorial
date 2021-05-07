#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mysql.connector import connection, errorcode
import mysql.connector

try:
    # Connexion
    cnx = connection.MySQLConnection(user="nnyimc", password="", 
                                     host="127.0.0.1", database="hibernate")
    # Initialisation du curseur
    cursor = cnx.cursor()
    
    # Ecriture de la requête SQL
    insert_stmt = (
    "INSERT INTO ingenieur (mle, nom, prenom, codepost, ville)"
    "VALUES (%s, %s, %s, %s, %s)" 
    )
    
    # Données affectées aux variables : %s
    data = (1202,'DOE', 'JANE', '92000', 'Nanterre') 
    
    # Execution de la requête
    cursor.execute(insert_stmt, data)
    
    # Confirmation de l'opération
    cnx.commit()
    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Il y a un problème avec votre username ou password");
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base n'existe pas")
    else: print(err)
else: cnx.close()