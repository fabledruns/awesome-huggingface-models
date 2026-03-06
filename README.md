# Awesome Hugging Face Models

> A curated list of the best Hugging Face models for NLP, vision, audio, and multimodal tasks — clean links, clear use cases, zero fluff.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/github/stars/JehoshuaM/awesome-huggingface-models.svg?style=social)](https://github.com/JehoshuaM/awesome-huggingface-models/stargazers)

This repository highlights **production-ready**, **state-of-the-art**, and **community-trusted** models on the Hugging Face Hub. Models are grouped by task with short descriptions so you can pick fast.

---

## Table of Contents

- [NLP](#nlp)
  - [Large Language Models](#large-language-models)
  - [Reasoning Models](#reasoning-models)
  - [Text Classification](#text-classification)
  - [Named Entity Recognition](#named-entity-recognition)
  - [Summarization](#summarization)
  - [Translation](#translation)
  - [Code Models](#code-models)
- [Computer Vision](#computer-vision)
- [Audio](#audio)
- [Multimodal](#multimodal)
- [Recommended Picks (2026)](#recommended-picks-2026)
- [Usage Examples](#usage-examples)
- [Contributing](#contributing)
- [License](#license)

---

## NLP

### Large Language Models

| Model | Description | Size |
|-------|-------------|------|
| [meta-llama/Llama-4-Scout-17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) | Fast multimodal instruction model, great for chat and agents | 17B MoE |
| [meta-llama/Llama-4-Maverick-17B-128E-Instruct](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) | Stronger Llama 4 variant, handles text + structured data | 17B MoE |
| [meta-llama/Meta-Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.3-70B-Instruct) | Clean structured output, solid everyday reasoning | 70B |
| [Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) | Strong reasoning + multilingual, Apache 2.0 | 32B |
| [Qwen/Qwen2.5-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-72B-Instruct) | Topped OpenCompass leaderboard, 29+ languages | 72B |
| [mistralai/Mixtral-8x22B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) | Fast MoE model, Apache 2.0, strong general reasoning | 141B MoE |
| [mistralai/Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) | Efficient and fast for its size | 7B |
| [google/gemma-3-9b-it](https://huggingface.co/google/gemma-3-9b-it) | Lightweight, low resource, great for edge/local use | 9B |
| [deepseek-ai/DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3) | Frontier-level general assistant, MoE with 128K context | 671B MoE |

---

### Reasoning Models

| Model | Description | Size |
|-------|-------------|------|
| [deepseek-ai/DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) | Best open reasoning model; rivals OpenAI o1 on math/code/logic | 671B MoE |
| [deepseek-ai/DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B) | Distilled R1; outperforms o1-mini, way more accessible | 32B |
| [deepseek-ai/DeepSeek-R1-Distill-Llama-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B) | Smallest R1 distill; solid reasoning at low compute cost | 8B |

---

### Text Classification

| Model | Use Case |
|-------|---------|
| [cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) | Sentiment analysis |
| [facebook/bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli) | Zero-shot classification |
| [unitary/toxic-bert](https://huggingface.co/unitary/toxic-bert) | Toxicity detection |

---

### Named Entity Recognition

| Model | Language |
|-------|----------|
| [dbmdz/bert-large-cased-finetuned-conll03-english](https://huggingface.co/dbmdz/bert-large-cased-finetuned-conll03-english) | English |
| [xlm-roberta-large-finetuned-conll03-english](https://huggingface.co/xlm-roberta-large-finetuned-conll03-english) | Multilingual |

---

### Summarization

| Model | Type |
|-------|------|
| [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) | News |
| [google/pegasus-xsum](https://huggingface.co/google/pegasus-xsum) | Extreme summarization |
| [sshleifer/distilbart-cnn-12-6](https://huggingface.co/sshleifer/distilbart-cnn-12-6) | Lightweight |

---

### Translation

| Model | Languages |
|-------|----------|
| [facebook/m2m100_418M](https://huggingface.co/facebook/m2m100_418M) | 100+ |
| [google/mt5-large](https://huggingface.co/google/mt5-large) | 101 |

---

### Code Models

| Model | Best For |
|-------|---------|
| [deepseek-ai/DeepSeek-Coder-V2-Instruct](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Instruct) | Best open code model; 300+ languages |
| [Qwen/Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) | Strong multilingual coding |
| [bigcode/starcoder2-15b](https://huggingface.co/bigcode/starcoder2-15b) | Code generation |
| [microsoft/CodeBERT-base](https://huggingface.co/microsoft/CodeBERT-base) | Code search |

---

## Computer Vision

| Model | Task |
|-------|------|
| [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) | Best open image generation model |
| [stabilityai/stable-diffusion-3-medium](https://huggingface.co/stabilityai/stable-diffusion-3-medium) | Image generation |
| [facebook/detr-resnet-50](https://huggingface.co/facebook/detr-resnet-50) | Object detection |
| [IDEA-Research/GroundingDINO](https://huggingface.co/IDEA-Research/GroundingDINO) | Open-vocab detection |
| [nvidia/segformer-b5-finetuned-ade-640-640](https://huggingface.co/nvidia/segformer-b5-finetuned-ade-640-640) | Segmentation |

---

## Audio

| Model | Task |
|-------|------|
| [openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) | Best open ASR |
| [distil-whisper/distil-large-v3](https://huggingface.co/distil-whisper/distil-large-v3) | Fast ASR |
| [facebook/seamless-m4t-v2-large](https://huggingface.co/facebook/seamless-m4t-v2-large) | Speech to/from text, multilingual |
| [facebook/musicgen-large](https://huggingface.co/facebook/musicgen-large) | Music generation |

---

## Multimodal

| Model | Capability |
|-------|-----------|
| [meta-llama/Llama-4-Scout-17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) | Vision + language, real-time inference |
| [Qwen/Qwen2.5-VL-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct) | Visual reasoning, strong on charts/docs |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | Image-text similarity |
| [Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large) | Image captioning |
| [microsoft/Florence-2-large](https://huggingface.co/microsoft/Florence-2-large) | Dense vision tasks: captioning, grounding, OCR |

---

## Recommended Picks (2026)

- **Best Open LLM** -> Llama 3.3 70B or DeepSeek-V3
- **Best Reasoning Model** -> DeepSeek-R1
- **Best Lightweight LLM** -> Mistral 7B or Gemma 3 9B
- **Best Code Model** -> DeepSeek-Coder-V2
- **Best Image Model** -> FLUX.1-dev
- **Best ASR** -> Whisper Large v3
- **Best Multimodal** -> Qwen2.5-VL 72B

---

## Usage Examples

```python
from transformers import pipeline

# Text generation
llm = pipeline("text-generation", model="meta-llama/Meta-Llama-3.3-70B-Instruct")
llm("Explain transformers in one sentence")

# Vision
vision = pipeline("image-classification", model="google/vit-base-patch16-224")
vision("image.jpg")

# Speech recognition
asr = pipeline("automatic-speech-recognition", model="openai/whisper-large-v3")
asr("audio.wav")

# Code generation
coder = pipeline("text-generation", model="Qwen/Qwen2.5-Coder-32B-Instruct")
coder("Write a binary search in Python")
```

---

## Contributing

PRs welcome.

Rules:
- Real models only
- HF links required
- Short and accurate descriptions
- No dead or deprecated models

---

## License

Creative Commons Attribution 4.0 International — see LICENSE.md

© Jehoshua 2026

Star the repo if it helped.  
Last updated: March 2026
