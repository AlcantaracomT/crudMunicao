# CRUD de Munições

Aplicação de console desenvolvida em Python para cadastrar, consultar, atualizar
e excluir registros de munições em um banco PostgreSQL.

## Funcionalidades

- Criar a tabela de munições automaticamente
- Cadastrar fabricante, quantidade e código de lote
- Listar munições
- Atualizar quantidade por fabricante
- Excluir munições pelo código de lote
- Validar entradas vazias e quantidades negativas

## Tecnologias

- Python 3
- PostgreSQL
- psycopg2
- python-dotenv
- pytest e pytest-mock

## Pré-requisitos

- Python 3.10 ou superior
- PostgreSQL instalado e acessível
- Git

## Instalação

```bash
git clone https://github.com/AlcantaracomT/crudMunicao.git
cd crudMunicao
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

## Configuração do banco

Copie o modelo `.env.example` para `.env` e ajuste os valores:

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=municao
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```

Não envie arquivos `.env` ou credenciais para o repositório.

## Execução

```bash
.venv/bin/python main.py
```

Use as opções exibidas no menu para adicionar, visualizar, atualizar ou excluir
registros.

## Testes

```bash
.venv/bin/python -m pytest -q
```

Os testes automatizados ficam em `test/test_repository.py` e usam mocks para
não depender de uma conexão real ao banco.

## Documentação do código-fonte

Os módulos e funções possuem docstrings no padrão Pydoc.

Para visualizar a documentação no terminal:

```bash
.venv/bin/python -m pydoc municao.muni
.venv/bin/python -m pydoc municao.menu
```

Para gerar páginas HTML:

```bash
mkdir -p docs
.venv/bin/python -m pydoc -w main municao.muni municao.menu
mv -f main.html municao.muni.html municao.menu.html docs/
```

Abra `docs/municao.muni.html` no navegador para consultar a documentação da
camada de banco e `docs/municao.menu.html` para consultar o menu.

## Estrutura

```text
crudMunicao/
├── main.py
├── municao/
│   ├── muni.py
│   └── menu.py
├── test/
│   └── test_repository.py
├── requirements.txt
└── README.md
```

## Autor

Alcantara
