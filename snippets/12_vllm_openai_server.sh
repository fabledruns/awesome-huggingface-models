#!/usr/bin/env bash
# 12_vllm_openai_server.sh — Serve any HF model as an OpenAI-compatible endpoint
#
# vLLM ships an OpenAI-compatible HTTP server out of the box. Once it's
# running, any client that speaks the OpenAI Chat Completions API can talk
# to it: the official openai python SDK, LangChain, LlamaIndex, curl, etc.
#
# Dependencies:
#     pip install vllm
#     # On the client side:
#     pip install openai  # optional, only if you want the SDK
#
# Notes:
#     - --tensor-parallel-size N shards the model across N GPUs.
#     - --max-model-len caps the (prompt + generation) length. Lower it
#       to fit longer prompts in less KV-cache memory.
#     - --gpu-memory-utilization 0.9 (default 0.9) controls how much VRAM
#       vLLM pre-allocates for the KV cache. Lower if you share the GPU.
#     - --quantization awq, gptq, fp8, etc. — vLLM supports on-the-fly
#       quantization for many formats.
#     - For LoRA adapters: --enable-lora --lora-modules name=path/to/adapter
#     - For tool/function calling: use --enable-auto-tool-choice
#       --tool-call-parser hermes (model-dependent).

set -euo pipefail

MODEL_ID="Qwen/Qwen3-30B-A3B-Instruct-2507"
TP_SIZE=1
MAX_MODEL_LEN=32768
PORT=8000

echo ">>> Starting vLLM OpenAI-compatible server..."
echo ">>> Model: ${MODEL_ID}"
echo ">>> Endpoint: http://localhost:${PORT}/v1/chat/completions"

vllm serve "${MODEL_ID}" \
    --tensor-parallel-size "${TP_SIZE}" \
    --max-model-len "${MAX_MODEL_LEN}" \
    --port "${PORT}" &

VLLM_PID=$!
echo ">>> vLLM PID: ${VLLM_PID}"

# Wait for the server to come up (poll the /v1/models endpoint)
echo ">>> Waiting for server to be ready..."
for i in $(seq 1 60); do
    if curl -sf "http://localhost:${PORT}/v1/models" > /dev/null 2>&1; then
        echo ">>> Server ready (after ${i}s)"
        break
    fi
    sleep 1
done

echo ">>> Sending a test chat completion..."
curl -s "http://localhost:${PORT}/v1/chat/completions" \
    -H "Content-Type: application/json" \
    -d "{
        \"model\": \"${MODEL_ID}\",
        \"messages\": [{\"role\": \"user\", \"content\": \"Say hi in 5 words.\"}],
        \"max_tokens\": 32,
        \"temperature\": 0.7
    }" | python3 -m json.tool

# Cleanup
echo ">>> Stopping vLLM (PID ${VLLM_PID})..."
kill "${VLLM_PID}" 2>/dev/null || true
wait "${VLLM_PID}" 2>/dev/null || true
