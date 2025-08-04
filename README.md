# Projeto: Gerenciamento de Usuários com SQLAlchemy + PostgreSQL

Este projeto Python utiliza SQLAlchemy para comunicação com um banco de dados PostgreSQL, com suporte ao uso de variáveis de ambiente via `.env`, versionamento Git com boas práticas, gerenciamento de dependências com `pip freeze`, e automação via `pre-commit`.

## 🚀 Começando

### 📁 Estrutura Inicial do Projeto

```
.
├── infra/
│   ├── configs/
│   │   └── connection.py
│   ├── entities/
│   │   └── user.py
│   └── repository/
│       └── user_repository.py
├── run.py
├── .env
├── .gitignore
├── .pre-commit-config.yaml
├── requirements.txt
├── README.md
└── .venv/
```

---

## ⚙️ Passo a passo para iniciar o projeto

### 1) Iniciando um git (versionamento)

No terminal ubuntu linux (shell) escreva:

```bash
git init
```

### 2) Criar um .gitignore

```bash
touch .gitignore
```

**Dentro do .gitignore, escrever os arquivos a serem ignorados:**

```
**/__pycache__
.pytest_cache
.env
.venv
```

```bash
git add .gitignore
git commit -m 'config: Starting project with .gitignore'
```

---

### 3) Criando um ambiente virtual em python (Ubuntu 22.04)

```bash
python3 -m venv .venv
```

### 4) Ativando o ambiente criado (Ubuntu 22.04)

```bash
source .venv/bin/activate
```

### OBS: Caso o .venv esteja sendo rastreado pelo git

```bash
git rm -r --cached .venv
git status
```

### 5) Add modificações no git

```bash
git add .gitignore
git commit -m 'config: Adding .venv to .gitignore'
```

---

### 6) Criando arquivo requirements.txt e passando as dependências para ele (Ubuntu 22.04)

```bash
.venv/bin/pip freeze > requirements.txt
```

---

### 7) Instalar todas as dependências do projeto (Ubuntu 22.04)

```bash
.venv/bin/pip install -r requirements.txt
```

---

### 8) Automatizando a atualização do requirements.txt sempre que um commit for realizado

#### Instalar pre-commit:

```bash
pip install pre-commit
```

#### Criar o arquivo .pre-commit-config.yaml

```bash
touch .pre-commit-config.yaml
```

**Conteúdo do arquivo:**

```yaml
repos:
  - repo: local
    hooks:
      - id: requirements
        name: requirements
        entry: bash -c '.venv/bin/pip freeze > requirements.txt; git add requirements.txt'
        language: system
        pass_filenames: false
        stages: [commit]
```

#### Subir o hook:

```bash
pre-commit migrate-config
```

---

### 9) Adicionar e comitar o arquivo de configuração do pre-commit

```bash
git add .pre-commit-config.yaml
git commit -m 'config: Adding pre-commit to project'
```

---

### 10) Adicionar e comitar este próprio arquivo de orientação (por exemplo, `informacao/code_init.txt`)

```bash
git add code_init.txt
git commit -m 'config: Add arquivo de orientação para configuração do projeto inicial (git, venv, requirements, automatizando pre-commit, criando db postgresql)'
```

---

### 11) Para deixar salvo senhas entre outras informações importantes no código

#### 11.1 Criar um arquivo .env

```bash
touch .env
```

**Conteúdo do arquivo .env:**

```env
DB_USER=zarzar
DB_PASS=my_pass
DB_HOST=localhost
DB_PORT=5432
DB_NAME=db_praia
```

#### 11.2 Usar python-dotenv para carregar as variáveis

```bash
pip install python-dotenv
```

#### 11.3 Exemplo no código python

```python
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis do .env

user = os.getenv("DB_USER")
password = os.getenv("DB_PASS")
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
dbname = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

engine = create_engine(DATABASE_URL)
```

---

### 12) Tipos de tags para commits (git)

| Prefixo   | Significado                                                             |
|-----------|-------------------------------------------------------------------------|
| `feat`    | Nova funcionalidade                                                     |
| `fix`     | Correção de bug                                                         |
| `docs`    | Mudança apenas em documentação                                          |
| `style`   | Formatação (sem alteração de lógica)                                    |
| `refactor`| Refatoração sem alteração de comportamento                              |
| `test`    | Adição ou ajustes em testes                                             |
| `chore`   | Mudanças que não afetam o código de produção                            |
| `config`  | Alterações em arquivos de configuração (.env, .gitignore, etc)          |

---

## ✅ Checklist de boas práticas

- [x] Uso de `.env` para variáveis sensíveis
- [x] Estrutura modular (config, entidades, repositórios)
- [x] Versionamento com Git e `.gitignore`
- [x] Ambiente virtual isolado com `venv`
- [x] Dependências rastreadas com `requirements.txt`
- [x] Automação com `pre-commit`

---
