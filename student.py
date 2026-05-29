from db_connection import db_connect


def add_student():
    con=db_connect()
    cur=con.cursor()

    name=input("Enter Student Name:")
    course=input("Enter Course Name:")
    mobile=input("Enter Mobile Number:")
    email=input("Enter Email ID:")
    query='''insert into students(student_name,course,phone,email) values(%s,%s,%s,%s)'''
    cur.execute(query,(name,course,mobile,email))
    con.commit()
    cur.close()
    con.close()
    print("Student added successfully")


def view_student():
    con=db_connect()
    cur=con.cursor()
    query='''select *from students'''
    cur.execute(query)
    students=cur.fetchall()
    print("\n----Student Records----")
    for std in students:
        print(std)
    con.commit()
    cur.close()
    con.close()


def delete_student():
    con=db_connect()
    cur=con.cursor()
    student_id=input("Enter the student_id you want to delete:")
    query='''delete from students where student_id=%s'''
    cur.execute(query,(student_id,))
    con.commit()
    cur.close()
    con.close()
    print("Student deleted successfully")
