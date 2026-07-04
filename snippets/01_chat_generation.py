"""01_chat_generation.py — Single-shot chat with proper chat template.

Run a Qwen3 MoE instruction-tuned model with the correct chat template,
bfloat16 weights, and auto device placement. Streams nothing — just prints
the final answer.

Dependencies:
    pip install transformers torch accelerate

GPU:
    Single 24GB GPU is enough for Qwen3-30B-A3B at bfloat16 (MoE, 3B active).

Notes:
    - Always use apply_chat_template(). Raw tokenizer(prompt) breaks
      instruction-tuned models because they expect structured turns with
      special tokens like <|im_start|>.
    - Pass torch_dtype=torch.bfloat16 explicitly. Default fp32 doubles VRAM.
    - Skip special tokens only on the *generated* slice to avoid echoing
      the prompt back.
"""
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

MODEL_ID = "Qwen/Qwen3-30B-A3B-Instruct-2507"


def main() -> None:
    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
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
        out = model.generate(
            inputs,
            max_new_tokens=512,
            do_sample=True,
            temperature=0.7,
        )
    # Slice off the prompt before decoding so we only print the answer.
    answer = tokenizer.decode(out[0][inputs.shape[-1]:], skip_special_tokens=True)
    print(answer)


if __name__ == "__main__":
    main()
