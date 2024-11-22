import whisper
import pyaudio
import numpy as np
import wave

model = whisper.load_model("base")

p = pyaudio.PyAudio()

RATE = 16000
CHUNK = 1024

stream = p.open(
    format=pyaudio.paInt16,
    channels=1,
    rate=RATE,
    input=True,
    frames_per_buffer=CHUNK
)

print("Listening for speech...")

while True:
    frames = []
    for _ in range(0, int(RATE / CHUNK * 5)):
        data = stream.read(CHUNK)
        frames.append(data)

    audio_data = np.frombuffer(b''.join(frames), dtype=np.int16)

    result = model.transcribe(audio_data)

    print("Transribed Text: ", result["text"])