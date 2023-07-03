
import psycopg2

from psycopg2.extras import DictCursor


def get_connect():
    return psycopg2.connect(
        host="192.168.0.7",
        port="5432",
        database="postgres",
        user="postgres",
        password="102030"
    )


def get_carros():
    with get_connect() as conn:
        cur = conn.cursor(cursor_factory=DictCursor)

        cur.execute("SELECT * FROM carros")
        data = cur.fetchall()

    car = [x for x in data]

    return car




