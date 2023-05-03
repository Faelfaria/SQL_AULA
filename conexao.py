import mysql.connector

def conectar():
    mybd = mysql.connector.connect(
        host = 'dbbaula.cexhup6dxtvg.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password = 'aulanoiteFaculdade',
        database = 'aula'
    )
    return mybd