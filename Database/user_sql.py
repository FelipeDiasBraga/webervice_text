import psycopg2

from psycopg2.extras import DictCursor


def get_connect():
    return psycopg2.connect(
        host="localhost",
        port="5432",
        database="postgres",
        user="postgres",
        password="102030"
    )


def save_user(name=None, email=None, senha=None):
    with get_connect() as conn:
        cur = conn.cursor()

        cur.execute("INSERT INTO cadastro (nome, email, senha) VALUES (%s, %s, %s);", (name, email, senha))
        conn.commit()

        return True


def get_table_carros():
    with get_connect() as conn:
        cur = conn.cursor(cursor_factory=DictCursor)

        cur.execute("SELECT * FROM carros")
        data = cur.fetchall()

    car = [x for x in data]

    return car




