# Awesome Hugging Face Models

> A curated list of the best Hugging Face models for NLP, vision, audio, multimodal, and embeddings. Clean links, clear use cases, zero fluff.

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/github/stars/JehoshuaM/awesome-huggingface-models.svg?style=social)](https://github.com/JehoshuaM/awesome-huggingface-models/stargazers)

This repo highlights **production-ready**, **state-of-the-art**, and **community-trusted** models on the Hugging Face Hub. Models are grouped by task with short descriptions so you can pick fast. Updated through July 2026 to include GPT-OSS, DeepSeek V3.2, Kimi K2, GLM-4.6, Qwen3-Coder, FLUX.1-Kontext, and other recent drops.

---

## Table of Contents

- [NLP](#nlp)
  - [Large Language Models](#large-language-models)
  - [Reasoning Models](#reasoning-models)
  - [Text Classification](#text-classification)
  - [Named Entity Recognition](#named-entity-recognition)
  - [Question Answering](#question-answering)
  - [Summarization](#summarization)
  - [Translation](#translation)
  - [Code Models](#code-models)
  - [Embeddings](#embeddings)
  - [Reranking](#reranking)
- [Computer Vision](#computer-vision)
  - [Image Classification](#image-classification)
  - [Image Generation](#image-generation)
  - [Image Editing](#image-editing)
  - [Video Generation](#video-generation)
  - [Vision Tasks](#vision-tasks)
- [Audio](#audio)
  - [Speech Recognition](#speech-recognition)
  - [Text-to-Speech](#text-to-speech)
  - [Audio Classification](#audio-classification)
  - [Music Generation](#music-generation)
- [Multimodal](#multimodal)
  - [Vision-Language](#vision-language)
  - [Audio-Text](#audio-text)
- [Featured Models](#featured-models)
- [Recommended Picks (July 2026)](#recommended-picks-july-2026)
- [Snippets](#snippets)
- [Standalone Snippet Files](#standalone-snippet-files)
- [Common Mistakes](#common-mistakes)
- [Contributing](#contributing)
- [License](#license)

---

## NLP

### Large Language Models

| Model | Description | Size |
|-------|-------------|------|
| [openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) | OpenAI's open-weight reasoning model, Apache 2.0, fits on a single 80GB GPU | 117B |
| [openai/gpt-oss-20b](https://huggingface.co/openai/gpt-oss-20b) | Smaller GPT-OSS, faster, great for local/edge | 21B |
| [deepseek-ai/DeepSeek-V3.2](https://huggingface.co/deepseek-ai/DeepSeek-V3.2) | Sparse attention, strong agent and reasoning performance | 671B MoE |
| [deepseek-ai/DeepSeek-V3.1](https://huggingface.co/deepseek-ai/DeepSeek-V3.1) | Improved V3 with better tool calling and coding | 671B MoE |
| [deepseek-ai/DeepSeek-V3](https://huggingface.co/deepseek-ai/DeepSeek-V3) | Frontier-level general assistant, 128K context | 671B MoE |
| [moonshotai/Kimi-K2-Instruct](https://huggingface.co/moonshotai/Kimi-K2-Instruct) | Top open MoE for agentic workflows and creative writing | 1T MoE / 32B active |
| [zai-org/GLM-4.6](https://huggingface.co/zai-org/GLM-4.6) | Strong coding and agent model, beats GLM-4.5 across the board | 355B MoE |
| [Qwen/Qwen3-235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507) | Flagship Qwen3 MoE, Apache 2.0, top open benchmarks | 235B MoE / 22B active |
| [Qwen/Qwen3-30B-A3B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507) | Tiny MoE, runs on a single 24GB GPU, fast | 30B MoE / 3B active |
| [Qwen/Qwen3-32B](https://huggingface.co/Qwen/Qwen3-32B) | Strong reasoning plus multilingual, Apache 2.0 | 32B |
| [meta-llama/Llama-4-Scout-17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) | Fast multimodal instruction model, good for chat and agents | 17B MoE |
| [meta-llama/Llama-4-Maverick-17B-128E-Instruct](https://huggingface.co/meta-llama/Llama-4-Maverick-17B-128E-Instruct) | Stronger Llama 4 variant, handles text plus structured data | 17B MoE |
| [meta-llama/Meta-Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Meta-Llama-3.3-70B-Instruct) | Clean structured output, solid everyday reasoning | 70B |
| [meta-llama/Llama-3.1-8B-Instruct](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct) | Widely-deployed lightweight Llama, still a strong edge default | 8B |
| [google/gemma-3-27b-it](https://huggingface.co/google/gemma-3-27b-it) | Larger Gemma 3, stronger reasoning than 9B | 27B |
| [google/gemma-3-9b-it](https://huggingface.co/google/gemma-3-9b-it) | Lightweight, low resource, great for edge/local | 9B |
| [google/gemma-3n-E4B-it](https://huggingface.co/google/gemma-3n-E4B-it) | Mobile-first Gemma, runs on phones and laptops | ~4B active |
| [mistralai/Mistral-Small-3.1-24B-Instruct-2503](https://huggingface.co/mistralai/Mistral-Small-3.1-24B-Instruct-2503) | Best mid-size Mistral, strong coding, vision-capable | 24B |
| [mistralai/Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) | Efficient and fast for its size | 7B |
| [mistralai/Mixtral-8x22B-Instruct-v0.1](https://huggingface.co/mistralai/Mixtral-8x22B-Instruct-v0.1) | Apache 2.0 MoE, strong general reasoning | 141B MoE |
| [microsoft/Phi-4](https://huggingface.co/microsoft/Phi-4) | 14B dense, punches above its weight on math and reasoning | 14B |

---

### Reasoning Models

| Model | Description | Size |
|-------|-------------|------|
| [deepseek-ai/DeepSeek-R1-0528](https://huggingface.co/deepseek-ai/DeepSeek-R1-0528) | Updated R1, better reasoning and tool use than original | 671B MoE |
| [deepseek-ai/DeepSeek-R1](https://huggingface.co/deepseek-ai/DeepSeek-R1) | Original R1, rivals OpenAI o1 on math/code/logic | 671B MoE |
| [deepseek-ai/DeepSeek-R1-Distill-Qwen-32B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-32B) | Distilled R1, outperforms o1-mini, way more accessible | 32B |
| [deepseek-ai/DeepSeek-R1-Distill-Llama-8B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-8B) | Smallest R1 distill, solid reasoning at low compute | 8B |
| [Qwen/Qwen3-235B-A22B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507) | Thinking variant of Qwen3-235B, strong chain-of-thought | 235B MoE |
| [Qwen/Qwen3-30B-A3B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507) | Small thinking MoE, runs locally with good results | 30B MoE |
| [moonshotai/Kimi-K2-Thinking-0905](https://huggingface.co/moonshotai/Kimi-K2-Thinking-0905) | Kimi K2 with extended thinking, top open leaderboard scores | 1T MoE |
| [microsoft/Phi-4-reasoning-plus](https://huggingface.co/microsoft/Phi-4-reasoning-plus) | Refined Phi-4 with longer reasoning traces | 14B |

---

### Text Classification

| Model | Use Case |
|-------|---------|
| [cardiffnlp/twitter-roberta-base-sentiment-latest](https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment-latest) | Sentiment analysis |
| [facebook/bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli) | Zero-shot classification |
| [unitary/toxic-bert](https://huggingface.co/unitary/toxic-bert) | Toxicity detection |
| [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) | Financial sentiment |

---

### Named Entity Recognition

| Model | Language |
|-------|----------|
| [dbmdz/bert-large-cased-finetuned-conll03-english](https://huggingface.co/dbmdz/bert-large-cased-finetuned-conll03-english) | English |
| [xlm-roberta-large-finetuned-conll03-english](https://huggingface.co/xlm-roberta-large-finetuned-conll03-english) | Multilingual |
| [dslim/bert-base-NER](https://huggingface.co/dslim/bert-base-NER) | English, lightweight |

---

### Question Answering

| Model | Best For |
|-------|---------|
| [deepset/roberta-base-squad2](https://huggingface.co/deepset/roberta-base-squad2) | Extractive QA, English, strong baseline |
| [deepset/deberta-v3-base-squad2](https://huggingface.co/deepset/deberta-v3-base-squad2) | DeBERTa-v3 backbone, better long-context QA |

For open-ended QA, prefer an instruction-tuned LLM (Qwen3, GPT-OSS, DeepSeek-V3.2). They handle multi-hop and ambiguous questions far better than extractive models.

---

### Summarization

| Model | Type |
|-------|------|
| [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn) | News |
| [google/pegasus-xsum](https://huggingface.co/google/pegasus-xsum) | Extreme summarization |
| [sshleifer/distilbart-cnn-12-6](https://huggingface.co/sshleifer/distilbart-cnn-12-6) | Lightweight |

For modern use, prefer an instruction-tuned LLM (Qwen3, GPT-OSS, DeepSeek-V3.2). They summarize better than BART/Pegasus in nearly every benchmark.

---

### Translation

| Model | Languages |
|-------|----------|
| [facebook/m2m100_418M](https://huggingface.co/facebook/m2m100_418M) | 100+ |
| [google/mt5-large](https://huggingface.co/google/mt5-large) | 101 |
| [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M) | 200 languages, lightweight |
| [facebook/nllb-200-3.3B](https://huggingface.co/facebook/nllb-200-3.3B) | 200 languages, full quality |

---

### Code Models

| Model | Best For |
|-------|---------|
| [Qwen/Qwen3-Coder-480B-A35B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct) | Best open coder, 256K context, agentic coding, 119 languages |
| [Qwen/Qwen3-Coder-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct) | Smaller Qwen3-Coder, fits a single 24GB GPU, fast |
| [openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) | Strong general reasoning plus coding, Apache 2.0 |
| [deepseek-ai/DeepSeek-Coder-V2-Instruct](https://huggingface.co/deepseek-ai/DeepSeek-Coder-V2-Instruct) | Solid multilingual coder, 337B MoE |
| [Qwen/Qwen2.5-Coder-32B-Instruct](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct) | Strong multilingual coding |
| [bigcode/starcoder2-15b-instruct-v2.0](https://huggingface.co/bigcode/starcoder2-15b-instruct-v2.0) | Code completion, BigCode v2 |
| [microsoft/CodeBERT-base](https://huggingface.co/microsoft/CodeBERT-base) | Code search |

---

### Embeddings

| Model | Best For |
|-------|---------|
| [Alibaba-NLP/gte-modernbert-base](https://huggingface.co/Alibaba-NLP/gte-modernbert-base) | Fast, ModernBERT-based, long context, English |
| [nomic-ai/nomic-embed-text-v2-moe](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe) | Multilingual MoE, ~100 languages, open weights |
| [BAAI/bge-multilingual-gemma2](https://huggingface.co/BAAI/bge-multilingual-gemma2) | LLM-based, strong multilingual retrieval |
| [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) | Multilingual, multi-granularity (dense, sparse, multi-vector) |
| [intfloat/multilingual-e5-large-instruct](https://huggingface.co/intfloat/multilingual-e5-large-instruct) | Solid multilingual baseline |
| [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) | Tiny, fast, still great for cheap RAG |
| [dunzhang/stella_en_v5_instruct](https://huggingface.co/dunzhang/stella_en_v5_instruct) | English, instruction-tuned, top MTEB scores |

Pick MiniLM if you need speed and low memory. Pick gte-modernbert for a balanced default. Pick nomic-embed-v2 or bge-multilingual-gemma2 when you need multilingual coverage. Pick bge-m3 if you want hybrid dense+sparse retrieval in a single model.

---

### Reranking

| Model | Best For |
|-------|---------|
| [BAAI/bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3) | Default multilingual reranker, fast, cheap |
| [Alibaba-NLP/gte-multilingual-reranker-base](https://huggingface.co/Alibaba-NLP/gte-multilingual-reranker-base) | Strong multilingual reranker, pairs with gte embeddings |
| [nvidia/nv-rerankqa-mistral4b-v3](https://huggingface.co/nvidia/nv-rerankqa-mistral4b-v3) | Heavy reranker, top QA accuracy |
| [mixedbread-ai/mxbai-rerank-large-v1](https://huggingface.co/mixedbread-ai/mxbai-rerank-large-v1) | English reranker, strong out of the box |

A two-stage retrieve-then-rerank pipeline (embedding recall top-50, reranker top-5) beats a single embedding on quality almost every time.

---

## Computer Vision

### Image Classification

| Model | Architecture |
|-------|-------------|
| [google/vit-base-patch16-224](https://huggingface.co/google/vit-base-patch16-224) | Vision Transformer baseline, ImageNet-1K |
| [microsoft/resnet-50](https://huggingface.co/microsoft/resnet-50) | Classic ResNet, still a solid default |
| [google/efficientnet-b7](https://huggingface.co/google/efficientnet-b7) | High-accuracy EfficientNet, heavier |

### Image Generation

| Model | Description |
|-------|-------------|
| [black-forest-labs/FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) | Best open image generation model, 12B |
| [black-forest-labs/FLUX.1-schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell) | 1-4 step fast variant, great for prototyping |
| [stabilityai/stable-diffusion-3.5-large](https://huggingface.co/stabilityai/stable-diffusion-3.5-large) | 8B, improved image quality and typography |
| [stabilityai/stable-diffusion-3.5-medium](https://huggingface.co/stabilityai/stable-diffusion-3.5-medium) | 2.5B, lighter SD3.5 for consumer GPUs |
| [stabilityai/stable-diffusion-3-medium](https://huggingface.co/stabilityai/stable-diffusion-3-medium) | Original SD3 |
| [HiDream-Dev/HiDream-I1-Dev](https://huggingface.co/HiDream-Dev/HiDream-I1-Dev) | Compact open generator, competitive with FLUX |

### Image Editing

| Model | Description |
|-------|-------------|
| [black-forest-labs/FLUX.1-Kontext-dev](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev) | In-context image editing, prompt-based edits keep identity |
| [black-forest-labs/FLUX.1-Kontext-bpy](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-bpy) | Kontext variant, better prompt adherence |

### Video Generation

| Model | Description |
|-------|-------------|
| [Lightricks/LTX-Video](https://huggingface.co/Lightricks/LTX-Video) | Fast open text-to-video, runs on a single GPU |
| [Wan-AI/Wan2.1-T2V-14B](https://huggingface.co/Wan-AI/Wan2.1-T2V-14B) | Strong open T2V, 14B |
| [Wan-AI/Wan2.1-T2V-1.3B](https://huggingface.co/Wan-AI/Wan2.1-T2V-1.3B) | Tiny Wan2.1, good for quick drafts |

### Vision Tasks

| Model | Task |
|-------|------|
| [facebook/detr-resnet-50](https://huggingface.co/facebook/detr-resnet-50) | Object detection |
| [facebook/detr-resnet-50-panoptic](https://huggingface.co/facebook/detr-resnet-50-panoptic) | Panoptic segmentation |
| [IDEA-Research/GroundingDINO](https://huggingface.co/IDEA-Research/GroundingDINO) | Open-vocab detection |
| [nvidia/segformer-b5-finetuned-ade-640-640](https://huggingface.co/nvidia/segformer-b5-finetuned-ade-640-640) | Semantic segmentation |
| [google/siglip2-so400m-patch16-naflex](https://huggingface.co/google/siglip2-so400m-patch16-naflex) | Image-text similarity, better than CLIP |
| [microsoft/trocr-base-printed](https://huggingface.co/microsoft/trocr-base-printed) | Printed OCR |
| [microsoft/trocr-large-handwritten](https://huggingface.co/microsoft/trocr-large-handwritten) | Handwritten OCR |

---

## Audio

### Speech Recognition

| Model | Description |
|-------|-------------|
| [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo) | Faster Whisper Large v3, 8x speedup, near-identical accuracy |
| [openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) | Best open ASR, full quality |
| [distil-whisper/distil-large-v3](https://huggingface.co/distil-whisper/distil-large-v3) | Distilled Whisper, fast ASR |
| [nvidia/parakeet-tdt-0.6b-v2](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v2) | Very fast ASR, top English accuracy |
| [nvidia/canary-1b-flash](https://huggingface.co/nvidia/canary-1b-flash) | Multilingual ASR plus translation, 1B |
| [facebook/seamless-m4t-v2-large](https://huggingface.co/facebook/seamless-m4t-v2-large) | Speech to/from text, multilingual |

### Text-to-Speech

| Model | Description |
|-------|-------------|
| [microsoft/speecht5_tts](https://huggingface.co/microsoft/speecht5_tts) | Lightweight TTS, fine-tunable per speaker |
| [suno/bark](https://huggingface.co/suno/bark) | Highly expressive TTS with nonverbal sounds |
| [Sesame/csm-1b](https://huggingface.co/Sesame/csm-1b) | Conversational speech model, natural TTS |
| [nari-labs/Dia-1.6B](https://huggingface.co/nari-labs/Dia-1.6B) | Expressive TTS with voice cloning |

### Audio Classification

| Model | Task |
|-------|------|
| [MIT/ast-finetuned-audioset-10-10-0.4593](https://huggingface.co/MIT/ast-finetuned-audioset-10-10-0.4593) | Audio event classification (AudioSet) |
| [superb/wav2vec2-base-superb-er](https://huggingface.co/superb/wav2vec2-base-superb-er) | Emotion recognition |

### Music Generation

| Model | Description |
|-------|-------------|
| [facebook/musicgen-large](https://huggingface.co/facebook/musicgen-large) | Text-to-music, stereo-capable |
| [facebook/musicgen-stereo-large](https://huggingface.co/facebook/musicgen-stereo-large) | Native stereo output, higher fidelity |

---

## Multimodal

### Vision-Language

| Model | Capability |
|-------|-----------|
| [Qwen/Qwen3-VL-235B-A22B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct) | Top open vision-language model, charts/docs/video |
| [Qwen/Qwen3-VL-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-30B-A3B-Instruct) | Smaller Qwen3-VL, single-GPU friendly |
| [meta-llama/Llama-4-Scout-17B-16E-Instruct](https://huggingface.co/meta-llama/Llama-4-Scout-17B-16E-Instruct) | Vision plus language, real-time inference |
| [mistralai/Pixtral-12B-2409](https://huggingface.co/mistralai/Pixtral-12B-2409) | Compact vision-language, strong OCR and charts |
| [mistralai/Pixtral-Large-Instruct-2411](https://huggingface.co/mistralai/Pixtral-Large-Instruct-2411) | Larger Pixtral, frontier-level multimodal |
| [Qwen/Qwen2.5-VL-72B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-72B-Instruct) | Visual reasoning, strong on charts and docs |
| [openai/clip-vit-large-patch14](https://huggingface.co/openai/clip-vit-large-patch14) | Image-text similarity, classic baseline |
| [Salesforce/blip-image-captioning-large](https://huggingface.co/Salesforce/blip-image-captioning-large) | Image captioning |
| [microsoft/Florence-2-large](https://huggingface.co/microsoft/Florence-2-large) | Dense vision tasks: captioning, grounding, OCR |
| [google/paligemma2-3b-pt-448](https://huggingface.co/google/paligemma2-3b-pt-448) | Fine-tunable VLM base, PaliGemma 2 |
| [microsoft/Phi-4-multimodal-instruct](https://huggingface.co/microsoft/Phi-4-multimodal-instruct) | Vision plus audio plus text in a 5.6B model |

### Audio-Text

| Model | Capability |
|-------|-----------|
| [laion/clap-htsat-unfused](https://huggingface.co/laion/clap-htsat-unfused) | Audio-text similarity, retrieval and zero-shot classification |

---

## Featured Models

### Most Downloaded (all time)

| Model | Why it matters |
|-------|---------------|
| [bert-base-uncased](https://huggingface.co/bert-base-uncased) | Foundational encoder, still used for fine-tuning baselines |
| [gpt2](https://huggingface.co/gpt2) | Original GPT-2, reference decoder for teaching |
| [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) | Distilled BERT, ~40% smaller, ~60% faster |
| [openai/clip-vit-base-patch32](https://huggingface.co/openai/clip-vit-base-patch32) | Baseline image-text model, still widely deployed |

### State-of-the-Art (July 2026)

| Model | Category |
|-------|----------|
| [openai/gpt-oss-120b](https://huggingface.co/openai/gpt-oss-120b) | Open LLM |
| [deepseek-ai/DeepSeek-V3.2](https://huggingface.co/deepseek-ai/DeepSeek-V3.2) | Open LLM |
| [moonshotai/Kimi-K2-Instruct](https://huggingface.co/moonshotai/Kimi-K2-Instruct) | Open LLM |
| [zai-org/GLM-4.6](https://huggingface.co/zai-org/GLM-4.6) | Open LLM |
| [Qwen/Qwen3-Coder-480B-A35B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-480B-A35B-Instruct) | Code |
| [Qwen/Qwen3-VL-235B-A22B-Instruct](https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct) | Multimodal |
| [black-forest-labs/FLUX.1-Kontext-dev](https://huggingface.co/black-forest-labs/FLUX.1-Kontext-dev) | Image editing |
| [openai/whisper-large-v3-turbo](https://huggingface.co/openai/whisper-large-v3-turbo) | ASR |
| [nomic-ai/nomic-embed-text-v2-moe](https://huggingface.co/nomic-ai/nomic-embed-text-v2-moe) | Embeddings |

---

## Recommended Picks (July 2026)

- **Best Open LLM (frontier)** -> DeepSeek-V3.2 or Kimi-K2-Instruct
- **Best Reasoning Model** -> DeepSeek-R1-0528 or Kimi-K2-Thinking-0905
- **Best Mid-Size LLM (single GPU)** -> Qwen3-30B-A3B-Instruct-2507 or Mistral-Small-3.1-24B
- **Best Lightweight LLM** -> gpt-oss-20b, Gemma 3 9B, or Phi-4
- **Best Code Model** -> Qwen3-Coder-480B-A35B-Instruct (Qwen3-Coder-30B for local)
- **Best Multimodal** -> Qwen3-VL-235B-A22B-Instruct or Pixtral-Large-2411
- **Best Image Generation** -> FLUX.1-dev
- **Best Image Editing** -> FLUX.1-Kontext-dev
- **Best ASR** -> Whisper Large v3 Turbo (balanced) or Parakeet-TDT-0.6B-v2 (speed)
- **Best TTS** -> Sesame/csm-1b (conversational) or nari-labs/Dia-1.6B (voice cloning)
- **Best Embeddings** -> nomic-embed-text-v2-moe (multilingual), gte-modernbert-base (English)
- **Best Reranker** -> bge-reranker-v2-m3
- **Best Open Reasoning on a Budget** -> DeepSeek-R1-Distill-Qwen-32B or Qwen3-30B-A3B-Thinking-2507

---

## Snippets

### Text generation with chat template

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "Qwen/Qwen3-30B-A3B-Instruct-2507"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

messages = [
    {"role": "system", "content": "You are a helpful coding assistant."},
    {"role": "user", "content": "Refactor this Python function to use pathlib."},
]
inputs = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True, return_tensors="pt"
).to(model.device)

with torch.no_grad():
    out = model.generate(inputs, max_new_tokens=512, do_sample=True, temperature=0.7)
print(tokenizer.decode(out[0][inputs.shape[-1]:], skip_special_tokens=True))
```

### Streaming output with Transformers

```python
from transformers import TextIteratorStreamer
from threading import Thread

streamer = TextIteratorStreamer(tokenizer, skip_prompt=True, skip_special_tokens=True)
gen_kwargs = dict(inputs=inputs, streamer=streamer, max_new_tokens=512)
Thread(target=model.generate, kwargs=gen_kwargs).start()

for text in streamer:
    print(text, end="", flush=True)
```

### Fast inference with vLLM

```python
from vllm import LLM, SamplingParams

llm = LLM(model="openai/gpt-oss-120b", tensor_parallel_size=1, dtype="bfloat16")
prompts = ["Explain backpropagation in 3 sentences."]
out = llm.generate(prompts, SamplingParams(temperature=0.7, max_tokens=200))
print(out[0].outputs[0].text)
```

### Embeddings + rerank pipeline (RAG)

```python
from sentence_transformers import SentenceTransformer
from FlagEmbedding import FlagReranker

docs = ["Paris is the capital of France.", "Rome is the capital of Italy.", "Berlin is the capital of Germany."]
query = "What is the capital of France?"

embedder = SentenceTransformer("Alibaba-NLP/gte-modernbert-base")
doc_embs = embedder.encode(docs, normalize_embeddings=True)
q_emb = embedder.encode([query], normalize_embeddings=True)

# Stage 1: retrieve top-3 by cosine similarity
scores = (doc_embs @ q_emb.T).ravel()
top_idx = scores.argsort()[::-1][:3]
candidates = [docs[i] for i in top_idx]

# Stage 2: rerank with a cross-encoder
reranker = FlagReranker("BAAI/bge-reranker-v2-m3", use_fp16=True)
pairs = [[query, c] for c in candidates]
rerank_scores = reranker.compute_score(pairs, normalize=True)

best = sorted(zip(candidates, rerank_scores), key=lambda x: -x[1])[0]
print(best)
```

### Whisper Turbo batched transcription

```python
from transformers import pipeline

asr = pipeline(
    "automatic-speech-recognition",
    model="openai/whisper-large-v3-turbo",
    chunk_length_s=30,
    device="cuda",
)
result = asr("meeting.wav", return_timestamps=True, batch_size=8)
print(result["text"])
```

### FLUX.1 image generation

```python
from diffusers import FluxPipeline
import torch

pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-dev", torch_dtype=torch.bfloat16)
pipe.to("cuda")
image = pipe(
    prompt="a photo of a red panda wearing a tiny chef hat, soft natural light",
    num_inference_steps=28,
    guidance_scale=3.5,
    height=1024, width=1024,
).images[0]
image.save("panda.png")
```

### FLUX.1-Kontext image editing

```python
from diffusers import FluxKontextPipeline
from PIL import Image
import torch

pipe = FluxKontextPipeline.from_pretrained(
    "black-forest-labs/FLUX.1-Kontext-dev", torch_dtype=torch.bfloat16
).to("cuda")

input_image = Image.open("portrait.png").convert("RGB")
edited = pipe(
    image=input_image,
    prompt="add round glasses and a yellow beanie",
    num_inference_steps=20,
    guidance_scale=2.5,
).images[0]
edited.save("portrait_edited.png")
```

### LoRA fine-tuning with PEFT

```python
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Meta-Llama-3.3-70B-Instruct",
    device_map="auto", torch_dtype=torch.bfloat16,
)
config = LoraConfig(
    r=16, lora_alpha=32, lora_dropout=0.05,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
    task_type="CAUSAL_LM",
)
model = get_peft_model(model, config)
model.print_trainable_parameters()  # ~0.1% of params
```

### Quantized loading (4-bit) with bitsandbytes

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig
import torch

bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
    bnb_4bit_use_double_quant=True,
)
model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen3-235B-A22B-Instruct-2507",
    quantization_config=bnb_config,
    device_map="auto",
)
```

### Run GGUF locally with llama.cpp

```bash
# Download a quantized GGUF
huggingface-cli download Qwen/Qwen3-30B-A3B-Instruct-2507-GGUF \
  Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf --local-dir ./models

# Run inference
llama-cli -m ./models/Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf \
  -p "Write a haiku about distributed systems" -n 128
```

### Qwen3-VL multimodal inference

```python
from transformers import AutoProcessor, AutoModelForVision2Seq
import torch
from PIL import Image

model_id = "Qwen/Qwen3-VL-30B-A3B-Instruct"
processor = AutoProcessor.from_pretrained(model_id)
model = AutoModelForVision2Seq.from_pretrained(
    model_id, torch_dtype=torch.bfloat16, device_map="auto"
)

image = Image.open("chart.png").convert("RGB")
messages = [
    {"role": "user", "content": [
        {"type": "image", "image": image},
        {"type": "text", "text": "Summarize this chart in 3 bullet points."},
    ]},
]
text = processor.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = processor(text=text, images=image, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=256)
print(processor.decode(out[0][inputs["input_ids"].shape[-1]:], skip_special_tokens=True))
```

### vLLM OpenAI-compatible server

```bash
# Serve any supported HF model with an OpenAI-compatible API
vllm serve Qwen/Qwen3-30B-A3B-Instruct-2507 \
  --tensor-parallel-size 1 \
  --max-model-len 32768 \
  --port 8000

# Then call it like the OpenAI API
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "Qwen/Qwen3-30B-A3B-Instruct-2507",
    "messages": [{"role": "user", "content": "Say hi in 5 words."}],
    "max_tokens": 32
  }'
```

---

## Standalone Snippet Files

Every snippet above is also available as a runnable standalone file in [`snippets/`](./snippets). Each file is self-contained: install the listed deps, then `python snippets/<name>.py`.

| File | What it does | Key deps |
|------|--------------|---------|
| [`snippets/01_chat_generation.py`](./snippets/01_chat_generation.py) | Single-shot chat with proper template + `torch.bfloat16` | `transformers`, `torch` |
| [`snippets/02_streaming.py`](./snippets/02_streaming.py) | Token-by-token streaming via `TextIteratorStreamer` | `transformers`, `torch` |
| [`snippets/03_vllm_inference.py`](./snippets/03_vllm_inference.py) | Batched high-throughput inference with vLLM | `vllm` |
| [`snippets/04_embeddings_rerank_rag.py`](./snippets/04_embeddings_rerank_rag.py) | Two-stage retrieve-then-rerank RAG pipeline | `sentence-transformers`, `FlagEmbedding` |
| [`snippets/05_whisper_turbo.py`](./snippets/05_whisper_turbo.py) | Batched long-audio transcription with Whisper Turbo | `transformers`, `torch` |
| [`snippets/06_flux_image_gen.py`](./snippets/06_flux_image_gen.py) | Text-to-image generation with FLUX.1-dev | `diffusers`, `torch` |
| [`snippets/07_flux_kontext_edit.py`](./snippets/07_flux_kontext_edit.py) | In-context image editing with FLUX.1-Kontext | `diffusers`, `torch`, `Pillow` |
| [`snippets/08_lora_peft.py`](./snippets/08_lora_peft.py) | Wrap a causal LM with LoRA via PEFT | `peft`, `transformers`, `torch` |
| [`snippets/09_bitsandbytes_4bit.py`](./snippets/09_bitsandbytes_4bit.py) | 4-bit NF4 quantized loading | `transformers`, `bitsandbytes`, `torch` |
| [`snippets/10_llama_cpp_gguf.sh`](./snippets/10_llama_cpp_gguf.sh) | Download a GGUF and run it with `llama-cli` | `huggingface-hub`, `llama.cpp` |
| [`snippets/11_qwen3_vl_multimodal.py`](./snippets/11_qwen3_vl_multimodal.py) | Vision-language Q&A with Qwen3-VL | `transformers`, `torch`, `Pillow` |
| [`snippets/12_vllm_openai_server.sh`](./snippets/12_vllm_openai_server.sh) | Serve an HF model as an OpenAI-compatible endpoint | `vllm`, `curl` |

---

## Common Mistakes

### 1. Skipping the chat template

Using raw `tokenizer(prompt)` instead of `apply_chat_template()` breaks instruction-tuned models. They were trained on structured turns with `<|im_start|>`, `<|start_header_id|>`, or similar special tokens. Without the template, the model gets a flat string and produces worse or weirdly formatted output. Always use:

```python
tokenizer.apply_chat_template(messages, add_generation_prompt=True, return_tensors="pt")
```

### 2. Loading large models without quantization

A 70B model in fp16 needs ~140GB of VRAM. On a single 24GB GPU, use 4-bit quantization (BitsAndBytesConfig with `load_in_4bit=True`) or GGUF (Q4_K_M). You can also pick a smaller MoE like Qwen3-30B-A3B, which only activates 3B parameters per token.

### 3. Using `device_map="auto"` with multi-GPU pipelines

`device_map="auto"` works for inference, but for vLLM or TensorRT-LLM you want explicit `tensor_parallel_size=N`. Auto-sharding across GPUs through `device_map` is slow because every layer crossing triggers a sync. For production, use vLLM with `--tensor-parallel-size N`.

### 4. Forgetting `torch_dtype` and loading in fp32

By default, Transformers loads weights in fp32. That doubles memory and halves throughput. Always pass `torch_dtype=torch.bfloat16` (or `float16`) when loading inference models.

### 5. Whisper on long audio without chunking

Whisper has a 30-second window. Pass an hour-long file straight to `pipeline(...)` and you get truncated or hallucinated output. Set `chunk_length_s=30` and `return_timestamps=True`, then batch with `batch_size=8` for speed.

### 6. Treating embeddings as cosine-optional

Many embedding models (gte, bge, nomic) output vectors that should be L2-normalized before similarity search. Skip the `normalize_embeddings=True` flag in `SentenceTransformer.encode()` and recall numbers quietly drop. Always check the model card.

### 7. Using CLIP for everything visual

CLIP is from 2021. For retrieval, SigLIP2 (`google/siglip2-so400m-patch16-naflex`) is stronger on every benchmark and supports variable image sizes. For captioning or VQA, use Qwen3-VL or Pixtral. CLIP is still fine for cheap image-text similarity baselines.

### 8. Trusting model card benchmarks without replication

Vendor benchmarks cherry-pick. Cross-check on LMSYS Arena, OpenCompass, or Artificial Analysis before picking a model for production. A model that wins HumanEval by 5 points might lose 10 points on your real-world task distribution.

### 9. Generating without `max_new_tokens`

Some inference setups default `max_new_tokens` to a small value (like 20) or to the full context window. Set it explicitly. Also set `do_sample=False` if you want deterministic output for tests and evals.

### 10. Fine-tuning the full model when LoRA would do

Full fine-tuning of a 7B model needs ~80GB+ of VRAM and three optimizer states per parameter. LoRA or QLoRA trains 0.1% of parameters and matches full-FT on most task-specific fine-tunes. Use PEFT unless you have a clear reason not to.

### 11. Not setting `padding_side="left"` for batched generation

Decoder-only models need left padding so the last token is the real last token. Default right-padding breaks batched generation silently. Set `tokenizer.padding_side = "left"` before batching.

### 12. Ignoring eos_token and watching the model ramble

If you change the tokenizer or strip special tokens, the model may never emit EOS and ramble to `max_new_tokens`. Always verify `eos_token_id` is set on both the tokenizer and the model config, and pass it explicitly to `generate()` if you customized templates.

### 13. Treating MoE size labels as dense equivalents

Qwen3-30B-A3B has 30B total parameters but only 3B active per token. VRAM is set by total params, throughput is set by active params. You need ~60GB VRAM to load Q4 but only get 3B-model-class latency. Read the `A<active>` suffix carefully when budgeting.

### 14. Comparing reasoning models without thinking budget

DeepSeek-R1 and Kimi-K2-Thinking emit `<think>...</think>` blocks that consume output tokens. If you set `max_new_tokens=256`, the model spends it all on thinking and never answers. Use 4K+ for reasoning models, or strip thinking tokens from your downstream parser.

### 15. Using the original FLUX.1-dev pipeline for editing

FLUX.1-dev is text-to-image only. For in-context image editing, use `FluxKontextPipeline` with FLUX.1-Kontext-dev. Trying to coax edits out of FLUX.1-dev with img2img gives blurry results and identity drift.

### 16. Mixing Qwen3-VL image input formats

Qwen3-VL expects the image as a `PIL.Image` (or list of URLs) passed through `processor(text=..., images=..., return_tensors="pt")`, not as a base64 string in the chat content. If you hand-craft the message dict with raw image bytes, the processor silently drops the image and the model hallucinates. Use the `{"type": "image", "image": pil_image}` content item and let the processor do the encoding.

---

## Contributing

PRs welcome.

Rules:
- Real models only, no vaporware
- HF links required
- Short and accurate descriptions
- No dead or deprecated models
- Prefer Apache 2.0 or MIT where possible

See [CONTRIBUTING.md](./CONTRIBUTING.md) for the full guide.

---

## License

Creative Commons Attribution 4.0 International, see [LICENSE.md](./LICENSE.md).

© Jehoshua 2026

Star the repo if it helped.
Last updated: July 2026
