import yt_dlp
import os

def baixar_audio_youtube(url_video):
    print(f"Iniciando download de: {url_video}...")

    # Configurações do download
    opcoes = {
        'format': 'bestaudio/best', # Baixa a melhor qualidade de áudio
        'postprocessors': [{
            'key': 'FFmpegExtractAudio', # Usa o FFmpeg para extrair o áudio
            'preferredcodec': 'mp3',     # Converte para MP3
            'preferredquality': '192',   # Qualidade (192kbps é padrão standard)
        }],
        # Nome do arquivo final: Título do vídeo.mp3
        'outtmpl': '%(title)s.%(ext)s', 
        # (Opcional) Define pasta de destino. Remove se quiser na pasta atual.
        'paths': {'home': './downloads'}, 
    }

    try:
        with yt_dlp.YoutubeDL(opcoes) as ydl:
            ydl.download([url_video])
        print("Download e conversão concluídos com sucesso!")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

def executar():
    link = input("Cole a URL do vídeo do YouTube: ")
    baixar_audio_youtube(link)        

if __name__ == "__main__":

    executar()

    print("\n" + "=====================================\n" )
    opcao = input("Pressione 'Enter' para baixar outro áudio ou qualquer outra tecla para sair... ")
    print("\n" + "=====================================\n" )

    os.system('cls' if os.name == 'nt' else 'clear')

    if opcao != "":
        exit()

    executar()