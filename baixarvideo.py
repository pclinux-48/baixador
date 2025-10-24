import subprocess
import sys
import yt_dlp
import os

def instalar_yt_dlp():
    """Instala a biblioteca yt-dlp se ainda não estiver instalada."""
    try:
        import yt_dlp
        print("yt-dlp já está instalado.")
    except ImportError:
        print("yt-dlp não encontrado. Instalando...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
            print("yt-dlp instalado com sucesso!")
        except subprocess.CalledProcessError as e:
            print(f"Erro ao tentar instalar yt-dlp: {e}")
            sys.exit(1)

def baixar_video_com_yt_dlp(url):
    """
    Baixa o vídeo da URL fornecida usando a biblioteca yt-dlp.
    """
    # Define as opções de download:
    ydl_opts = {
        # Formato do arquivo (por exemplo, melhor qualidade de vídeo e áudio)
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        
        # Onde salvar o arquivo: nome original do vídeo + ID do vídeo + extensão
        'outtmpl': os.path.join('videos_baixados', '%(title)s.%(ext)s'),
        
        # Ignorar erros de certificado SSL
        'nocheckcertificate': True,
        
        # Se for uma playlist, apenas baixar o vídeo
        'noplaylist': True,
        
        # Definir a verbosidade (saída no terminal) para a experiência do usuário
        'quiet': False,
    }

    try:
        print(f"\nIniciando o download da URL: {url}")
        
        # Cria a pasta 'videos_baixados' se ela não existir
        if not os.path.exists('videos_baixados'):
            os.makedirs('videos_baixados')
            
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Tenta extrair informações e baixar o vídeo
            ydl.download([url])
        
        print("\n=======================================================")
        print("✅ Download concluído com sucesso!")
        print("O vídeo foi salvo na pasta 'videos_baixados'.")
        print("=======================================================")

    except yt_dlp.utils.DownloadError as e:
        print(f"\n❌ ERRO DE DOWNLOAD: Não foi possível baixar o vídeo.")
        print(f"Detalhes: {e}")
    except Exception as e:
        print(f"\n❌ ERRO INESPERADO: {e}")

# --- EXECUÇÃO PRINCIPAL ---
if __name__ == "__main__":
    
    # Garante que a biblioteca está instalada
    instalar_yt_dlp()
    
    # Loop para garantir que o usuário forneça uma URL válida
    while True:
        link_video = input("\nPor favor, cole a URL do vídeo que deseja baixar (ou digite 'sair'): ").strip()
        
        if link_video.lower() == 'sair':
            print("Programa encerrado.")
            break
            
        if link_video and ('http' in link_video or 'https' in link_video):
            baixar_video_com_yt_dlp(link_video)
        else:
            print("URL inválida. Por favor, tente novamente ou digite 'sair'.")