"""06_flux_image_gen.py — Text-to-image generation with FLUX.1-dev.

FLUX.1-dev is the best open image generation model as of mid-2026. 12B
rectified-flow transformer, Apache-2.0-adjacent (non-commercial OK).

Dependencies:
    pip install diffusers torch accelerate
    # Optional: pip install sentencepiece protobuf (for the T5 text encoder)

GPU:
    - 24GB VRAM is enough at bfloat16.
    - For <16GB VRAM: add `pipe.enable_model_cpu_offload()` and remove
      `pipe.to("cuda")`. Trades speed for memory.
    - For <12GB VRAM: use FLUX.1-schnell (1-4 steps) and quantize the
      text encoder.

Notes:
    - guidance_scale=3.5 is the FLUX.1-dev sweet spot. Lower = more
      creative, higher = more prompt-faithful but artifact-prone.
    - num_inference_steps=28 is the recommended default. 20 is fine for
      draft quality, 50 for final.
    - For prompt-based image EDITING (not generation), use
      FluxKontextPipeline instead — see 07_flux_kontext_edit.py.
"""
import torch
from diffusers import FluxPipeline

MODEL_ID = "black-forest-labs/FLUX.1-dev"
PROMPT = "a photo of a red panda wearing a tiny chef hat, soft natural light"
OUTPUT_PATH = "panda.png"


def main() -> None:
    pipe = FluxPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.bfloat16,
    )
    pipe.to("cuda")

    image = pipe(
        prompt=PROMPT,
        num_inference_steps=28,
        guidance_scale=3.5,
        height=1024,
        width=1024,
    ).images[0]
    image.save(OUTPUT_PATH)
    print(f"Saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
