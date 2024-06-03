import mysql.connector

try:
     config = {
    'host' : 'localhost',
    'user' : 'mgalina302',
    'password': 'WSGZerct77mf&M7d',
    'database': 'mgalina302'
}

     print('successfully connected...')
except Exception as ex:
    print('connection refused')
    print(ex)

