import sounddevice as sd
import wave
import speech_recognition as sr

def guardar_audio(nome_arquivo, duracao_segundos, taxa=44100):
    print("Diga um produto")
    audio = sd.rec(int(duracao_segundos * taxa), samplerate=taxa, channels=1, dtype='int16')
    sd.wait()
    with wave.open(nome_arquivo, 'wb') as wb:
        wb.setnchannels(1)
        wb.setsampwidth(2)
        wb.setframerate(taxa)
        wb.writeframes(audio.tobytes())
    print("Anotado com sucesso!")

def transcrever_audio():
    recognizer = sr.Recognizer()
    with sr.AudioFile("audio.wav") as source:
        print("Processando áudio...")
        audio = recognizer.record(source)
        texto = recognizer.recognize_google(audio, language="pt-BR")
        print("Transcrição:", texto)
        return texto

def adicionar_produtos():
    produtos = []
    while True:
        nome_arquivo = "audio.wav"
        duracao_segundos = 5
        guardar_audio(nome_arquivo, duracao_segundos)
        produto = transcrever_audio()
        produtos.append(produto)
        
        continuar = input("Deseja adicionar mais um produto? (S/N): ").strip().lower()
        if continuar != "s":
            break
    
    print("\nProdutos anotados:")
    for idx, produto in enumerate(produtos, 1):
        print(f"{idx}. {produto}")

def principal():
    adicionar_produtos()

principal()
