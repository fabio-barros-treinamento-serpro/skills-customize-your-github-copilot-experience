# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Construir uma API REST simples com FastAPI para gerenciar tarefas, praticando rotas HTTP, modelos com Pydantic e codigos de status.

## 📝 Tasks

### 🛠️	Criar Endpoints Basicos

#### Descricao
Implemente uma API inicial para cadastro e listagem de tarefas usando uma estrutura em memoria.

#### Requisitos
O programa concluido deve:

- Criar uma aplicacao FastAPI no arquivo starter-code.py
- Implementar GET /health retornando {"status": "ok"}
- Implementar POST /tasks para criar uma tarefa com id, title e done
- Implementar GET /tasks para listar todas as tarefas cadastradas


### 🛠️	Completar CRUD e Validacoes

#### Descricao
Evolua a API para suportar consulta individual, atualizacao e remocao de tarefas, com tratamento de erros.

#### Requisitos
O programa concluido deve:

- Implementar GET /tasks/{task_id} com retorno 404 quando a tarefa nao existir
- Implementar PUT /tasks/{task_id} para atualizar title e done
- Implementar DELETE /tasks/{task_id} retornando status 204
- Usar modelos Pydantic para entrada e saida dos dados
- Retornar status 201 na criacao de novas tarefas