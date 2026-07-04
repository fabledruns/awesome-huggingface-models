"""08_lora_peft.py — Wrap a causal LM with LoRA via PEFT.

LoRA (Low-Rank Adaptation) freezes the base model and trains small rank-r
matrices on top of q/k/v/o (and optionally MLP) projections. Typically
trains 0.1-1% of parameters with no measurable accuracy drop on
task-specific fine-tunes.

Dependencies:
    pip install peft transformers torch accelerate bitsandbytes

GPU:
    - This example loads Meta-Llama-3.3-70B in bfloat16, which needs
      ~140GB VRAM. On a single 24GB GPU, add `quantization_config=
      BitsAndBytesConfig(load_in_4bit=True, ...)` to load in 4-bit QLoRA.
    - See 09_bitsandbytes_4bit.py for the BNB config pattern.

Notes:
    - target_modules=["q_proj","k_proj","v_proj","o_proj"] is the standard
      attention-only target set. For better quality, also add MLP:
      target_modules=["q_proj","k_proj","v_proj","o_proj","gate_proj",
                      "up_proj","down_proj"]
    - r=16, alpha=32 is the standard "sweet spot" — alpha is typically 2*r.
    - After training, save with model.save_pretrained("lora_out/") — this
      writes only the LoRA adapter weights (~50MB), not the base model.
"""
import torch
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM

MODEL_ID = "meta-llama/Meta-Llama-3.3-70B-Instruct"


def main() -> None:
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        device_map="auto",
        torch_dtype=torch.bfloat16,
    )
    config = LoraConfig(
        r=16,
        lora_alpha=32,
        lora_dropout=0.05,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, config)
    model.print_trainable_parameters()  # ~0.1% of params


if __name__ == "__main__":
    main()
