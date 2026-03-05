#!/usr/bin/env python3
"""
节拍器音频生成脚本（无需额外依赖）
纯 Python 实现
"""

import math
import struct
import random

def write_wav(filename, sample_rate, audio_data):
    """写入 WAV 文件"""
    num_samples = len(audio_data)
    num_channels = 1
    sample_width = 2  # 16-bit
    
    with open(filename, 'wb') as f:
        # RIFF header
        f.write(b'RIFF')
        f.write(struct.pack('<I', 36 + num_samples * num_channels * sample_width))
        f.write(b'WAVE')
        
        # fmt chunk
        f.write(b'fmt ')
        f.write(struct.pack('<I', 16))  # chunk size
        f.write(struct.pack('<H', 1))   # PCM
        f.write(struct.pack('<H', num_channels))
        f.write(struct.pack('<I', sample_rate))
        f.write(struct.pack('<I', sample_rate * num_channels * sample_width))
        f.write(struct.pack('<H', num_channels * sample_width))
        f.write(struct.pack('<H', sample_width * 8))
        
        # data chunk
        f.write(b'data')
        f.write(struct.pack('<I', num_samples * num_channels * sample_width))
        
        # audio data
        for sample in audio_data:
            # Clamp to [-1, 1] and convert to 16-bit int
            sample = max(-1.0, min(1.0, sample))
            int_sample = int(sample * 32767)
            f.write(struct.pack('<h', int_sample))

def generate_wood(is_accent, filename):
    """生成木鱼音色"""
    sample_rate = 44100
    duration = 0.08
    freq = 1200 if is_accent else 800
    volume = 0.7 if is_accent else 0.5
    
    num_samples = int(sample_rate * duration)
    audio = []
    
    for i in range(num_samples):
        t = i / sample_rate
        envelope = math.exp(-t * 30)
        sample = math.sin(2 * math.pi * freq * t) * envelope * volume
        audio.append(sample)
    
    write_wav(filename, sample_rate, audio)
    print(f"✓ 生成: {filename}")

def generate_click(is_accent, filename):
    """生成咔哒音色"""
    sample_rate = 44100
    duration = 0.05
    freq = 1500 if is_accent else 1000
    volume = 0.65 if is_accent else 0.45
    
    num_samples = int(sample_rate * duration)
    audio = []
    
    for i in range(num_samples):
        t = i / sample_rate
        envelope = math.exp(-t * 50)
        noise = (random.random() * 2 - 1) * 0.3
        tone = math.sin(2 * math.pi * freq * t) * 0.7
        sample = (tone + noise) * envelope * volume
        audio.append(sample)
    
    write_wav(filename, sample_rate, audio)
    print(f"✓ 生成: {filename}")

def generate_beep(is_accent, filename):
    """生成电子音色"""
    sample_rate = 44100
    duration = 0.1
    freq = 880 if is_accent else 660
    volume = 0.6 if is_accent else 0.4
    
    num_samples = int(sample_rate * duration)
    audio = []
    
    for i in range(num_samples):
        t = i / sample_rate
        envelope = math.exp(-t * 20)
        sample = math.sin(2 * math.pi * freq * t) * envelope * volume
        audio.append(sample)
    
    write_wav(filename, sample_rate, audio)
    print(f"✓ 生成: {filename}")

def generate_drum(is_accent, filename):
    """生成鼓声音色"""
    sample_rate = 44100
    duration = 0.15
    freq = 200 if is_accent else 150
    volume = 0.8 if is_accent else 0.55
    
    num_samples = int(sample_rate * duration)
    audio = []
    
    for i in range(num_samples):
        t = i / sample_rate
        envelope = math.exp(-t * 15)
        noise = (random.random() * 2 - 1) * 0.2
        kick = math.sin(2 * math.pi * freq * t * (1 - t * 5)) * 0.8
        sample = (kick + noise) * envelope * volume
        audio.append(sample)
    
    write_wav(filename, sample_rate, audio)
    print(f"✓ 生成: {filename}")

def main():
    print("开始生成节拍器音频文件...\n")
    
    # 生成所有音频文件
    sounds = [
        ('wood', generate_wood, '木鱼'),
        ('click', generate_click, '咔哒'),
        ('beep', generate_beep, '电子'),
        ('drum', generate_drum, '鼓声')
    ]
    
    for sound_type, generator, name in sounds:
        print(f"生成 {name} 音色:")
        generator(False, f"{sound_type}_normal.wav")
        generator(True, f"{sound_type}_accent.wav")
        print()
    
    print("=" * 50)
    print("所有音频文件生成完成！")
    print("\n后续步骤:")
    print("1. 将生成的 .wav 文件重命名为 .mp3")
    print("   (uni-app 支持 wav 格式，也可以直接使用)")
    print("2. 或使用 ffmpeg 转换为 mp3:")
    print("   for %f in (*.wav) do ffmpeg -i %f -codec:a libmp3lame -qscale:a 2 %~nf.mp3")
    print("3. 文件已在当前目录生成，可直接使用")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"错误: {e}")
        import traceback
        traceback.print_exc()
