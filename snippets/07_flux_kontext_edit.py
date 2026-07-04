"""07_flux_kontext_edit.py — In-context image editing with FLUX.1-Kontext.

FLUX.1-Kontext is a separate model from FLUX.1-dev. It takes an image AND
a prompt, and edits the image while preserving identity (faces, objects,
style). Trying to coax edits out of plain FLUX.1-dev with img2img gives
blurry results and identity drift — see Common Mistake #15 in README.

Dependencies:
    pip install diffusers torch accelerate Pillow

GPU:
    - 24GB VRAM at bfloat16.
    - Use pipe.enable_model_cpu_offload() for <16GB.

Notes:
    - guidance_scale=2.5 for Kontext (lower than dev's 3.5).
    - The image argument accepts a PIL.Image, a list of PIL.Images, or a URL.
    - For multi-image editing (e.g. compose A + B), pass a list of images
      and describe the composition in the prompt.
"""
import torch
from diffusers import FluxKontextPipeline
from PIL import Image

MODEL_ID = "black-forest-labs/FLUX.1-Kontext-dev"
INPUT_PATH = "portrait.png"
OUTPUT_PATH = "portrait_edited.png"
PROMPT = "add round glasses and a yellow beanie"


def main() -> None:
    pipe = FluxKontextPipeline.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.bfloat16,
    ).to("cuda")

    input_image = Image.open(INPUT_PATH).convert("RGB")
    edited = pipe(
        image=input_image,
        prompt=PROMPT,
        num_inference_steps=20,
        guidance_scale=2.5,
    ).images[0]
    edited.save(OUTPUT_PATH)
    print(f"Saved: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
