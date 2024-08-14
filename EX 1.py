import sounddevice as sd
import wave

def gravar_audio(nome_arquivo, duracao_segundos, taxa_amostragem=44100):
    audio_data = sd.rec(int(duracao_segundos * taxa_amostragem), samplerate= taxa_amostragem,channels=1, dtype = "int16")

    print("Gravando...")
    sd.wait()
    with wave.open(nome_arquivo,"wb") as wf:
        wf.setchannels(1)
        wf.setframerate(4100)
        wf.setsampwidth(4)
        wf.writeframes(audio_data.tobytes())

    print(f"Áudio gravado com sucesso em '{nome_arquivo}'.")
def principal():
    nome_arquivo = "gravacao.wav"
    duracao_segundos = 5
    gravar_audio(nome_arquivo, duracao_segundos)

principal()
