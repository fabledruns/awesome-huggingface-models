"""03_vllm_inference.py — Batched high-throughput inference with vLLM.

vLLM is 5-20x faster than raw transformers for throughput-bound workloads
because of paged KV cache and continuous batching. Use it for production
serving, batch eval, or any time you need to process many prompts.

Dependencies:
    pip install vllm

GPU:
    - gpt-oss-120b fits a single 80GB GPU at bfloat16.
    - For 70B-class dense models on smaller GPUs, use --tensor-parallel-size N
      across N GPUs, or quantize.

Notes:
    - tensor_parallel_size=N shards the model across N GPUs. Use this over
      device_map="auto" — auto-sharding through HF Transformers is much
      slower because of cross-GPU sync per layer.
    - SamplingParams accepts temperature, top_p, top_k, max_tokens, etc.
    - For an OpenAI-compatible HTTP server, see 12_vllm_openai_server.sh.
"""
from vllm import LLM, SamplingParams

MODEL_ID = "openai/gpt-oss-120b"


def main() -> None:
    llm = LLM(
        model=MODEL_ID,
        tensor_parallel_size=1,
        dtype="bfloat16",
    )

    prompts = [
        "Explain backpropagation in 3 sentences.",
        "Write a Python decorator that retries a function on exception.",
        "What is the difference between TCP and UDP?",
    ]
    sampling = SamplingParams(temperature=0.7, max_tokens=200)
    outputs = llm.generate(prompts, sampling)

    for i, out in enumerate(outputs, 1):
        print(f"--- Prompt {i} ---")
        print(out.prompt)
        print("->", out.outputs[0].text)
        print()


if __name__ == "__main__":
    main()
