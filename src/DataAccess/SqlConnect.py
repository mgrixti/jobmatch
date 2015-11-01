__author__ = 'mgrixti'

import mysql.connector
from mysql.connector import errorcode

class SqlConnect():

    conn = None

    # Establish connection to Database
    def connect(self):
        try:
            SqlConnect.conn = mysql.connector.connect(user='fakeuser', password='notrealpass', host='fakehost',
                                    database='fakedatabase')
            print("Connection Successful")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

    # Close connection to database
    def close(self):
        SqlConnect.conn.close()