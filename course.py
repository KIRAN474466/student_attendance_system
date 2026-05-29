from db_connection import db_connect

def add_course():
    con=db_connect()
    cur=con.cursor()
    course_name=input("Course Name:")
    faculty_name=input("Faculty Name:")
    query='''insert into courses(course_name,faculty_name) values(%s,%s)'''
    cur.execute(query,(course_name,faculty_name))
    con.commit()
    cur.close()
    con.close()
