# Sistema de Agendamento de Salas - SES-PE 🏥

Sistema web institucional para gerenciamento e reserva de salas de reunião, desenvolvido para a Secretaria de Saúde do Estado de Pernambuco.

![Status do Projeto](https://img.shields.io/badge/Status-Em_Produção-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey)

## 📋 Funcionalidades

### 🔐 Autenticação e Segurança
- **Login Seguro:** Proteção de rotas com `Flask-Login`.
- **Níveis de Acesso:**
  - **Usuário Padrão:** Pode reservar, visualizar suas reservas e editar seu perfil.
  - **Administrador:** Gerencia salas, usuários, cancela qualquer reserva e visualiza relatórios.
- **Criptografia:** Senhas armazenadas com hash seguro (`werkzeug.security`).
- **CSRF Protection:** Proteção contra ataques Cross-Site Request Forgery.

### 📅 Gestão de Reservas
- **Dashboard Interativo:** Visão em tempo real das salas (Ocupadas/Disponíveis).
- **Recorrência:** Agendamentos **Semanais**, **Quinzenais** e **Mensais**.
- **Resiliência a Conflitos:** O sistema detecta conflitos em séries recorrentes e agenda apenas os dias livres, avisando o usuário sobre os dias ocupados.
- **Validação de Fuso Horário:** Todo o sistema opera no fuso `America/Recife`, garantindo precisão independente do servidor.
- **Cancelamento Inteligente:** Opção de cancelar apenas uma ocorrência ou toda a série de repetição.

### 🏢 Administração
- **Gestão de Salas:** Cadastro, edição, exclusão e reordenação (drag-and-drop) de salas.
- **Gestão de Usuários:** Criação e remoção de usuários e administradores.

## 🛠️ Tecnologias Utilizadas

- **Backend:** Python 3.12 + Flask
- **Banco de Dados:** SQLAlchemy (PostgreSQL em Produção / SQLite Local)
- **Frontend:** HTML5, Tailwind CSS (via CDN), JavaScript
- **Deploy:** Render.com

## 🚀 Como Rodar o Projeto

### Pré-requisitos
- Python 3.12+
- Git

### Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Williams-Sobrinho/sistema_agendamento.git
   cd sistema_agendamento
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente (Opcional):**
   Crie um arquivo `.env` ou exporte as variáveis:
   ```bash
   export FLASK_APP=run.py
   export SECRET_KEY='sua-chave-secreta'
   ```

5. **Execute a aplicação:**
   ```bash
   python run.py
   ```
   Acesse em: `http://localhost:5000`

## ☁️ Deploy no Render

O projeto está configurado para deploy automático no Render.

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `gunicorn run:app`
- **Variáveis de Ambiente Necessárias:**
  - `DATABASE_URL`: URL de conexão interna do PostgreSQL.
  - `SECRET_KEY`: Chave aleatória forte.
  - `PYTHON_VERSION`: `3.12.8`

## 📂 Estrutura do Projeto

```text
sistema_reunião/
├── app/
│   ├── __init__.py        # Factory Application
│   ├── models.py          # Modelos do Banco de Dados
│   ├── routes/            # Rotas (Auth, Main, Admin)
│   ├── templates/         # Páginas HTML
│   ├── static/            # Arquivos Estáticos (CSS, Img)
│   └── utils/             # Helpers e Utilitários
├── run.py                 # Ponto de entrada da aplicação
├── requirements.txt       # Dependências
└── patch_db.py            # Scripts de manutenção de banco
```

## 📄 Licença

Este projeto é de uso exclusivo da Secretaria de Saúde de Pernambuco.

---
Desenvolvido por **Williams Sobrinho**.
