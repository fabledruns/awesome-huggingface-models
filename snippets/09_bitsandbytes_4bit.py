"""09_bitsandbytes_4bit.py — 4-bit NF4 quantized loading.

bitsandbytes 4-bit NF4 quantization lets you load a model in ~25% of its
fp16 VRAM footprint with negligible quality loss. Pairs with LoRA to make
"QLoRA" — fine-tuning a 70B model on a single 24GB consumer GPU.

Dependencies:
    pip install transformers torch bitsandbytes accelerate

GPU:
    - Qwen3-235B-A22B-Instruct-2507 in 4-bit needs ~120GB VRAM total
      (still a lot, because 235B * 0.5 bytes/param = ~117GB). For a
      single-GPU example, swap MODEL_ID for a 30-70B model.
    - For inference, just call .generate() on the returned model — same
      API as bfloat16 loading.
    - For training (QLoRA), wrap with peft.get_peft_model after this.

Notes:
    - bnb_4bit_quant_type="nf4" is the recommended quantization (NormalFloat
      4-bit). "fp4" is also supported but slightly worse.
    - bnb_4bit_compute_dtype=torch.bfloat16 controls the compute dtype
      inside the dequantized matmul. bfloat16 is faster; float16 is more
      portable to older GPUs.
    - bnb_4bit_use_double_quant=True quantizes the quantization constants
      themselves, saving ~0.4 bits/param with no quality loss.
"""
import torch
from transformers import AutoModelForCausalLM, BitsAndBytesConfig

MODEL_ID = "Qwen/Qwen3-235B-A22B-Instruct-2507"


def main() -> None:
    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        quantization_config=bnb_config,
        device_map="auto",
    )
    print(f"Loaded {MODEL_ID} in 4-bit NF4.")
    print(f"Model device map: {model.hf_device_map}")


if __name__ == "__main__":
    main()
