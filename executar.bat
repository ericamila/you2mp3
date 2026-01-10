@echo off
:: Navega para a pasta do script (opcional, se o .bat estiver na mesma pasta)
cd /d "%~dp0"

:: Ativa o ambiente virtual (ajuste 'venv' para o nome da sua pasta)
call .venv\Scripts\activate

:: Executa o script Python
python app.py

:: Mantém o terminal aberto se houver erro ou após finalizar
pause