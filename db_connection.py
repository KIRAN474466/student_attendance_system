import mysql.connector as db


def db_connect():
    con=db.connect(user="root",password="Kiran@474",
    host="localhost",database="Attendance")
    return con
