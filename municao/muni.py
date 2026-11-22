"""Acesso ao banco de dados PostgreSQL e operações CRUD de munições.

As funções deste módulo recebem dados validados pela camada de interface
ou pelas próprias operações e executam comandos SQL por meio de `executar_comando`.
"""

import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def _conexao():
    """Retorna as configurações de conexão obtidas das variáveis de ambiente."""
    return {
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "database": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASSWORD"),
    }


def executar_comando(sql, parametros=None, retornar_dados=False):
    """Executa um comando SQL e retorna linhas apenas em consultas.

    Args:
        sql: Comando SQL a ser executado.
        parametros: Valores substituídos nos placeholders `%s`.
        retornar_dados: Quando verdadeiro, retorna o resultado de `fetchall`.

    Returns:
        Lista de linhas para consultas ou `None` para demais comandos.
    """
    dados = None
    try:
        with psycopg2.connect(**_conexao()) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, tuple(parametros) if parametros else None)
                if retornar_dados:
                    dados = cur.fetchall()
    except psycopg2.Error as erro:
        print(f"Erro: {erro}")
    return dados


def criar_tabela():
    """Cria a tabela `municao` quando ela ainda não existe."""
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
    """Insere uma munição após validar os dados informados.

    Raises:
        ValueError: Quando fabricante ou lote estão vazios ou quantidade é negativa.
    """
    if not fabricante.strip():
        raise ValueError("Fabricante não pode ficar vazio")
    if quantidade < 0:
        raise ValueError("Quantidade não pode ser negativa")
    if not codigo_lote.strip():
        raise ValueError("Código do lote não pode ficar vazio")

    sql = "INSERT INTO municao(fabricante, quantidade, codigo_lote) VALUES (%s, %s, %s);"
    executar_comando(sql, [fabricante, quantidade, codigo_lote])

def ver_municao():
    """Retorna todas as munições cadastradas."""
    sql = "SELECT id, fabricante, quantidade, codigo_lote FROM municao;"
    return executar_comando(sql, retornar_dados=True)

def atualiza_municao(fabricante, nova_quantidade):
    """Atualiza a quantidade das munições de um fabricante.

    Raises:
        ValueError: Quando fabricante está vazio ou quantidade é negativa.
    """
    if not fabricante.strip():
        raise ValueError("Fabricante não pode ficar vazio")
    if nova_quantidade < 0:
        raise ValueError("Quantidade não pode ser negativa")

    sql = "UPDATE municao SET quantidade = %s WHERE fabricante = %s;"
    executar_comando(sql, [nova_quantidade, fabricante])

def deleta_municao(codigo_lote):
    """Remove munições pelo código do lote.

    Raises:
        ValueError: Quando o código do lote está vazio.
    """
    if not codigo_lote.strip():
        raise ValueError("Código do lote não pode ficar vazio")

    sql = "DELETE FROM municao WHERE codigo_lote = %s;"
    executar_comando(sql, [codigo_lote])