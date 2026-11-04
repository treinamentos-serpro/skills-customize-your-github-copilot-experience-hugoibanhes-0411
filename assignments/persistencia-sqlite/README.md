# 📘 Atividade: Persistência de Dados com SQLite

## 🎯 Objetivo

Use Python e SQLite para armazenar livros em um banco de dados que continua disponível depois que o programa é encerrado. Você vai criar uma tabela, inserir registros e consultar os dados usando SQL.

## 📝 Tarefas

### 🛠️ Crie a tabela de livros

#### Descrição
Complete a função `create_table` em `starter-code.py` para criar a tabela `books` no banco de dados SQLite. Cada livro deve ter um ID, título e autor. Execute o programa mais de uma vez para confirmar que a tabela pode ser criada sem apagar os dados existentes.

#### Requisitos
O programa concluído deve:

- Criar a tabela `books` com as colunas `id`, `title` e `author`.
- Usar o ID como chave primária gerada pelo SQLite.
- Usar `CREATE TABLE IF NOT EXISTS` para não falhar se a tabela já existir.

### 🛠️ Cadastre livros

#### Descrição
Complete `add_book` para inserir um livro no banco. Use os espaços reservados `?` do SQLite para passar os valores separadamente do comando SQL.

#### Requisitos
O programa concluído deve:

- Inserir o título e o autor recebidos pela função.
- Usar parâmetros SQL em vez de montar o comando com concatenação de strings.
- Salvar a alteração para que o livro continue no banco após o programa terminar.

### 🛠️ Consulte os livros cadastrados

#### Descrição
Complete `list_books` para consultar e exibir todos os livros, incluindo o ID. Depois, complete `find_book` para procurar um livro pelo ID e informar quando nenhum registro corresponder à busca.

#### Requisitos
O programa concluído deve:

- Exibir todos os livros com ID, título e autor.
- Buscar um livro pelo ID usando um parâmetro SQL.
- Informar claramente quando o banco ainda não tiver livros ou quando o ID não existir.
- Fechar a conexão com o banco ao terminar a execução.