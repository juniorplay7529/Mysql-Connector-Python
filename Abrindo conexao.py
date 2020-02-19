import mysql.connector
from mysql.connector import errorcode

try:
    cnx = mysql.connector.connect(
        user='usuario', database='nome do bando de dados')
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Algo está errado com seu nome de usuário ou senha")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Esse banco de dados não existe")
    else:
        print(err)
else:
    cnx.close()
