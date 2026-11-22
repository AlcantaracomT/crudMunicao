def executar_comando(sql, parametros=None, retornar_dados=False):
    raise NotImplementedError


def criar_tabela():
    sql = """
    CREATE TABLE IF NOT EXISTS municao (
        id SERIAL PRIMARY KEY,
        fabricante VARCHAR(50) NOT NULL,
        quantidade INT,
        codigo_lote VARCHAR(50)
    );
    """
    executar_comando(sql)

def add_municao(fabricante, quantidade, codigo_lote):
    sql = "INSERT INTO municao(fabricante, quantidade, codigo_lote) VALUES (%s, %s, %s);"
    executar_comando(sql, [fabricante, quantidade, codigo_lote])
