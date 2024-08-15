# Gerenciamento de Pacientes

Este projeto é uma aplicação web que permite o gerenciamento de informações sobre pacientes e suas visitas médicas. O sistema utiliza Flask como framework web e SQLAlchemy para interagir com um banco de dados PostgreSQL.

## Funcionalidades

- Adicionar pacientes com informações como nome, data de nascimento e sexo.
- Registrar visitas médicas para cada paciente.
- Recuperar informações sobre pacientes e suas visitas.

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados:

- Python 3.x
- PostgreSQL

## Instalação

1. Clone o repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DA_PASTA_DO_REPOSITORIO>

3. Instale as dependências:

   ```bash
   pip install Flask Flask-SQLAlchemy marshmallow requests xmltodict psycopg2

4. Crie o banco de dados no PostgreSQL e configure a URI de conexão no arquivo config.py:
   
   ```bash
   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://usuario:senha@localhost/nome_do_banco')

6. Inicialize o banco de dados executando o script:

   ```bash
   python init_db.py

## Como Rodar o Servidor

   ```
   python -m app.main
   ```


## Como Rodar o Cliente

   ```
   python -m cliente.cliente
   ```

## Testes

O projeto inclui testes automatizados para garantir que a aplicação funcione conforme o esperado. Os testes são realizados utilizando a biblioteca [pytest](https://docs.pytest.org/en/stable/).


### Executando os Testes

Para rodar os testes, siga os seguintes passos:

1. **Instale as Dependências**: 

Certifique-se de que todas as dependências estão instaladas. Você pode usar o seguinte comando:
   
    ```
    pip install -r requirements.txt
    ```
    

2. **Execute os Testes**: 

Utilize o seguinte comando para executar os testes:

    ```
    pytest
    ```

Os resultados dos testes serão exibidos no terminal. Todos os testes devem passar para garantir que a aplicação está funcionando corretamente.


## Estrutura do Projeto

```/projeto
├── /app
│ ├── init.py
│ ├── config.py
│ ├── main.py
│ ├── /models
│ │ ├── init.py
│ │ ├── paciente.py
│ │ └── visitas.py
│ ├── /repositories
│ │ ├── init.py
│ │ ├── paciente_repository.py
│ │ └── visitas_repository.py
│ ├── /routes
│ │ ├── init.py
│ │ ├── paciente_routes.py
│ │ └── visitas_routes.py
│ └── /schemas
│ ├── init.py
│ ├── paciente_schema.py
│ └── visitas_schema.py
├── /cliente
│ └── cliente.py
├── /tests
│ ├── init.py
│ ├── conftest.py
│ ├── test_conversion.py
└── init_db.py
