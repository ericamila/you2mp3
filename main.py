import yt_dlp
import os
import tkinter as tk
from tkinter import messagebox

# Definindo o caminho da pasta de downloads para um local externo
caminho_downloads = os.path.expanduser('~/Downloads')

def baixar_audio_youtube(url_video):
    print(f"Iniciando download de: {url_video}...")

    opcoes = {
        'format': 'bestaudio/best', 
        'postprocessors': [{
            'key': 'FFmpegExtractAudio', # Usa o FFmpeg para extrair o áudio
            'preferredcodec': 'mp3',     # Converte 
            'preferredquality': '192',   
        }],
        # Nome do arquivo final: Título do vídeo.mp3
        'outtmpl': '%(title)s.%(ext)s', 

        'paths': {'home': caminho_downloads}, 
    }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url_video])
        print("Download e conversão concluídos com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def baixar_video_youtube(url_video):
    print(f"Iniciando download de: {url_video}...")

    opcoes = {
        'format': 'bestvideo+bestaudio/best', 
        'outtmpl': '%(title)s.%(ext)s', 
        'paths': {'home': caminho_downloads}, 
    }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url_video])
            print("Download concluído!")
    except Exception as e:
        print(f"Erro ao baixar: {e}")

def baixar():
    url = entry_url.get()
    if not url:
        messagebox.showwarning("Aviso", "Por favor, insira uma URL válida.")
        return
    tipo = var_tipo.get()
    if tipo == 'Áudio':
        baixar_audio_youtube(url)
    else:
        baixar_video_youtube(url)
    messagebox.showinfo("Sucesso", "Download concluído!")

# Criando a interface gráfica
root = tk.Tk()
root.title("Downloader YouTube")

# Label e Entry para URL
label_url = tk.Label(root, text="Cole a URL do vídeo do YouTube:")
label_url.pack(pady=10)
entry_url = tk.Entry(root, width=50)
entry_url.pack(pady=10)

# Radio buttons para escolher entre áudio e vídeo
var_tipo = tk.StringVar(value='Áudio')
radio_audio = tk.Radiobutton(root, text='Áudio', variable=var_tipo, value='Áudio')
radio_video = tk.Radiobutton(root, text='Vídeo', variable=var_tipo, value='Vídeo')
radio_audio.pack(pady=5)
radio_video.pack(pady=5)

# Botão para iniciar o download
botao_download = tk.Button(root, text="Baixar", command=baixar)
botao_download.pack(pady=20)

root.mainloop()