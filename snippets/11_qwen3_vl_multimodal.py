"""11_qwen3_vl_multimodal.py — Vision-language Q&A with Qwen3-VL.

Qwen3-VL is the current top open vision-language model. It handles
charts, documents, screenshots, and short video clips. This example
loads the 30B-A3B variant (single-GPU friendly) and runs a single
image+text turn.

Dependencies:
    pip install transformers torch accelerate Pillow
    # Optional: pip install qwen-vl-utils  # for advanced image preprocessing

GPU:
    - 30B-A3B at bfloat16: ~24GB VRAM (MoE, 3B active per token).
    - 235B-A22B at bfloat16: ~120GB VRAM (multi-GPU required).
    - For <24GB, use BitsAndBytesConfig(load_in_4bit=True) — see
      09_bitsandbytes_4bit.py.

Notes:
    - Qwen3-VL expects images as PIL.Image objects (or URLs / file paths)
      passed through processor(text=..., images=..., return_tensors="pt").
      Do NOT hand-craft message dicts with raw base64 — the processor
      silently drops them. See Common Mistake #16 in README.
    - AutoModelForVision2Seq is the right class for Qwen3-VL. If it fails
      on a different VLM, try AutoModelForCausalLM with trust_remote_code.
    - For video input, pass a list of frames as images and use the
      {"type": "video", "video": [frame1, frame2, ...]} content type.
"""
import torch
from PIL import Image
from transformers import AutoProcessor, AutoModelForVision2Seq

MODEL_ID = "Qwen/Qwen3-VL-30B-A3B-Instruct"
IMAGE_PATH = "chart.png"
PROMPT = "Summarize this chart in 3 bullet points."


def main() -> None:
    processor = AutoProcessor.from_pretrained(MODEL_ID)
    model = AutoModelForVision2Seq.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )

    image = Image.open(IMAGE_PATH).convert("RGB")
    messages = [
        {
            "role": "user",
            "content": [
                {"type": "image", "image": image},
                {"type": "text", "text": PROMPT},
            ],
        },
    ]
    text = processor.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = processor(
        text=text, images=image, return_tensors="pt"
    ).to(model.device)

    with torch.no_grad():
        out = model.generate(**inputs, max_new_tokens=256)

    # Slice off the prompt before decoding so we only print the answer.
    input_len = inputs["input_ids"].shape[-1]
    answer = processor.decode(out[0][input_len:], skip_special_tokens=True)
    print(answer)


if __name__ == "__main__":
    main()
