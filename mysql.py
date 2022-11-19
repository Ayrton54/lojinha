import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conctar():
    cur = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='clientes',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield cur
    finally:

        cur.close()

# adicionando clientes a tabela
'''with conctar() as cur:
    with cur.cursor() as cursor:
        sql = 'INSERT INTO clientes(nome,sobrenome,idade,peso)VALUES(%s,%s,%s,%s)'
        dados=[
            ('jenifer','silva',25,70),
            ('jessica', 'limma', 25, 78),
            ('junior', 'pereira', 25, 100.80),
        ]

        cursor.executemany(sql, dados)
        cur.commit()'''
# deletando dados de um em um
'''with conctar() as cur:
    with cur.cursor() as cursor:
        sql = ('DELETE FROM clientes WHERE id =%s')
        cursor.execute(sql,(6,))
        cur.commit()'''
# deletando e, cadeia
'''with conctar() as cur:
    with cur.cursor() as cursor:
        sql = ('DELETE FROM clientes WHERE id BETWEEN %s and %s')
        cursor.execute(sql,(5,8))
        cur.commit()
'''
#editando dados
'''with conctar() as cur:
    with cur.cursor() as cursor:
        sql ='UPDATE clientes SET nome=%s WHERE id=%s'
        cursor.execute(sql,('GOKU',5))
        cur.commit()'''

with conctar() as cur:
    with cur.cursor() as cursor:
        cursor.execute('SELECT * FROM clientes LIMIT 100')
        res = cursor.fetchall()

        for linha in res:
            print(linha)
