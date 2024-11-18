# Controle de Check-in e Check-out de Crianças - Backend

Este projeto é um sistema de backend para controle de check-in e check-out de crianças em uma igreja, desenvolvido com Django.

## Requisitos

- Python 3.12
- Git (para clonar o repositório)
- Virtualenv (opcional, mas recomendado para o ambiente virtual)

## Instruções de Configuração e Execução

### 1. Clonar o Repositório

Primeiro, crie um fork do repositório e, após isso, clone seu fork para sua máquina local:

```bash
git clone https://github.com/SeuUsuario/controle-criancas-backend.git
cd controle-criancas-backend
```
### 2. Criar e Ativar o Ambiente Virtual
É recomendado criar um ambiente virtual para isolar as dependências do projeto. Para criar e ativar o ambiente virtual, execute:

```bash
python -m venv venv
```
Ative o ambiente virtual:

* Windows:
```bash
.\venv\Scripts\Activate
```

* Linux/Mac:
```bash
source venv/bin/activate
```

### 3. Instalar as Dependências
Com o ambiente virtual ativado, instale as dependências do projeto:
```bash
pip install -r requirements.txt
```

### 4. Configuração do Banco de Dados
O projeto usa um banco de dados SQLite por padrão, que será criado automaticamente ao rodar as migrações. Para configurar o banco de dados, aplique as migrações do Django:
```bash
python manage.py migrate
```

### 5. Criar um Superusuário
Para acessar o painel administrativo do Django, crie um superusuário:
```bash
python manage.py createsuperuser
```

### 6. Executar o Servidor de Desenvolvimento
Agora, inicie o servidor de desenvolvimento do Django:
```bash
python manage.py runserver
```

O servidor estará disponível em http://127.0.0.1:8000/.
