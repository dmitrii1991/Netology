import psycopg2

def create_db(dbname_, user_, password_):
    conn = psycopg2.connect(dbname=dbname_, user=user_, password=password_)
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

def get_students(course_id): # возвращает студентов определенного курса
    pass

def add_students(course_id, students): # создает студентов и 
                                       # записывает их на курс
    pass


def add_student(student): # просто создает студента
    pass

def get_student(student_id):
    pass


# create_db("netology_db", "postgres", "1234")
