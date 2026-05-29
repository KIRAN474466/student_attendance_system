from login import login
from student import add_student
from student import view_student
from student import delete_student
from course import add_course
from attendance import mark_attendance
from report import attendance_report

if login():
    while True:
        print('1. Add student')
        print('2 .View student')
        print('3. Add course')
        print('4. Mark attendance')
        print('5. Attendance report')
        print('6. Delete student')
        print('7. Exit')

        ch=int(input('Choose one option:'))
        if ch==1:
            add_student()

        elif ch==2:
            view_student()
            
        elif ch==3:
            add_course()

        elif ch==4:
            mark_attendance()

        elif ch==5:
            attendance_report()

        elif ch==6:
            delete_student()

        elif ch==7:
            break

        else:
            print("choose correct option:")

    

else:
    print("You are not valid user")
