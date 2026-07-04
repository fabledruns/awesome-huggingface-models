#!/usr/bin/env bash
# 10_llama_cpp_gguf.sh — Download a GGUF and run it with llama.cpp
#
# GGUF is the quantized file format used by llama.cpp. A Q4_K_M quant of
# a 30B model is typically ~18GB and runs at ~30 tokens/sec on a single
# modern consumer GPU (or even CPU-only at ~5-10 tok/s).
#
# Dependencies:
#     pip install -U "huggingface_hub[cli]"
#     # Build llama.cpp: https://github.com/ggerganov/llama.cpp#build
#     # On Ubuntu: apt install build-essential cmake git
#     # Then: git clone https://github.com/ggerganov/llama.cpp && \
#     #       cd llama.cpp && cmake -B build && cmake --build build -j
#
# Notes:
#     - Q4_K_M is the recommended balance of size/quality. Q5_K_M is
#       slightly better quality, Q3_K_M is smaller and noticeably worse.
#     - For interactive chat, use llama-cli with -cnv flag.
#     - For OpenAI-compatible HTTP server: llama-server -m model.gguf
#     - llama.cpp auto-detects CUDA/Metal. For CUDA, build with
#       -DGGML_CUDA=ON.

set -euo pipefail

MODEL_REPO="Qwen/Qwen3-30B-A3B-Instruct-2507-GGUF"
MODEL_FILE="Qwen3-30B-A3B-Instruct-2507-Q4_K_M.gguf"
LOCAL_DIR="./models"
PROMPT="Write a haiku about distributed systems"
MAX_TOKENS=128

echo ">>> Downloading ${MODEL_FILE} from ${MODEL_REPO}..."
huggingface-cli download "${MODEL_REPO}" "${MODEL_FILE}" \
    --local-dir "${LOCAL_DIR}"

echo ">>> Running inference with llama-cli..."
llama-cli \
    -m "${LOCAL_DIR}/${MODEL_FILE}" \
    -p "${PROMPT}" \
    -n "${MAX_TOKENS}" \
    --color \
    --temperature 0.7

# For chat mode, replace llama-cli flags with:
#   llama-cli -m "${LOCAL_DIR}/${MODEL_FILE}" -cnv
#
# For an OpenAI-compatible HTTP server:
#   llama-server -m "${LOCAL_DIR}/${MODEL_FILE}" --port 8080
# Then curl http://localhost:8080/v1/chat/completions -H 'Content-Type: application/json' \
#     -d '{"model":"local","messages":[{"role":"user","content":"hi"}]}'
