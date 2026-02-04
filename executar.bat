@echo off

call .venv\Scripts\activate

python main.py

:: Mantém o terminal aberto se houver erro ou após finalizar
pause