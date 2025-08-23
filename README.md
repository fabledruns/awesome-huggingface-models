# 🤗 Awesome Hugging Face Models

> Top Hugging Face models for NLP, vision, and audio tasks — links, descriptions, and demos included.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/github/stars/JehoshuaM/awesome-huggingface-models.svg?style=social&label=Star&maxAge=2592000)](https://github.com/JehoshuaM/awesome-huggingface-models/stargazers/)

A curated list of the most powerful and popular models available on Hugging Face Hub, organized by task and domain. Each model includes direct links, detailed descriptions, and information about available demos.

## 📋 Table of Contents

- [Natural Language Processing](#-natural-language-processing)
  - [Large Language Models](#large-language-models)
  - [Text Classification](#text-classification)
  - [Named Entity Recognition](#named-entity-recognition)
  - [Question Answering](#question-answering)
  - [Text Summarization](#text-summarization)
  - [Translation](#translation)
  - [Code Generation](#code-generation)
- [Computer Vision](#-computer-vision)
  - [Image Classification](#image-classification)
  - [Object Detection](#object-detection)
  - [Image Segmentation](#image-segmentation)
  - [Image Generation](#image-generation)
  - [Optical Character Recognition](#optical-character-recognition)
- [Audio Processing](#-audio-processing)
  - [Speech Recognition](#speech-recognition)
  - [Text-to-Speech](#text-to-speech)
  - [Audio Classification](#audio-classification)
  - [Music Generation](#music-generation)
- [Multimodal](#-multimodal)
  - [Vision-Language](#vision-language)
  - [Audio-Text](#audio-text)
- [Contributing](#-contributing)
- [License](#-license)

## 🔤 Natural Language Processing

### Large Language Models

| Model | Description | Size | Demo |
|-------|-------------|------|------|
| [microsoft/DialoGPT-large](https://huggingface.co/microsoft/DialoGPT-large) | Conversational AI model fine-tuned on Reddit conversations | 345M | [🚀 Demo](https://huggingface.co/microsoft/DialoGPT-large) |
| [EleutherAI/gpt-j-6B](https://huggingface.co/EleutherAI/gpt-j-6B) | Open-source GPT-style autoregressive language model | 6B | [🚀 Demo](https://huggingface.co/EleutherAI/gpt-j-6B) |
| [bigscience/bloom-7b1](https://huggingface.co/bigscience/bloom-7b1) | Multilingual autoregressive language model trained on 46 languages | 7.1B | [🚀 Demo](https://huggingface.co/bigscience/bloom-7b1) |
| [meta-llama/Llama-2-7b-chat-hf](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) | Fine-tuned Llama 2 model optimized for dialogue use cases | 7B | [🚀 Demo](https://huggingface.co/meta-llama/Llama-2-7b-chat-hf) |
| [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) | Mixture of experts model with excellent instruction following | 46.7B | [🚀 Demo](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) |

### Text Classification

| Model | Description | Use Case | Demo |
|-------|-------------|----------|------|
| [cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) | Sentiment analysis model trained on Twitter data | Social media sentiment | [🚀 Demo](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) |
| [facebook/bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli) | Zero-shot classification using natural language inference | General classification | [🚀 Demo](https://huggingface.co/facebook/bart-large-mnli) |
| [martin-ha/toxic-comment-model](https://huggingface.co/martin-ha/toxic-comment-model) | Detects toxic comments and hate speech | Content moderation | [🚀 Demo](https://huggingface.co/martin-ha/toxic-comment-model) |

### Named Entity Recognition

| Model | Description | Languages | Demo |
|-------|-------------|-----------|------|
| [dbmdz/bert-large-cased-finetuned-conll03-english](https://huggingface.co/dbmdz/bert-large-cased-finetuned-conll03-english) | BERT model fine-tuned for NER on CoNLL-03 | English | [🚀 Demo](https://huggingface.co/dbmdz/bert-large-cased-finetuned-conll03-english) |
| [xlm-roberta-large-finetuned-conll03-english](https://huggingface.co/xlm-roberta-large-finetuned-conll03-english) | Multilingual RoBERTa for cross-lingual NER | 100+ languages | [🚀 Demo](https://huggingface.co/xlm-roberta-large-finetuned-conll03-english) |

### Question Answering

| Model | Description | Type | Demo |
|-------|-------------|------|------|
| [deepset/roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2) | RoBERTa fine-tuned on SQuAD 2.0 for extractive QA | Extractive | [🚀 Demo](https://huggingface.co/deepset/roberta-base-squad2) |
| [microsoft/DialoGPT-medium](https://huggingface.co/microsoft/DialoGPT-medium) | Conversational QA with context understanding | Generative | [🚀 Demo](https://huggingface.co/microsoft/DialoGPT-medium) |

### Text Summarization

| Model | Description | Type | Demo |
|-------|-------------|------|------|
| [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) | BART fine-tuned on CNN/DailyMail for news summarization | Abstractive | [🚀 Demo](https://huggingface.co/facebook/bart-large-cnn) |
| [google/pegasus-xsum](https://huggingface.co/google/pegasus-xsum) | PEGASUS model fine-tuned on XSum dataset | Abstractive | [🚀 Demo](https://huggingface.co/google/pegasus-xsum) |
| [sshleifer/distilbart-cnn-12-6](https://huggingface.co/sshleifer/distilbart-cnn-12-6) | Distilled BART model for efficient summarization | Abstractive | [🚀 Demo](https://huggingface.co/sshleifer/distilbart-cnn-12-6) |

### Translation

| Model | Description | Languages | Demo |
|-------|-------------|-----------|------|
| [Helsinki-NLP/opus-mt-en-de](https://huggingface.co/Helsinki-NLP/opus-mt-en-de) | English to German translation | EN → DE | [🚀 Demo](https://huggingface.co/Helsinki-NLP/opus-mt-en-de) |
| [facebook/m2m100_418M](https://huggingface.co/facebook/m2m100_418M) | Multilingual machine translation without English pivoting | 100 languages | [🚀 Demo](https://huggingface.co/facebook/m2m100_418M) |
| [google/mt5-large](https://huggingface.co/google/mt5-large) | Multilingual T5 for various text-to-text tasks | 101 languages | [🚀 Demo](https://huggingface.co/google/mt5-large) |

### Code Generation

| Model | Description | Languages | Demo |
|-------|-------------|-----------|------|
| [Salesforce/codegen-350M-mono](https://huggingface.co/Salesforce/codegen-350M-mono) | Code generation model trained on Python | Python | [🚀 Demo](https://huggingface.co/Salesforce/codegen-350M-mono) |
| [microsoft/CodeBERT-base](https://huggingface.co/microsoft/CodeBERT-base) | Pre-trained model for programming languages | Multiple | [🚀 Demo](https://huggingface.co/microsoft/CodeBERT-base) |
| [codeparrot/codeparrot](https://huggingface.co/codeparrot/codeparrot) | GPT-2 model fine-tuned on Python code | Python | [🚀 Demo](https://huggingface.co/codeparrot/codeparrot) |

## 🖼️ Computer Vision

### Image Classification

| Model | Description | Dataset | Demo |
|-------|-------------|---------|------|
| [google/vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224) | Vision Transformer for image classification | ImageNet-21k | [🚀 Demo](https://huggingface.co/google/vit-base-patch16-224) |
| [microsoft/resnet-50](https://huggingface.co/microsoft/resnet-50) | ResNet-50 model for general image classification | ImageNet-1k | [🚀 Demo](https://huggingface.co/microsoft/resnet-50) |
| [google/efficientnet-b7](https://huggingface.co/google/efficientnet-b7) | EfficientNet model with excellent accuracy/efficiency trade-off | ImageNet | [🚀 Demo](https://huggingface.co/google/efficientnet-b7) |

### Object Detection

| Model | Description | Framework | Demo |
|-------|-------------|-----------|------|
| [facebook/detr-resnet-50](https://huggingface.co/facebook/detr-resnet-50) | End-to-end object detection with Transformers | PyTorch | [🚀 Demo](https://huggingface.co/facebook/detr-resnet-50) |
| [hustvl/yolos-tiny](https://huggingface.co/hustvl/yolos-tiny) | You Only Look at One Sequence for object detection | PyTorch | [🚀 Demo](https://huggingface.co/hustvl/yolos-tiny) |

### Image Segmentation

| Model | Description | Type | Demo |
|-------|-------------|------|------|
| [facebook/detr-resnet-50-panoptic](https://huggingface.co/facebook/detr-resnet-50-panoptic) | DETR model for panoptic segmentation | Panoptic | [🚀 Demo](https://huggingface.co/facebook/detr-resnet-50-panoptic) |
| [nvidia/segformer-b5-finetuned-ade-640-640](https://huggingface.co/nvidia/segformer-b5-finetuned-ade-640-640) | SegFormer for semantic segmentation | Semantic | [🚀 Demo](https://huggingface.co/nvidia/segformer-b5-finetuned-ade-640-640) |

### Image Generation

| Model | Description | Type | Demo |
|-------|-------------|------|------|
| [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) | Stable Diffusion model for text-to-image generation | Text-to-Image | [🚀 Demo](https://huggingface.co/runwayml/stable-diffusion-v1-5) |
| [CompVis/stable-diffusion-v1-4](https://huggingface.co/CompVis/stable-diffusion-v1-4) | Earlier version of Stable Diffusion | Text-to-Image | [🚀 Demo](https://huggingface.co/CompVis/stable-diffusion-v1-4) |
| [prompthero/openjourney](https://huggingface.co/prompthero/openjourney) | Fine-tuned Stable Diffusion with artistic style | Text-to-Image | [🚀 Demo](https://huggingface.co/prompthero/openjourney) |

### Optical Character Recognition

| Model | Description | Languages | Demo |
|-------|-------------|-----------|------|
| [microsoft/trocr-base-printed](https://huggingface.co/microsoft/trocr-base-printed) | Transformer-based OCR for printed text | English | [🚀 Demo](https://huggingface.co/microsoft/trocr-base-printed) |
| [microsoft/trocr-large-handwritten](https://huggingface.co/microsoft/trocr-large-handwritten) | OCR model specifically for handwritten text | English | [🚀 Demo](https://huggingface.co/microsoft/trocr-large-handwritten) |

## 🎵 Audio Processing

### Speech Recognition

| Model | Description | Languages | Demo |
|-------|-------------|-----------|------|
| [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) | State-of-the-art speech recognition and translation | 99 languages | [🚀 Demo](https://huggingface.co/openai/whisper-large-v2) |
| [facebook/wav2vec2-large-960h-lv60-self](https://huggingface.co/facebook/wav2vec2-large-960h-lv60-self) | Self-supervised speech recognition model | English | [🚀 Demo](https://huggingface.co/facebook/wav2vec2-large-960h-lv60-self) |
| [jonatasgrosman/wav2vec2-large-xlsr-53-english](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english) | Cross-lingual speech recognition model | English | [🚀 Demo](https://huggingface.co/jonatasgrosman/wav2vec2-large-xlsr-53-english) |

### Text-to-Speech

| Model | Description | Quality | Demo |
|-------|-------------|---------|------|
| [microsoft/speecht5_tts](https://huggingface.co/microsoft/speecht5_tts) | SpeechT5 model for text-to-speech synthesis | High | [🚀 Demo](https://huggingface.co/microsoft/speecht5_tts) |
| [espnet/kan-bayashi_ljspeech_vits](https://huggingface.co/espnet/kan-bayashi_ljspeech_vits) | VITS model for high-quality speech synthesis | High | [🚀 Demo](https://huggingface.co/espnet/kan-bayashi_ljspeech_vits) |

### Audio Classification

| Model | Description | Classes | Demo |
|-------|-------------|---------|------|
| [MIT/ast-finetuned-audioset-10-10-0.4593](https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593) | Audio Spectrogram Transformer for sound classification | 527 classes | [🚀 Demo](https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593) |
| [superb/wav2vec2-base-superb-er](https://huggingface.co/superb/wav2vec2-base-superb-er) | Emotion recognition from speech | Emotions | [🚀 Demo](https://huggingface.co/superb/wav2vec2-base-superb-er) |

### Music Generation

| Model | Description | Type | Demo |
|-------|-------------|------|------|
| [facebook/musicgen-small](https://huggingface.co/facebook/musicgen-small) | MusicGen model for controllable music generation | Conditional | [🚀 Demo](https://huggingface.co/facebook/musicgen-small) |
| [facebook/musicgen-melody](https://huggingface.co/facebook/musicgen-melody) | MusicGen with melody conditioning capabilities | Melody-conditioned | [🚀 Demo](https://huggingface.co/facebook/musicgen-melody) |

## 🔀 Multimodal

### Vision-Language

| Model | Description | Capabilities | Demo |
|-------|-------------|--------------|------|
| [Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large) | BLIP model for image captioning | Image → Text | [🚀 Demo](https://huggingface.co/Salesforce/blip-image-captioning-large) |
| [Salesforce/blip-vqa-base](https://huggingface.co/Salesforce/blip-vqa-base) | Visual question answering with BLIP | VQA | [🚀 Demo](https://huggingface.co/Salesforce/blip-vqa-base) |
| [microsoft/git-large-coco](https://huggingface.co/microsoft/git-large-coco) | Generative Image-to-text Transformer | Image captioning | [🚀 Demo](https://huggingface.co/microsoft/git-large-coco) |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | CLIP model for image-text similarity | Zero-shot classification | [🚀 Demo](https://huggingface.co/openai/clip-vit-large-patch14) |

### Audio-Text

| Model | Description | Capabilities | Demo |
|-------|-------------|--------------|------|
| [laion/clap-htsat-unfused](https://huggingface.co/laion/clap-htsat-unfused) | Contrastive Language-Audio Pre-training | Audio-text similarity | [🚀 Demo](https://huggingface.co/laion/clap-htsat-unfused) |

## 🏆 Featured Collections

### 🌟 Most Popular Models
The top models by downloads and community adoption:
- [bert-base-uncased](https://huggingface.co/bert-base-uncased) - The foundational BERT model
- [gpt2](https://huggingface.co/gpt2) - OpenAI's GPT-2 model
- [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) - Distilled BERT for efficiency
- [openai/clip-vit-base-patch32](https://huggingface.co/openai/clip-vit-base-patch32) - CLIP for vision-language tasks

### 🚀 State-of-the-Art Models
Cutting-edge models pushing the boundaries:
- [openai/whisper-large-v2](https://huggingface.co/openai/whisper-large-v2) - Best speech recognition
- [runwayml/stable-diffusion-v1-5](https://huggingface.co/runwayml/stable-diffusion-v1-5) - Leading image generation
- [facebook/musicgen-large](https://huggingface.co/facebook/musicgen-large) - Advanced music generation
- [mistralai/Mixtral-8x7B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x7B-Instruct-v0.1) - Top instruction-following LLM

## 📊 Model Comparison

### Large Language Models Comparison

| Model | Parameters | Open Source | Commercial Use | Best For |
|-------|------------|-------------|----------------|----------|
| GPT-J 6B | 6B | ✅ | ✅ | General text generation |
| BLOOM 7B | 7.1B | ✅ | ✅ | Multilingual tasks |
| Llama 2 Chat 7B | 7B | ✅ | ✅ | Conversational AI |
| Mixtral 8x7B | 46.7B | ✅ | ✅ | Complex reasoning |

### Vision Models Comparison

| Model | Type | Accuracy (ImageNet) | Parameters | Best For |
|-------|------|-------------------|------------|----------|
| ResNet-50 | CNN | 76.1% | 25.6M | General classification |
| ViT-Base | Transformer | 81.8% | 86M | Image understanding |
| EfficientNet-B7 | CNN | 84.4% | 66M | Efficient classification |
| DETR | Transformer | - | 41M | Object detection |

## 🛠️ Usage Examples

### Quick Start with Transformers

```python
# Text Classification
from transformers import pipeline
classifier = pipeline("sentiment-analysis", 
                     model="cardiffnlp/twitter-roberta-base-sentiment-latest")
result = classifier("I love this awesome repository!")

# Image Classification  
classifier = pipeline("image-classification", 
                     model="google/vit-base-patch16-224")
result = classifier("path/to/image.jpg")

# Speech Recognition
transcriber = pipeline("automatic-speech-recognition",
                      model="openai/whisper-large-v2")
result = transcriber("path/to/audio.wav")
```

### Using Specific Models

```python
# Question Answering
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")

# Image Captioning
from transformers import BlipProcessor, BlipForConditionalGeneration
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
```

## 🔍 How to Choose a Model

### For NLP Tasks
- **Text Classification**: Start with RoBERTa-based models for accuracy
- **Generation**: Use GPT-style models (GPT-J, BLOOM, Llama 2)
- **Question Answering**: BERT/RoBERTa fine-tuned on SQuAD
- **Multilingual**: XLM-R, mBERT, or BLOOM for cross-lingual tasks

### For Computer Vision
- **Image Classification**: ViT for state-of-the-art, ResNet for efficiency
- **Object Detection**: DETR for end-to-end, YOLO for speed
- **Image Generation**: Stable Diffusion for quality and control

### For Audio
- **Speech Recognition**: Whisper for multilingual, Wav2Vec2 for English
- **TTS**: SpeechT5 for quality, Tacotron for customization
- **Audio Classification**: AST for general audio understanding

## 📈 Performance Benchmarks

### NLP Benchmarks
- **GLUE**: General Language Understanding benchmark
- **SuperGLUE**: More challenging language understanding tasks  
- **SQuAD**: Reading comprehension benchmark
- **HellaSwag**: Commonsense reasoning

### Vision Benchmarks
- **ImageNet**: Image classification accuracy
- **COCO**: Object detection and segmentation
- **Open Images**: Large-scale object detection

### Audio Benchmarks
- **LibriSpeech**: Speech recognition accuracy
- **CommonVoice**: Multilingual speech recognition
- **AudioSet**: Audio classification tasks

## 🎯 Use Case Recommendations

### Content Creation
- **Text**: GPT-J 6B, BLOOM 7B
- **Images**: Stable Diffusion v1.5
- **Music**: MusicGen Large

### Business Applications  
- **Customer Support**: DialoGPT, RoBERTa sentiment analysis
- **Document Processing**: LayoutLM, TrOCR
- **Search & Retrieval**: CLIP, Sentence Transformers

### Research & Development
- **Multimodal**: CLIP, BLIP, ALIGN
- **Code**: CodeT5, CodeBERT, CodeGen
- **Scientific**: SciBERT, BioBERT, DistilRoBERTa

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Add new models**: Submit a PR with model details following our format
2. **Update benchmarks**: Share performance results and comparisons  
3. **Fix issues**: Report broken links or outdated information
4. **Improve descriptions**: Make model descriptions more accurate and helpful

### Contribution Guidelines

- Use the existing format for consistency
- Include direct Hugging Face Hub links
- Verify that demos work before submitting
- Add appropriate tags and categories
- Keep descriptions concise but informative

### Model Criteria

To be included, models should be:
- Publicly available on Hugging Face Hub
- Well-documented with clear use cases
- Actively maintained or widely adopted
- Demonstrate strong performance on benchmarks

## 📝 License

This repository is licensed under the Creative Commons Attribution 4.0 International Public License. See [LICENSE](LICENSE) for details.

© Jehoshua 2025

---

⭐ **Star this repository** if you find it helpful!

📫 **Questions or suggestions?** Open an issue or start a discussion.

🔗 **Share with others** who might benefit from this curated list.

---

*Last updated: August 2025*
