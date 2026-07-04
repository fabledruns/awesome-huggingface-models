"""05_whisper_turbo.py — Batched long-audio transcription with Whisper Turbo.

Whisper has a 30-second window. For audio longer than 30s you must:
    1. Set chunk_length_s=30 so the pipeline splits the file into chunks.
    2. Set return_timestamps=True if you need word/segment timestamps.
    3. Set batch_size=N to parallelize chunk inference (big speedup).

Dependencies:
    pip install transformers torch accelerate
    # Optional: pip install flash-attn (2-3x faster attention on Ampere+)
    ffmpeg  # required by transformers.audio_utils for non-WAV input

Notes:
    - whisper-large-v3-turbo is ~8x faster than whisper-large-v3 with
      near-identical WER on most languages.
    - For very long audio (1h+), consider higher batch_size (16-32) and
      flash-attn. Memory scales with batch_size * chunk_len.
    - If you see hallucinations on silence, lower --chunk_length_s to 20
      and pass `stride_length_s=10` to overlap chunks.
"""
from transformers import pipeline

MODEL_ID = "openai/whisper-large-v3-turbo"
AUDIO_PATH = "meeting.wav"


def main() -> None:
    asr = pipeline(
        "automatic-speech-recognition",
        model=MODEL_ID,
        chunk_length_s=30,
        device="cuda",
    )
    result = asr(
        AUDIO_PATH,
        return_timestamps=True,
        batch_size=8,
    )
    print(result["text"])

    # If return_timestamps=True, you also get chunks:
    if "chunks" in result:
        print("\n--- Chunks ---")
        for chunk in result["chunks"][:10]:
            start, end = chunk["timestamp"]
            print(f"[{start:.1f}s -> {end:.1f}s] {chunk['text']}")


if __name__ == "__main__":
    main()
