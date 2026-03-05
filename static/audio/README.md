# 节拍器音频文件说明

## 音频文件已生成 ✓

当前目录包含以下音频文件（已生成）：

### 木鱼音色
- `wood_normal.wav` - 普通拍 ✓
- `wood_accent.wav` - 重音拍 ✓

### 咔哒音色
- `click_normal.wav` - 普通拍 ✓
- `click_accent.wav` - 重音拍 ✓

### 电子音色
- `beep_normal.wav` - 普通拍 ✓
- `beep_accent.wav` - 重音拍 ✓

### 鼓声音色
- `drum_normal.wav` - 普通拍 ✓
- `drum_accent.wav` - 重音拍 ✓

## 如何重新生成音频

如果需要重新生成或修改音频文件：

### 使用 Python 脚本（推荐）
```bash
python generate_simple.py
```

### 使用浏览器生成器
在浏览器中打开 `generate.html`，点击按钮下载音频文件

## 音频参数说明

- 采样率: 44100 Hz
- 格式: WAV (16-bit PCM)
- 时长: 50-150ms
- 音量: 已优化，重音拍比普通拍更响

## 自定义音频

如果想使用自己的音频文件：
1. 确保文件格式为 WAV 或 MP3
2. 文件时长建议在 50-200ms 之间
3. 按照命名规则: `{音色类型}_{normal/accent}.wav`
4. 放置在当前目录即可

