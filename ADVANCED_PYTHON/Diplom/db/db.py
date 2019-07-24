import psycopg2

def create_db(dbname_, user_, password_):
    conn = psycopg2.connect(dbname=dbname_,
                            user=user_,
                            password=password_)

    cur = conn.cursor()
    cur.execute("""CREATE TABLE VKinder(
        id serial PRIMARY KEY NOT NULL,
        id_vk varchar(100) NOT NULL,
        points numeric(1000),
        fotos varchar(1000));
        """)
    conn.commit()
    conn.close()

def add_users(user_list, dbname_, user_, password_):
    conn = psycopg2.connect(dbname=dbname_,
                            user=user_,
                            password=password_)
    cur = conn.cursor()
    for user in user_list:
        id_vk, points, fotos = user[1], user[0], user[2]
        cur.execute('insert into VKinder (id_vk, points, fotos) values(%s, %s, %s)', (id_vk, points, fotos))
    conn.commit()
    conn.close()