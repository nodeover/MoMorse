import numpy as np
import simpleaudio as sa


def generate_tone(frequency, duration, sample_rate=44100, volume=0.3):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    
    if frequency == 0:
        return np.zeros_like(t)
    
    tone = np.sin(frequency * t * 2 * np.pi) * volume
    
    base_frequency = 500
    base_fade_ratio = 0.06
    
    fade_ratio = max(base_fade_ratio * (base_frequency / frequency), 0.05)
    
    fade_samples = int(sample_rate * duration * fade_ratio)
    max_fade_samples = int(sample_rate * 0.01)
    fade_in_samples = min(fade_samples, max_fade_samples)
    fade_out_samples = fade_in_samples
    
    # 페이드 인
    for i in range(fade_in_samples):
        tone[i] *= (i / fade_in_samples)
        
    # 페이드 아웃
    for i in range(fade_out_samples):
        tone[-i-1] *= (i / fade_out_samples)
        
    return tone


def play_audio(audio):
    audio = audio * (2**15 - 1) / np.max(np.abs(audio))
    audio = audio.astype(np.int16)
    play_obj = sa.play_buffer(audio, 1, 2, sample_rate)
    play_obj.wait_done()

# options
dot_duration = 0.05 # .
dash_duration = dot_duration*3 # .
char_duration = dot_duration*3 # btw char ' '
word_duration = dot_duration*7 # btw word '/'
sample_rate = 44100  # sampling rate
frequency = 500  # Hz

# var
signal = np.array([], dtype=np.float32)
message = ".... . .-.. .-.. --- ..--../-. .. -.-. ./- ---/-- . . -/-.-- --- ..-"

dash_tone = generate_tone(frequency, dash_duration, sample_rate)
dot_tone = generate_tone(frequency, dot_duration, sample_rate)
char_tone = generate_tone(0, char_duration, sample_rate)
word_tone = generate_tone(0, word_duration, sample_rate)

for element in message:
    if element == '.':
        tone = dot_tone
    elif element == '-':
        tone = dash_tone
    elif element == ' ':
        tone = char_tone
    elif element == '/':
        tone = word_tone
    else:
        pass
    signal = np.concatenate((signal, tone))
    
    # 요소 사이와 마지막 요소 이후에는 정적 추가
    silence = np.zeros(int(sample_rate * 0.1))
    signal = np.concatenate((signal, silence))

# play
play_audio(signal)
