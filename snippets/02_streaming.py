"""02_streaming.py — Token-by-token streaming via TextIteratorStreamer.

Same setup as 01_chat_generation.py, but generation runs on a background
thread and we iterate the streamer to print tokens as they arrive. Lower
time-to-first-token, better UX for chat.

Dependencies:
    pip install transformers torch accelerate

Notes:
    - TextIteratorStreamer yields strings (not token IDs). skip_prompt=True
      means we only get the generated tokens, not the prompt echoed back.
    - Run model.generate() in a Thread; the main thread reads from the
      streamer. If the thread crashes, the iterator just ends silently —
      check the thread's exception if output is unexpectedly short.
"""
from threading import Thread

import torch
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    TextIteratorStreamer,
)

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

    streamer = TextIteratorStreamer(
        tokenizer, skip_prompt=True, skip_special_tokens=True
    )
    gen_kwargs = dict(inputs=inputs, streamer=streamer, max_new_tokens=512)
    thread = Thread(target=model.generate, kwargs=gen_kwargs)
    thread.start()

    for text in streamer:
        print(text, end="", flush=True)
    print()  # trailing newline
    thread.join()


if __name__ == "__main__":
    main()
