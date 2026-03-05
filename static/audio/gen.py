import math
import struct
import random

def write_wav(filename, sample_rate, audio_data):
    num_samples = len(audio_data)
    num_channels = 1
    sample_width = 2
    
    with open(filename, 'wb') as f:
        f.write(b'RIFF')
        f.write(struct.pack('<I', 36 + num_samples * num_channels * sample_width))
        f.write(b'WAVE')
        f.write(b'fmt ')
        f.write(struct.pack('<I', 16))
        f.write(struct.pack('<H', 1))
        f.write(struct.pack('<H', num_channels))
        f.write(struct.pack('<I', sample_rate))
        f.write(struct.pack('<I', sample_rate * num_channels * sample_width))
        f.write(struct.pack('<H', num_channels * sample_width))
        f.write(struct.pack('<H', sample_width * 8))
        f.write(b'data')
        f.write(struct.pack('<I', num_samples * num_channels * sample_width))
        
        for sample in audio_data:
            sample = max(-1.0, min(1.0, sample))
            int_sample = int(sample * 32767)
            f.write(struct.pack('<h', int_sample))

def gen_wood(is_accent, filename):
    sr = 44100
    dur = 0.08
    freq = 1200 if is_accent else 800
    vol = 0.7 if is_accent else 0.5
    
    audio = []
    for i in range(int(sr * dur)):
        t = i / sr
        env = math.exp(-t * 30)
        audio.append(math.sin(2 * math.pi * freq * t) * env * vol)
    
    write_wav(filename, sr, audio)
    print(f"OK: {filename}")

def gen_click(is_accent, filename):
    sr = 44100
    dur = 0.05
    freq = 1500 if is_accent else 1000
    vol = 0.65 if is_accent else 0.45
    
    audio = []
    for i in range(int(sr * dur)):
        t = i / sr
        env = math.exp(-t * 50)
        noise = (random.random() * 2 - 1) * 0.3
        tone = math.sin(2 * math.pi * freq * t) * 0.7
        audio.append((tone + noise) * env * vol)
    
    write_wav(filename, sr, audio)
    print(f"OK: {filename}")

def gen_beep(is_accent, filename):
    sr = 44100
    dur = 0.1
    freq = 880 if is_accent else 660
    vol = 0.6 if is_accent else 0.4
    
    audio = []
    for i in range(int(sr * dur)):
        t = i / sr
        env = math.exp(-t * 20)
        audio.append(math.sin(2 * math.pi * freq * t) * env * vol)
    
    write_wav(filename, sr, audio)
    print(f"OK: {filename}")

def gen_drum(is_accent, filename):
    sr = 44100
    dur = 0.15
    freq = 200 if is_accent else 150
    vol = 0.8 if is_accent else 0.55
    
    audio = []
    for i in range(int(sr * dur)):
        t = i / sr
        env = math.exp(-t * 15)
        noise = (random.random() * 2 - 1) * 0.2
        kick = math.sin(2 * math.pi * freq * t * (1 - t * 5)) * 0.8
        audio.append((kick + noise) * env * vol)
    
    write_wav(filename, sr, audio)
    print(f"OK: {filename}")

print("Generating audio files...")
gen_wood(False, "wood_normal.wav")
gen_wood(True, "wood_accent.wav")
gen_click(False, "click_normal.wav")
gen_click(True, "click_accent.wav")
gen_beep(False, "beep_normal.wav")
gen_beep(True, "beep_accent.wav")
gen_drum(False, "drum_normal.wav")
gen_drum(True, "drum_accent.wav")
print("Done!")
