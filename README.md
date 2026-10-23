# 🚀 API de Gestão de Pokémons - Projeto Final EBAC

API RESTful desenvolvida em **Python** utilizando **FastAPI** e **SQLAlchemy**, inspirada na conceituada PokeAPI. O projeto implementa um CRUD completo para o gerenciamento de registos de Pokémons, seguindo as melhores práticas de desenvolvimento backend, arquitetura modular, conteinerização com Docker e testes unitários automatizados.

---

## 🛠️ Tecnologias e Ferramentas Utilizadas

* **Linguagem:** Python 3.10+
* **Framework Web:** FastAPI
* **ORM:** SQLAlchemy
* **Validação de Dados:** Pydantic v2
* **Base de Dados:** PostgreSQL (Produção) / SQLite (Testes)
* **Conteinerização:** Docker & Docker Compose
* **Testes Unitários:** Pytest & TestClient
* **Versionamento:** Git

---

## 📂 Estrutura do Projeto

```text
projeto_final_ebac_40/
│
├── main.py              # Aplicação principal FastAPI e rotas do CRUD
├── database.py          # Configuração da sessão e conexão com a base de dados
├── models.py            # Definição do modelo de dados (Tabela PostgreSQL/SQLite)
├── schemas.py           # Esquemas de validação e serialização (Pydantic)
├── test_main.py         # Testes unitários automatizados
├── Dockerfile           # Configuração da imagem Docker da aplicação
├── docker-compose.yml   # Orquestração dos serviços (FastAPI + PostgreSQL)
├── requirements.txt     # Dependências do projeto
├── .env.example         # Exemplo de variáveis de ambiente
└── README.md            # Documentação detalhada do repositório

 
