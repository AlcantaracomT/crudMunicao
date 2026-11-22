import pytest
from unittest.mock import MagicMock

from municao import muni


def test_criar_tabela_executa_sql(mocker):
    mock_exec = mocker.patch("municao.muni.executar_comando")
    muni.criar_tabela()

    sql = mock_exec.call_args.args[0]
    assert "CREATE TABLE IF NOT EXISTS municao" in sql


def test_add_municao_insere_com_parametros(mocker):
    mock_exec = mocker.patch("municao.muni.executar_comando")

    muni.add_municao("CBC", 100, "LOTE1")

    sql, params = mock_exec.call_args.args
    assert "INSERT INTO municao" in sql
    assert params == ["CBC", 100, "LOTE1"]


@pytest.mark.parametrize(
    ("fabricante", "quantidade", "lote"),
    [
        ("", 100, "LOTE1"),
        ("CBC", -1, "LOTE1"),
        ("CBC", 100, ""),
    ],
)
def test_add_municao_rejeita_dados_invalidos(mocker, fabricante, quantidade, lote):
    mock_exec = mocker.patch("municao.muni.executar_comando")

    with pytest.raises(ValueError):
        muni.add_municao(fabricante, quantidade, lote)

    mock_exec.assert_not_called()


def test_ver_municao_retorna_lista(mocker):
    mocker.patch(
        "municao.muni.executar_comando",
        return_value=[(1, "CBC", 100, "LOTE1")],
    )

    linhas = muni.ver_municao()

    assert linhas == [(1, "CBC", 100, "LOTE1")]


def test_atualiza_municao_envia_update(mocker):
    mock_exec = mocker.patch("municao.muni.executar_comando")

    muni.atualiza_municao("CBC", 50)

    sql, params = mock_exec.call_args.args
    assert "UPDATE municao" in sql
    assert params == [50, "CBC"]


def test_atualiza_municao_rejeita_quantidade_negativa(mocker):
    mock_exec = mocker.patch("municao.muni.executar_comando")

    with pytest.raises(ValueError):
        muni.atualiza_municao("CBC", -1)

    mock_exec.assert_not_called()


def test_deleta_municao_envia_delete(mocker):
    mock_exec = mocker.patch("municao.muni.executar_comando")

    muni.deleta_municao("LOTE1")

    sql, params = mock_exec.call_args.args
    assert "DELETE FROM municao" in sql
    assert params == ["LOTE1"]


def test_deleta_municao_rejeita_lote_vazio(mocker):
    mock_exec = mocker.patch("municao.muni.executar_comando")

    with pytest.raises(ValueError):
        muni.deleta_municao("")

    mock_exec.assert_not_called()


def test_executar_comando_execute_fetchall_e_fecha_conexao(mocker):
    cursor = MagicMock()
    cursor_context = MagicMock()
    cursor_context.__enter__.return_value = cursor

    connection = MagicMock()
    connection.__enter__.return_value = connection
    connection.cursor.return_value = cursor_context

    mocker.patch("municao.muni.psycopg2.connect", return_value=connection)
    cursor.fetchall.return_value = [(1, "CBC", 100, "LOTE1")]

    resultado = muni.executar_comando(
        "SELECT * FROM municao;",
        retornar_dados=True,
    )

    cursor.execute.assert_called_once_with("SELECT * FROM municao;", None)
    cursor.fetchall.assert_called_once_with()
    connection.__enter__.assert_called_once_with()
    connection.__exit__.assert_called_once()
    assert resultado == [(1, "CBC", 100, "LOTE1")]
