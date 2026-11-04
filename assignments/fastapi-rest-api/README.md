# 📘 Atividade: APIs REST com FastAPI

## 🎯 Objetivo

Construa uma API REST em Python com FastAPI para cadastrar e consultar livros, praticando rotas HTTP, parâmetros, modelos de dados e respostas de erro.

## 📝 Tarefas

### 🛠️ Implemente a listagem de livros

#### Descrição
Complete o endpoint de listagem no arquivo `starter-code.py`. Instale as dependências com `python -m pip install "fastapi[standard]"`, inicie a aplicação com `fastapi dev starter-code.py` e consulte a documentação interativa em `/docs`.

#### Requisitos
O programa concluído deve:

- Responder a `GET /books` com uma lista JSON de livros.
- Incluir `id`, `title` e `author` em cada livro retornado.
- Retornar uma lista vazia quando ainda não houver livros.
- Exibir o endpoint `GET /books` na documentação interativa em `/docs`.

### 🛠️ Consulte um livro pelo ID

#### Descrição
Implemente o endpoint que recebe o ID de um livro pela URL e procura esse livro na coleção mantida em memória.

#### Requisitos
O programa concluído deve:

- Responder a `GET /books/{book_id}` com o livro correspondente ao ID informado.
- Retornar o status HTTP `404` e uma mensagem de erro quando o ID não existir.
- Permitir testar os casos de sucesso e de ID inexistente pela documentação em `/docs`.

### 🛠️ Cadastre um livro

#### Descrição
Implemente `POST /books` para receber os dados de um livro, gerar um ID e armazenar o novo registro. Os dados ficam em memória e são reiniciados quando a aplicação é encerrada.

#### Requisitos
O programa concluído deve:

- Aceitar `title` e `author` no corpo da requisição usando o modelo `BookCreate`.
- Gerar um ID único e adicionar o livro à coleção.
- Retornar o livro criado com o status HTTP `201`.
- Rejeitar dados inválidos com a validação automática do FastAPI.