# Mapeamento Objeto-Relacional com SQLAlchemy

## Introdução

O SQLAlchemy é uma biblioteca popular em Python para interagir com bancos de dados relacionais. Ele fornece uma interface de ORM (Object-Relational Mapping) que permite que os desenvolvedores trabalhem com dados de um banco de dados utilizando objetos Python, ao invés de escrever consultas SQL diretamente. Este trabalho discente tem como objetivo desenvolver um mapeamento objeto-relacional utilizando o SQLAlchemy.

## Objetivo

O objetivo deste trabalho é realizar o mapeamento objeto-relacional utilizando o SQLAlchemy. O aluno irá criar um pequeno projeto onde desenvolverá um modelo de dados, configurará uma conexão com um banco de dados, e implementará operações básicas de CRUD (Create, Read, Update, Delete) utilizando o SQLAlchemy.

## Requisitos

### Ambiente de Desenvolvimento

- **Python 3.x**
- **SQLAlchemy**
- **Banco de dados relacional** (SQLite, MySQL, MariaDB, entre outros)

### Bibliotecas

- **SQLAlchemy**: Instale com `pip install sqlalchemy`
- **Driver específico para o banco de dados**:
  - Para SQLite, não é necessário instalar drivers adicionais.
  - Para MySQL, instale o driver: `pip install mysql-connector-python` (caso opte por MySQL).

### Banco de Dados

- **Entidades**: Mínimo 4 entidades
- **Atributos**: A escolha dos atributos fica a critério do estudante para criar um problema relevante.

## Documentação

### Introdução

O projeto visa criar um modelo de dados utilizando SQLAlchemy para realizar operações básicas de CRUD em um banco de dados relacional. O modelo será composto por quatro entidades principais e suas respectivas operações de inserção, consulta, atualização e exclusão de registros.

### Descrição das Entidades e Atributos

1. **Clientes**
   - **Tabela**: `users`
   - **Atributos**:
     - `id`: Identificador único do cliente (Integer)
     - `nome`: Nome do cliente (String)
     - `comida_favorita`: Comida favorita do cliente (String)
     - `idade`: Idade do cliente (Integer)
     - `dia_todo_mes_recebe`: Dia do mês em que o cliente recebe a entrega (Integer)
     - `endereco_completo`: Endereço completo do cliente (String)

2. **Estoque**
   - **Tabela**: `alimento_que_recebe`
   - **Atributos**:
     - `id`: Identificador único do item no estoque (Integer)
     - `comida_estoque`: Nome do item no estoque (String)
     - `quantidade`: Quantidade disponível do item (Integer)

3. **Entrega**
   - **Tabela**: `batatinha_em_casa`
   - **Atributos**:
     - `id`: Identificador único da entrega (Integer)
     - `cliente_id`: Identificador do cliente (Integer, ForeignKey)
     - `data_entrega_escolhida`: Data de entrega escolhida (Integer)
     - `endereco_entrega`: Endereço da entrega (String)

4. **Fornecedor**
   - **Tabela**: `fornecedores`
   - **Atributos**:
     - `id`: Identificador único do fornecedor (Integer)
     - `nome_empresa`: Nome da empresa fornecedora (String)
     - `telefone_empresa`: Telefone da empresa (String)
     - `endereco_empresa`: Endereço da empresa (String)
     - `cidade_empresa`: Cidade da empresa (String)
     - `estado_empresa`: Estado da empresa (String)
     - `cep_empresa`: CEP da empresa (String)

### Modelo Conceitual

![Modelo Conceitual](path_to_your_diagram.png)

### Implementação em Python
