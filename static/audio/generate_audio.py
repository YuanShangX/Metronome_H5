#!/usr/bin/env python3
"""
节拍器音频生成脚本
需要安装: pip install numpy scipy
"""

import numpy as np
from scipy.io import wavfile
import os

def generate_wood(is_accent, filename):
    """生成木鱼音色"""
    sample_rate = 44100
    duration = 0.08
    freq = 1200 if is_accent else 800
    volume = 0.4 if is_accent else 0.25
    
    t = np.linspace(0, duration, int(sample_rate * duration))
    envelope = np.exp(-t * 30)
    audio = np.sin(2 * np.pi * freq * t) * envelope * volume
    
    audio_int = np.int16(audio * 32767)
    wavfile.write(filename, sample_rate, audio_int)
    print(f"✓ 生成: {filename}")

def generate_click(is_accent, filename):
    """生成咔哒音色"""
    sample_rate = 44100
    duration = 0.05
    freq = 1500 if is_accent else 1000
    volume = 0.35 if is_accent else 0.2
    
    t = np.linspace(0, duration, int(sample_rate * duration))
    envelope = np.exp(-t * 50)
    noise = np.random.uniform(-1, 1, len(t)) * 0.3
    tone = np.sin(2 * np.pi * freq * t) * 0.7
    audio = (tone + noise) * envelope * volume
    
    audio_int = np.int16(audio * 32767)
    wavfile.write(filename, sample_rate, audio_int)
    print(f"✓ 生成: {filename}")

def generate_beep(is_accent, filename):
    """生成电子音色"""
    sample_rate = 44100
    duration = 0.1
    freq = 880 if is_accent else 660
    volume = 0.3 if is_accent else 0.18
    
    t = np.linspace(0, duration, int(sample_rate * duration))
    envelope = np.exp(-t * 20)
    audio = np.sin(2 * np.pi * freq * t) * envelope * volume
    
    audio_int = np.int16(audio * 32767)
    wavfile.write(filename, sample_rate, audio_int)
    print(f"✓ 生成: {filename}")

def generate_drum(is_accent, filename):
    """生成鼓声音色"""
    sample_rate = 44100
    duration = 0.15
    freq = 200 if is_accent else 150
    volume = 0.5 if is_accent else 0.3
    
    t = np.linspace(0, duration, int(sample_rate * duration))
    envelope = np.exp(-t * 15)
    noise = np.random.uniform(-1, 1, len(t)) * 0.2
    kick = np.sin(2 * np.pi * freq * t * (1 - t * 5)) * 0.8
    audio = (kick + noise) * envelope * volume
    
    audio_int = np.int16(audio * 32767)
    wavfile.write(filename, sample_rate, audio_int)
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
    print("\n提示:")
    print("1. 如需 MP3 格式，可使用 ffmpeg 转换:")
    print("   ffmpeg -i input.wav -codec:a libmp3lame -qscale:a 2 output.mp3")
    print("2. 或使用在线转换工具: https://cloudconvert.com/wav-to-mp3")
    print("3. 将生成的文件放到 static/audio/ 目录下")

if __name__ == "__main__":
    try:
        main()
    except ImportError:
        print("错误: 缺少必要的库")
        print("请运行: pip install numpy scipy")
    except Exception as e:
        print(f"错误: {e}")
