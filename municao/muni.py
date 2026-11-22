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

def ver_municao():
    sql = "SELECT id, fabricante, quantidade, codigo_lote FROM municao;"
    return executar_comando(sql, retornar_dados=True)

def atualiza_municao(fabricante, nova_quantidade):
    sql = "UPDATE municao SET quantidade = %s WHERE fabricante = %s;"
    executar_comando(sql, [nova_quantidade, fabricante])

def deleta_municao(codigo_lote):
    sql = "DELETE FROM municao WHERE codigo_lote = %s;"
    executar_comando(sql, [codigo_lote])