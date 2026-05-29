from db_connection import db_connect

def attendance_report():
    con=db_connect()
    cur=con.cursor()

    stdno=input("Enter student ID:")
    no_classes='''select count(*) from attendance where student_id=%s'''
    p_classes='''select count(*) from attendance where student_id=%s and status=%s'''
    cur.execute(no_classes,(stdno,))
    num_classes=cur.fetchone()[0]
    cur.execute(p_classes,(stdno,'P'))
    present_classes=cur.fetchone()[0]

    if num_classes>0:
        percentage=(present_classes/num_classes)*100
    else:
        percentage=0

    print('*'*10,'Attendance Report','*'*10)
    print('Number of classes',num_classes)
    print('Classes attended',present_classes)
    print('Attendance percentage',percentage)
    con.commit()
    cur.close()
    con.close()
