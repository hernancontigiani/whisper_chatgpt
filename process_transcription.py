import os
text_path = 'transcription.txt'

if not os.path.exists(text_path):
    print("Error, mp4 file doesnt exists:", text_path)
    exit()

transcription = open(text_path, "r").read()

chatgpt_txt = f'''
Título de la reunión: Discutir como usar whisper y chatgpt
Cantidad de Participantes: 2
Contexto: lluvia de ideas
Transcripción de la reunión: {transcription}\n

Por favor genera un resumen de la transcripción anterior.
'''

print("Cantidad de caracteres:", len(chatgpt_txt))

# Guardar la transcripción en un archivo de texto
with open("chatgpt_msg.txt", "w") as f:
    f.write(chatgpt_txt)
print("Finish")