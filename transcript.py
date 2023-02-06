import os
import subprocess
import whisper

# definir la ruta del video y audio
video_path = 'video.mp4'
audio_path = 'audio.wav'

if not os.path.exists(video_path):
    print("Error, mp4 file doesnt exists:", video_path)
    exit()

# extraer el audio del video con ffmpeg
if not os.path.exists(audio_path):
    print("Convert mp4 to wav...")
    command = f'ffmpeg -i {video_path} -vn -acodec pcm_s16le -ar 44100 -ac 2 {audio_path}'
    os.system(command)


if not os.path.exists(audio_path):
    print("Error, wav file doesnt exists:", audio_path)
    exit()

# procesar el audio con Whisper
# audio_file = open(audio_path, 'rb')
# audio_bytes = audio_file.read()
print("Star transcription in spanish")
model = whisper.load_model("small")
# transcription = model.transcribe(audio_path, language='es-ES')
result = model.transcribe(audio_path)

# Guardar la transcripción en un archivo de texto
with open("transcription.txt", "w") as f:
    f.write(result["text"])
print("Transcription saved to transcription.txt")
