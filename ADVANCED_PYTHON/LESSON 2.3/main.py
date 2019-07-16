import psycopg2

def create_db(dbname_, user_, password_):
    conn = psycopg2.connect(dbname=dbname_,
                            user=user_,
                            password=password_)

    cur = conn.cursor()
    cur.execute("""CREATE TABLE student (
        id serial PRIMARY KEY NOT NULL,
        name varchar(100) NOT NULL,
        gpa numeric(10,2),
        birth timestamp with time zone);
        """)
    cur.execute("""CREATE TABLE course (
        id serial PRIMARY KEY NOT NULL,
        name varchar(100) NOT NULL);
        """)
    cur.execute("""CREATE TABLE student_course (
        id serial PRIMARY KEY NOT NULL,
        student_id INTEGER REFERENCES student(id),
        course_id INTEGER REFERENCES course(id));
        """)
    conn.commit()
    conn.close()

def add_course(course_list, dbname_, user_, password_): # добавить курс в таблицу курсов
    conn = psycopg2.connect(dbname=dbname_,
                            user=user_,
                            password=password_)
    cur = conn.cursor()
    for course in course_list:
        id_course, name_course = course['id'], course['name']
        cur.execute('insert into course (id, name) values(%s, %s)', (id_course, name_course))
    conn.commit()
    conn.close()

def get_students(course_id: int, dbname_, user_, password_): # возвращает студентов определенного курса
    id_student = []
    conn = psycopg2.connect(dbname=dbname_,
                            user=user_,
                            password=password_)
    cur = conn.cursor()
    cur.execute("select course_id from student_course")
    rows = cur.fetchall()
    if (course_id,) in rows:
        cur.execute("select student_id, course_id from student_course")
        rows = cur.fetchall()
        for student, course in rows:
            if course == course_id:
                id_student.append(student)

        cur.execute("select id, name, gpa, birth from student")
        rows = cur.fetchall()
        for row in rows:
            if row[0] in id_student:
                print(f"""
                ID: {row[0]}
                Name: {row[1]}
                GPA: {row[2]}
                birth: {row[3]}
                        """, end='\n')
    else:
        print('Нет студентов в курсе')

def add_students(course_id: int, students: list, dbname_, user_, password_):  # создает студентов и записывает их на существующий курс
    conn = psycopg2.connect(dbname=dbname_,
                            user=user_,
                            password=password_)
    cur = conn.cursor()
    cur.execute("select id from course")
    rows = cur.fetchall()
    if (course_id,) in rows:
        for student in students:
            name, gpa, birth = student['name'], student['gpa'], student['birth']
            cur.execute('insert into student (name, gpa, birth) values (%s, %s, %s) RETURNING id', (name, gpa, birth))
            id_of_new_row = cur.fetchone()[0]  # возвращает первичный
            cur.execute('insert into student_course (student_id, course_id) values (%s, %s)', (id_of_new_row, course_id))
    else:
        print('Нет id данного курса')
    conn.commit()
    conn.close()  #

def add_student(students: list, dbname_, user_, password_): # просто создает студента
    for student in students:
        name, gpa, birth = student['name'], student['gpa'], student['birth']
        conn = psycopg2.connect(dbname=dbname_,
                                user=user_,
                                password=password_)
        cur = conn.cursor()
        cur.execute('insert into student (name, gpa, birth) values (%s, %s, %s)', (name, gpa, birth))
        conn.commit()
        conn.close()

def get_student(student_id: int, dbname_, user_, password_):  # получить информацию о студенте
    conn = psycopg2.connect(dbname=dbname_,
                            user=user_,
                            password=password_)
    cur = conn.cursor()
    cur.execute("select id from student")
    rows = cur.fetchall()
    if (student_id,) in rows:
        cur.execute("select id, name, gpa, birth from student")
        numb_of_list_id = rows.index((student_id,))
        rows = cur.fetchall()
        print(f"""
ID: {rows[numb_of_list_id][0]}
Name: {rows[numb_of_list_id][1]}
GPA: {rows[numb_of_list_id][2]}
birth: {rows[numb_of_list_id][3]}
        """, end='\n')

        cur.execute("select student_id from student_course ")
        rows = cur.fetchall()
        if (student_id,) in rows:
            cur.execute("select id, student_id, course_id from student_course ")
            numb_of_list_id_course = rows.index((student_id,))
            rows = cur.fetchall()
            print(f"Course:{rows[numb_of_list_id_course][2]}")
        else:
            print('Нет записи на какие-либо курсы')
    else:
        print('Нет такого студента')


students = [
    {'name': 'Дима', 'gpa': 9, 'birth': '14.11.2000'},
    {'name': 'Аня', 'gpa': 8, 'birth': '25.05.2001'},
    {'name': 'Полина', 'gpa': 5, 'birth': '04.02.2002'},
]
students1 = [
    {'name': 'Егор', 'gpa': 2, 'birth': '14.11.2003'},
]
course_list = [
    {'id': 5, 'name': 'math'},
    {'id': 33, 'name': 'prog'},
]

if __name__ == "__main__":
    # create_db("netology_db", "postgres", "1234")
    # add_course(course_list, "netology_db", "postgres", "1234")
    # add_student(students, "netology_db", "postgres", "1234")
    # add_students(33, students1, "netology_db", "postgres", "1234")
    # get_student(23, "netology_db", "postgres", "1234")
    # get_students(33, "netology_db", "postgres", "1234")
