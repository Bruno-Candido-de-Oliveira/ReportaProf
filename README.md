# Para inicializar o back-end:

Após baixar e extrair os arquivos do projeto em uma pasta, no terminal, siga os seguintes passos:

- 1 - Criar a variável de ambiente "python -m venv venv"
- 2 - Inicializar a variável de ambiente "venv\Scripts\activate"
- 3 - Instalar as dependências "pip install -r requirements.txt"
- 4 - Inicializar a aplicação "python manage.py runserver"

OBS.: É necessário ter o Python instalado em sua máquina.

Usuários disponíveis:

Administrador em http://127.0.0.1:8000/admin/
- Usuário: Admin
- Senha: admin

Professores em http://127.0.0.1:8000/auth/token/
- Usuário: BrunoCandido Senha: professor123
- Usuário: Pasquale Senha: professor123
- Usuário: Girafales Senha: professor123
- Usuário: Pardal Senha: professor123

Visualização das rotas em: http://127.0.0.1:8000/swagger/
