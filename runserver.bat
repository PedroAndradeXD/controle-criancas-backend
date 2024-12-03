@echo off
REM Caminhos relativos ao diretório do script
SET SCRIPT_DIR=%~dp0
SET BACKEND_DIR=%SCRIPT_DIR%controle-criancas-backend
SET FRONTEND_DIR=%SCRIPT_DIR%controle-de-criancas-frontend\controle-criancas-front

REM Porta e endereço para o frontend
SET FRONTEND_PORT=5173
SET FRONTEND_URL=http://localhost:%FRONTEND_PORT%

REM Ativa o ambiente virtual
CALL "%BACKEND_DIR%\venv\Scripts\Activate"

REM Exibe uma mensagem inicial
echo Iniciando os servidores do frontend e backend...

REM Inicia o servidor do frontend
START cmd.exe /C "cd /D %FRONTEND_DIR% && npm run dev"
echo Servidor do frontend iniciado.

REM Inicia o servidor do backend
START cmd.exe /C "cd /D %BACKEND_DIR% && python manage.py runserver"
echo Servidor do backend iniciado.

REM Abrir o navegador no endereço do frontend
START %FRONTEND_URL%

REM Mensagem final
echo Ambos os servidores foram iniciados. Verifique os terminais abertos para mais informações.
PAUSE
