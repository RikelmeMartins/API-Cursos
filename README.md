API Flask - Gerenciamento de Cursos e Professores

API REST desenvolvida com Flask para gerenciamento de usuários, professores, cursos e formações.

O projeto utiliza uma estrutura organizada em camadas, separando Entidades, Models, Schemas, Services e Views, facilitando a manutenção, organização e evolução da aplicação.

🚀 Tecnologias utilizadas

Python

Flask

Flask-RESTful

Flask-SQLAlchemy

SQLAlchemy

Flask-Marshmallow

Marshmallow

Flask-JWT-Extended

Passlib

Flask-Migrate

Alembic

Banco de dados relacional

📁 Estrutura do projeto

APIFlask/
│
├── api/
│   │
│   ├── entidades/
│   │   ├── __init__.py
│   │   ├── curso.py
│   │   ├── formacao.py
│   │   ├── professor.py
│   │   └── usuario.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── curso_model.py
│   │   ├── formacao_model.py
│   │   ├── professor_formacao_model.py
│   │   ├── professor_model.py
│   │   └── usuario_model.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── curso_schema.py
│   │   ├── formacao_schema.py
│   │   ├── login_schema.py
│   │   ├── professor_schema.py
│   │   └── usuario_schema.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── curso_service.py
│   │   ├── formacao_service.py
│   │   ├── professor_service.py
│   │   └── usuario_service.py
│   │
│   ├── views/
│   │   ├── __init__.py
│   │   ├── curso_views.py
│   │   ├── formacao_views.py
│   │   ├── login_views.py
│   │   ├── professor_views.py
│   │   └── usuario_views.py
│   │
│   ├── __init__.py
│   └── paginate.py
│
├── migrations/
├── postman/
├── .env
├── .gitignore
├── config.py
└── run.py

🏗️ Organização da aplicação

O projeto utiliza separação de responsabilidades em diferentes camadas:

Entidades: representam os objetos e dados utilizados pela aplicação.

Models: representam as tabelas e relacionamentos do banco utilizando SQLAlchemy.

Schemas: validam e serializam os dados de entrada e saída.

Services: concentram as regras de negócio e o acesso aos Models.

Views: recebem as requisições HTTP e retornam as respostas da API.

Entidades

A pasta entidades contém as classes utilizadas para representar os dados que circulam pela aplicação.

As principais entidades são:

Usuário

Professor

Curso

Formação

Essa camada ajuda a separar a representação dos dados das classes responsáveis diretamente pela persistência no banco de dados.

Models

A pasta models contém as classes responsáveis pela representação das tabelas do banco de dados.

Os Models utilizam SQLAlchemy para realizar o mapeamento objeto-relacional.

Entre os principais Models estão:

Usuário

Professor

Curso

Formação

Relacionamento entre Professor e Formação

Schemas

A pasta schemas é responsável pela validação, serialização e desserialização dos dados enviados e recebidos pela API.

São utilizados Schemas para:

Usuários

Login

Professores

Cursos

Formações

Services

A camada services contém as regras de negócio e operações relacionadas ao banco de dados.

Essa separação evita colocar toda a lógica diretamente nas rotas.

Fluxo simplificado:

Cliente / Postman
       ↓
     Views
       ↓
    Schemas
       ↓
   Services
       ↓
 Models / Entidades
       ↓
Banco de Dados

Views

A pasta views contém os endpoints da API.

As Views recebem as requisições HTTP, validam os dados através dos Schemas e utilizam os Services para executar as operações necessárias.

🔐 Autenticação

A API possui sistema de autenticação utilizando JWT.

O usuário informa seu e-mail e senha:

{
    "email": "usuario@email.com",
    "senha": "123456"
}

Após a validação das credenciais, a API gera um access_token.

Exemplo:

{
    "access_token": "token_jwt"
}

Esse token pode ser utilizado posteriormente para acessar rotas protegidas.

🔒 Segurança das senhas

As senhas não são armazenadas diretamente no banco de dados.

O projeto utiliza a biblioteca Passlib com o algoritmo:

pbkdf2_sha256

Exemplo de geração do hash:

from passlib.hash import pbkdf2_sha256

self.senha = pbkdf2_sha256.hash(self.senha)

Para verificar a senha durante o login:

pbkdf2_sha256.verify(senha, self.senha)

Dessa forma, a senha original do usuário não precisa ser armazenada no banco.

👤 Usuários

