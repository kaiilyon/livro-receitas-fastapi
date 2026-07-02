 — Livro de Receitas (FastAPI + Supabase)

# 📖 Livro de Receitas — CRUD Full-Stack

Projeto desenvolvido como trabalho prático da disciplina **Tecnologias Emergentes**.

O sistema é uma aplicação web completa com CRUD, utilizando FastAPI no backend, HTML com Jinja2 no frontend e banco de dados PostgreSQL no Supabase.

---

## 🚀 Tecnologias utilizadas

- Python 3
- FastAPI
- SQLAlchemy (ORM)
- Jinja2 (templates HTML)
- Supabase (PostgreSQL na nuvem)
- HTML5 + CSS3
- Git / GitHub
- Codespaces (ambiente de desenvolvimento)

---

## 📌 Funcionalidades

- ✔ Criar receitas
- ✔ Listar receitas
- ✔ Editar receitas
- ✔ Excluir receitas
- ✔ Cadastro de categorias
- ✔ Relacionamento entre Receita e Categoria (FK)
- ✔ Interface web estilizada
- ✔ Dados persistidos no Supabase

---

## 🧠 Estrutura do projeto

```

├── main.py
├── database.py
├── models.py
├── templates/
│   ├── base.html
│   ├── form.html
│   └── lista.html
├── static/
│   └── style.css
├── pyproject.toml
├── uv.lock

````

---

## 🗃️ Banco de dados

O projeto utiliza o Supabase como banco PostgreSQL em nuvem.

### Tabelas:

- **categorias**
  - id (PK)
  - nome

- **receitas**
  - id (PK)
  - nome
  - ingredientes
  - modo_preparo
  - categoria_id (FK → categorias.id)

---

## 👥 Integrantes do grupo

- Emanuele  
- Kaylane  
- Dielson  

---

## 🎯 Objetivo

Este projeto tem como objetivo aplicar conceitos de:

- Desenvolvimento Web Full-Stack
- CRUD completo com persistência de dados
- Modelagem de banco de dados relacional
- Integração com banco de dados em nuvem (Supabase)
- Renderização de páginas HTML no servidor

---

## ⚙️ Como executar o projeto

```bash
uv sync
uv run fastapi dev main.py
```

Depois acesse:

```
http://127.0.0.1:8000
```

---

## 📷 Observação

Projeto desenvolvido em ambiente **GitHub Codespaces**, garantindo execução sem instalação local.
