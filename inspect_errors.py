import json

# Select examples for qualitative analysis
indices = [0, 3, 7, 17, 22, 5, 6, 14, 36, 37]

with open("data/dev/dev_track_a.jsonl", encoding="utf-8") as f:
    examples = [json.loads(line) for line in f]

for i in indices:
    example = examples[i]

    print(f"\n{'=' * 60}")
    print(f"EXAMPLE {i}")
    print(f"{'=' * 60}")

    print("\nANCHOR:")
    print(example["anchor_text"])

    print("\nCANDIDATE A:")
    print(example["text_a"])

    print("\nCANDIDATE B:")
    print(example["text_b"])

    print("\nCORRECT ANSWER:",
          "A" if example["text_a_is_closer"] else "B")
