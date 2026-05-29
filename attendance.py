from db_connection import db_connect
from datetime import date
 
def mark_attendance():
    con=db_connect()
    cur=con.cursor()
    today=date.today()
    cur.execute('''select student_id,student_name from students''')
    for std in cur.fetchall():
        attendance=input(f'{std[1]} P/A?:')
        query='''insert into attendance(student_id,date,status) values(%s,%s,%s)'''
        cur.execute(query,(std[0],today,attendance.upper()))
        con.commit()
        cur.close()
        con.close()
