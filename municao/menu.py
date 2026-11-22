"""Interface de texto do CRUD de munições.

Este módulo apresenta o menu principal e encaminha as operações
para as funções de acesso ao banco no módulo `municao.muni`.
"""

from municao import muni


def menu():
    """Exibe as opções disponíveis no programa."""
    print("\n1. Adicionar\n2. Visualizar\n3. Atualizar\n4. Deletar\n5. Sair")


def main():
    """Inicializa a tabela e executa o ciclo principal do menu."""
    muni.criar_tabela()
    while True:
        menu()
        opcao = input("\nEscolha: ")

        match opcao:
            case '1':
                try:
                    muni.add_municao(
                        input("Fabricante: "),
                        int(input("Quantidade: ")),
                        input("Lote: "),
                    )
                except (ValueError, TypeError) as erro:
                    print(f"Erro: {erro}")
            case '2':
                linhas = muni.ver_municao() or []
                for l in linhas:
                    print(f"ID: {l[0]} | Fab: {l[1]} | Qtd: {l[2]} | Lote: {l[3]}")
            case '3':
                try:
                    muni.atualiza_municao(
                        input("Fabricante: "), int(input("Nova qtd: "))
                    )
                except (ValueError, TypeError) as erro:
                    print(f"Erro: {erro}")
            case '4':
                try:
                    muni.deleta_municao(input("Lote: "))
                except (ValueError, TypeError) as erro:
                    print(f"Erro: {erro}")
            case '5':
                break
            case _:
                print("Opção inválida")