#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from mysql.connector import connection, errorcode
try:
    cnx = connection.MySQLConnection(user="nnyimc", password="P!4st!qu3", 
                                     host="127.0.0.1", database="hibernate")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Il y a un problème avec votre username ou password");
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("La base n'existe pas")
    else: print(err)
else: cnx.close()