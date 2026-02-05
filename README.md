#### Melhorias na interface com tkinter
 - Adicionar opções para baixar áudio ou vídeo
 - Melhorar a usabilidade e estética da interface

#### Criar executável com PyInstaller
 - Usar o comando 'pyinstaller --onefile main.py' para gerar o executável.
````sh
uv run pyinstaller -–noconsole -–name="Converte You2mp3" -–incon "icon.ico" -–add-data="icon.ico;." -–onefile main.py 

uv run pyinstaller --onefile --windowed --icon=icon.ico main.py
````