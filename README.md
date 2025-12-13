# 🤗 Awesome Hugging Face Models

> A curated, up-to-date list of the best Hugging Face models for NLP, vision, audio, and multimodal tasks — clean links, clear use cases, zero fluff.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/github/stars/JehoshuaM/awesome-huggingface-models.svg?style=social)](https://github.com/JehoshuaM/awesome-huggingface-models/stargazers)

This repository highlights **production-ready**, **state-of-the-art**, and **community-trusted** models on the Hugging Face Hub. Models are grouped by task with demos and short descriptions so you can pick fast.

---

## 📋 Table of Contents

- [NLP](#-nlp)
  - [Large Language Models](#large-language-models)
  - [Text Classification](#text-classification)
  - [NER](#named-entity-recognition)
  - [Summarization](#summarization)
  - [Translation](#translation)
  - [Code Models](#code-models)
- [Computer Vision](#-computer-vision)
- [Audio](#-audio)
- [Multimodal](#-multimodal)
- [Recommended Picks (2025)](#-recommended-picks-2025)
- [Usage Examples](#-usage-examples)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🔤 NLP

### Large Language Models

| Model | Description | Size | Demo |
|------|-------------|------|------|
| [meta-llama/Meta-Llama-3-8B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct) | Strong general-purpose instruction model | 8B | 🚀 |
| [meta-llama/Meta-Llama-3.1-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.1-70B-Instruct) | Near-SOTA open LLM | 70B | 🚀 |
| [mistralai/Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) | Fast + efficient reasoning | 7B | 🚀 |
| [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) | High-quality multilingual LLM | 7B | 🚀 |
| [google/gemma-2-9b-it](https://huggingface.co/google/gemma-2-9b-it) | Lightweight, clean instruction tuning | 9B | 🚀 |

---

### Text Classification

| Model | Use Case |
|------|---------|
| [cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) | Sentiment analysis |
| [facebook/bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli) | Zero-shot classification |
| [unitary/toxic-bert](https://huggingface.co/unitary/toxic-bert) | Toxicity detection |

---

### Named Entity Recognition

| Model | Language |
|------|----------|
| [dbmdz/bert-large-cased-finetuned-conll03-english](https://huggingface.co/dbmdz/bert-large-cased-finetuned-conll03-english) | English |
| [xlm-roberta-large-finetuned-conll03-english](https://huggingface.co/xlm-roberta-large-finetuned-conll03-english) | Multilingual |

---

### Summarization

| Model | Type |
|------|-----|
| [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) | News |
| [google/pegasus-xsum](https://huggingface.co/google/pegasus-xsum) | Extreme summarization |
| [sshleifer/distilbart-cnn-12-6](https://huggingface.co/sshleifer/distilbart-cnn-12-6) | Lightweight |

---

### Translation

| Model | Languages |
|------|----------|
| [facebook/m2m100_418M](https://huggingface.co/facebook/m2m100_418M) | 100+ |
| [google/mt5-large](https://huggingface.co/google/mt5-large) | 101 |

---

### Code Models

| Model | Best For |
|------|---------|
| [bigcode/starcoder2-15b](https://huggingface.co/bigcode/starcoder2-15b) | Code generation |
| [Salesforce/codet5p-16b](https://huggingface.co/Salesforce/codet5p-16b) | Code understanding |
| [microsoft/CodeBERT-base](https://huggingface.co/microsoft/CodeBERT-base) | Code search |

---

## 🖼️ Computer Vision

| Model | Task |
|------|-----|
| [stabilityai/stable-diffusion-3](https://huggingface.co/stabilityai/stable-diffusion-3) | Image generation |
| [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) | Next-gen T2I |
| [facebook/detr-resnet-50](https://huggingface.co/facebook/detr-resnet-50) | Object detection |
| [IDEA-Research/GroundingDINO](https://huggingface.co/IDEA-Research/GroundingDINO) | Open-vocab detection |
| [nvidia/segformer-b5-finetuned-ade-640-640](https://huggingface.co/nvidia/segformer-b5-finetuned-ade-640-640) | Segmentation |

---

## 🎵 Audio

| Model | Task |
|------|-----|
| [openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) | Speech recognition |
| [distil-whisper/distil-large-v3](https://huggingface.co/distil-whisper/distil-large-v3) | Fast ASR |
| [facebook/seamless-m4t-v2-large](https://huggingface.co/facebook/seamless-m4t-v2-large) | Speech ↔ text |
| [facebook/musicgen-large](https://huggingface.co/facebook/musicgen-large) | Music generation |

---

## 🔀 Multimodal

| Model | Capability |
|------|-----------|
| [llava-hf/llava-1.6-34b](https://huggingface.co/llava-hf/llava-1.6-34b) | Vision + language |
| [Qwen/Qwen-VL-Chat](https://huggingface.co/Qwen/Qwen-VL-Chat) | Visual reasoning |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | Image-text similarity |
| [Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large) | Image captioning |

---

## ⭐ Recommended Picks (2025)

- **Best Open LLM** → Llama 3.1 70B  
- **Best Lightweight LLM** → Mistral 7B  
- **Best Image Model** → FLUX.1  
- **Best ASR** → Whisper v3  
- **Best Multimodal** → LLaVA 1.6  

---

## 🛠️ Usage Examples

```python
from transformers import pipeline

llm = pipeline("text-generation", model="meta-llama/Meta-Llama-3-8B-Instruct")
llm("Explain transformers in one sentence")

vision = pipeline("image-classification", model="google/vit-base-patch16-224")
vision("image.jpg")

asr = pipeline("automatic-speech-recognition",
               model="openai/whisper-large-v3")
asr("audio.wav")
```

🤝 Contributing
  PRs welcome.

Rules

 - Real models only
 - HF links required
 - Short + accurate descriptions
 - No dead or deprecated models

📝 License
  Creative Commons Attribution 4.0 International
  See LICENSE.md

© Jehoshua 2025

⭐ Star the repo if it helped
🔄 Last updated: December 2025

---
