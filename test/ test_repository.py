from unittest.mock import patch
from municao import muni


def test_criar_tabela_executa_sql(mocker):
    mock_exec = mocker.patch("municao.muni.executar_comando")
    muni.criar_tabela()
    sql = mock_exec.call_args[0][0]
    assert "CREATE TABLE IF NOT EXISTS municao" in sql

def test_add_municao_insere_com_parametros(mocker):
    mock_exec = mocker.patch("municao.muni.executar_comando")
    muni.add_municao("CBC", 100, "LOTE1")
    sql, params = mock_exec.call_args[0]
    assert "INSERT INTO municao" in sql
    assert params == ["CBC", 100, "LOTE1"]

def test_ver_municao_retorna_lista(mocker):
    mocker.patch(
        "municao.muni.executar_comando",
        return_value=[(1, "CBC", 100, "LOTE1")],
    )
    linhas = muni.ver_municao()
    assert linhas == [(1, "CBC", 100, "LOTE1")]
