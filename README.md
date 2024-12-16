# Voice KKuTu

[![Hugging Face: ShapeLayer/embedded-voice-kkutu-models](https://img.shields.io/badge/%F0%9F%A4%97-ShapeLayer%2fembedded--voice--kkutu--models-yellow)](https://huggingface.co/ShapeLayer/embedded-voice-kkutu-models)

Voice KKuTu - Team Project for Embedded Software Lecture

## Getting Started

[`rye`](https://rye.astral.sh) is required for run this project easily.

**Required:**
```sh
# 1. Fetch KKuTu Repository
git module init
git module update

# 2. Install dependencies
rye sync

# 3. Convert word database from KKuTu DB*
rye run convert

# 4. Download and convert whisper model**
rye run make-model
```
\* [&lt;Convert word data from KKuTu DB&gt;](#convert-word-data-from-kkutu-db) Section.  
\*\* [&lt;Download and convert Whisper model or just download from Hugging Face&gt;](#download-and-convert-whisper-model-or-just-download-from-hugging-face) Section.  


**(Optional) When you clone for developing:**
```sh
# Install pre commit script for linting
rye run pre-commit
```

## Details
### Commands
If below commands are not executed sucessfully, Try `rye sync` first.

```sh
rye run app
rye run convert
rye run clean
rye run black
rye run pre-commit
rye run make-model
rye run stt
```

### Convert word data from KKuTu DB\*
This repository contains KKuTu repository as submodule.  

Word data for KKuTu server can be migrated for this project with converting script.

```sh
git submodule init
git submodule update
rye run convert
```

### Download and convert Whisper model or just download from Hugging Face\*\*

```sh
rye run make-model
rye run make-model --model-size=model
```

There are converted model at [Hugging Face](https://huggingface.co/ShapeLayer/embedded-voice-kkutu-models). You can run application just downloading models from there.

```sh
git lfs install
git clone https://huggingface.co/ShapeLayer/embedded-voice-kkutu-models models
```

> [!NOTE]
> If you use a model other than the default model, you must pass parameters while running the app.

```sh
rye run app --model=model
```

| Model | `model` value |
| :-: | :-: |
| Tiny | `tiny` |
| (en) Tiny | `tiny.en` |
| Base | `base` |
| (en) Base | `base.en` |
| Small | `small` |
| (en) Small | `small.en` |
| Medium | `medium` |
| (en) Medium | `medium.en` |
| Large-v1 | `large-v1` |
| Large-v2 | `large-v2` |
| Large-v3 | `large-v3` |
| Large-v3-turbo | `large-v3-turbo` |
| Turbo | `turbo` |
| Distil-large-v2 | `distil-large-v2` |
| Distil-large-v3 | `distil-large-v3` |
| (en) Distil-medium | `distil-medium.en` |
| (en) Distil-small | `distil-small.en` |

## Troubleshooting

### fatal error: 'portaudio.h' file not found

```
[stderr]
src/pyaudio/device_api.c:9:10: fatal error: 'portaudio.h' file not found
    9 | #include "portaudio.h"
      |          ^~~~~~~~~~~~~
1 error generated.
error: command '/usr/bin/clang' failed with exit code 1

hint: This error likely indicates that you need to install a library that provides "portaudio.h" for `pyaudio@0.2.14`
```

Install portaudio
```sh
sudo apt-get install portaudio19-dev  
```


### Warning: When Run in Raspberry Pi
To install PyTorch on a Raspberry Pi, you need to install the CPU-only version. You can do so using the following command:
```sh
pip install torch torchvision torchaudio --index-url <https://download.pytorch.org/whl/cpu>

```

### Activate audio
```sh
# Enable auido (loads snd_bcm2835)
dtparam=audio=on
```
Remove comments from `boot/config.txt`

```sh
sudo /etc/init.d/alsa-utils reset
sudo reboot
```

### Set audio output device using `raspi-config`
```sh
sudo raspi-config
```
System Options > Audio > [choose the audio output]

### Test audio output is enabled
Run TTS
```sh
sudo apt-get install espeak
espeak "hello"
```
