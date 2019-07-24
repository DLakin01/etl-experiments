import mysql.connector as mysql
from config import mysql_config

def pull_data(sql_query):
    cnx = mysql.connect(**mysql_config)
    cursor = cnx.cursor()
    cursor.execute(sql_query)

    data = cursor.fetchall()
    cursor.close()

    if data:
        return data