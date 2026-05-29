from db_connection import db_connect


def login():
    username=input("Enter the username:")
    password=input("Enter the password:")
    con=db_connect()
    cur=con.cursor()
    cur.execute('''select count(*) from users where username=%s and password=%s''',(username,password))
    count=cur.fetchone()
    if count[0]>0:
        return True
    else:
        return False
