
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


def save_user(nome, email, telefone, endereco):
    with get_connect() as conn:

        cur = conn.cursor(cursor_factory=DictCursor)
        select = f"insert into postgres.compras.clientes (nome, email, telefone, endereco) " \
                 f"values ('{nome}', '{email}', '{telefone}', '{endereco}')"
        cur.execute(select)
        conn.commit()

    return True


def get_list_clientes():
    with get_connect() as conn:
        cur = conn.cursor(cursor_factory=DictCursor)
        cur.execute(f"select c.nome from postgres.compras.clientes c")
        dados = cur.fetchall()
        data = []
        [data.append(i.get("nome")) for i in dados]

    return rows_dict_clientes(data)


def get_estoque(produtos=False, id=None):
    with get_connect() as conn:
        cur = conn.cursor(cursor_factory=DictCursor)
        if produtos:
            cur.execute(f"SELECT p.id_produto, p.nome_produto, p.quantidade_estoque "
                        f"FROM compras.produtos p where id_produto ={id}")
            dados = cur.fetchall()
            dict_dados = [dict({
                "dados": rows_dict_produtoas([i for i in dados])
            })]
            print([i for i in dados])
    return dict_dados


def dados_json_bd():
    with get_connect() as conn:
        cur = conn.cursor(cursor_factory=DictCursor)
        select = f"select * from postgres.compras.dados_json_items "
        cur.execute(select)
        nota = cur.fetchall()
        print(nota)
        dados_js = [i for i in nota]
        lista2 = []
        for i in dados_js:
            lista2.append(i)
        for i in range(len(lista2)):
            # rows = rows_dados_da_nota(lista2[i][0],lista2[i][0][1], lista2[i][0][2], lista2[i][0][3],lista2[i][0][4])

            rows1 = rows_dados_da_nota(lista2[i][1][0],lista2[i][1][1], lista2[i][1][2], lista2[i][1][3],lista2[i][1][4])

    return dict({
        # "1": rows,
        "2": rows1
    })


def rows_dados_da_nota(id, produto, qtd_estoque, qtd, nome):
    return dict(
        {
            "id": f'{id}',
            "nome_produto": f"{produto}",
            "quantidade_em_estoque": qtd_estoque,
            "quantidade": qtd,
            "nome_usuario":f"{nome}"
        }
    )


def rows_dict_produtoas(row):
    return dict({
        "nome_produtos": row
    })


def rows_dict_clientes(row):
    return dict({
        "lista_de_nomes": row
    })
