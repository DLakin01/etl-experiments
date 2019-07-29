from os import environ

mysql_config = {
    'user': 'root',
    'password': environ['MYSQL_PASSWORD'],
    'host': "localhost",
    'database': 'employees'
}