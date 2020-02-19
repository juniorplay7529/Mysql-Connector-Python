import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="nome do usuario",
    passwd="senha do usuario"
)

#variavel na qual passa um string sendo o nome do banco
DB_NOME = "teste"

#cursor o possibilita realizar diversas atividades
#como, passar comandos sql.
cursor = db.cursor()

#comando passar execução de instruções sql
cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(DB_NOME))

#Fechando conexão, lembre sempre de fechar
#Senão pode ocorrer erros no bancos de dados
cursor.close()