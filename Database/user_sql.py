import psycopg2

from psycopg2.extras import DictCursor


def get_connect():
    return psycopg2.connect(
        host="host.docker.internal",
        port="5432",
        database="postgres",
        user="postgres",
        password="102030",
        connect_timeout=3
    )


def save_user(name=None, email=None, senha=None):

    with get_connect() as conn:
        cur = conn.cursor()
        select = f"INSERT INTO public.cadastro (nome, email, senha) VALUES ('{name}', '{email}', '{senha}');"
        cur.execute(select)
        conn.commit()

        return True


def get_table_carros():
    with get_connect() as conn:
        cur = conn.cursor(cursor_factory=DictCursor)

        cur.execute("SELECT * FROM carros")
        data = cur.fetchall()

    car = [x for x in data]

    return car


def get_dados_vadildate():
    with get_connect() as conn:
        cur = conn.cursor(cursor_factory=DictCursor)
        cur.execute(f"SELECT nome from public.cadastro;")
        dados = cur.fetchall()
        print(dados)