A API permite o gerenciamento de usuários.

Principais operações:

Criar usuário

Listar usuários

Buscar usuário

Atualizar usuário

Excluir usuário

Realizar login

Gerar token JWT

👨‍🏫 Professores

O módulo de professores permite cadastrar e gerenciar os professores da aplicação.

Entre as informações que podem ser relacionadas estão:

Nome

Dados pessoais

Cursos

Formações

🎓 Cursos

A API possui endpoints para gerenciamento dos cursos.

Operações disponíveis:

Cadastrar curso

Listar cursos

Buscar curso

Atualizar curso

Excluir curso

📚 Formações

Também é possível cadastrar as formações acadêmicas dos professores.

Exemplos:

Graduação

Especialização

Mestrado

Doutorado

O projeto possui um Model específico para realizar o relacionamento entre professores e formações.

🔗 Relacionamentos

O sistema trabalha com relacionamentos entre entidades utilizando SQLAlchemy.

Exemplo conceitual:

Professor
    │
    ├── Curso
    │
    └── Formação

O relacionamento entre professor e formação pode utilizar uma tabela associativa, permitindo que um professor possua diversas formações.

📄 Paginação

O projeto possui suporte a paginação através do arquivo:

paginate.py

Isso permite retornar grandes quantidades de registros de maneira organizada.

Exemplo:

GET /professores?page=1

🗄️ Banco de dados

A persistência dos dados é realizada utilizando SQLAlchemy.

As alterações na estrutura do banco são controladas através de migrations utilizando:

Flask-Migrate

Alembic

🔄 Migrations

Para criar uma nova migration:

flask db migrate -m "Descrição da alteração"

Aplicar as alterações no banco:

flask db upgrade

Caso seja necessário voltar uma migration:

flask db downgrade

⚙️ Configuração do ambiente

Clone o repositório:

git clone <URL_DO_REPOSITORIO>

Entre na pasta:

cd APIFlask

Crie um ambiente virtual:

python -m venv .venv

Ative o ambiente virtual.

Linux

source .venv/bin/activate

Windows

.venv\Scripts\activate

📦 Instalação das dependências

Instale as bibliotecas necessárias:

pip install flask
pip install flask-restful
pip install flask-sqlalchemy
pip install flask-marshmallow
pip install marshmallow
pip install flask-jwt-extended
pip install passlib
pip install flask-migrate

Ou, caso o projeto possua requirements.txt:

pip install -r requirements.txt

Para gerar o arquivo requirements.txt:

pip freeze > requirements.txt

🔑 Variáveis de ambiente

O projeto utiliza um arquivo .env para armazenar informações que não devem ficar diretamente no código.

Exemplo:

SECRET_KEY=sua_chave_secreta
JWT_SECRET_KEY=sua_chave_jwt
DATABASE_URI=sua_url_do_banco

O arquivo .env não deve ser enviado para o GitHub.

Por isso, ele deve estar presente no .gitignore.

Exemplo:

.env
.venv/
__pycache__/
*.pyc

▶️ Executando o projeto

Com o ambiente virtual ativado:

python run.py

A API ficará disponível normalmente em:

http://127.0.0.1:5000

🧪 Testando a API

Os endpoints podem ser testados utilizando ferramentas como:

Postman

Insomnia

Thunder Client

O projeto também possui uma pasta:

postman/

que pode ser utilizada para armazenar coleções de testes da API.

📌 Exemplo de fluxo de login

Cliente
   │
   │ POST /login
   ▼
LoginView
   │
   │ valida os dados
   ▼
LoginSchema
   │
   ▼
UsuarioService
   │
   │ busca pelo email
   ▼
Usuario
   │
   │ verifica senha com Passlib
   ▼
JWT
   │
   │ gera access_token
   ▼
Cliente

🎯 Objetivo do projeto

O objetivo deste projeto é aplicar conceitos de desenvolvimento de APIs REST com Python e Flask, utilizando boas práticas de organização de código e separação de responsabilidades.

Durante o desenvolvimento são aplicados conceitos como:

API REST

CRUD

Programação Orientada a Objetos

Arquitetura em camadas

ORM

Relacionamentos entre tabelas

Serialização

Validação de dados

Autenticação JWT

Hash de senhas

Migrations

Paginação

👨‍💻 Autor

Rikelme Martins

Projeto desenvolvido para estudo e prática de desenvolvimento Back-end utilizando Python e Flask.