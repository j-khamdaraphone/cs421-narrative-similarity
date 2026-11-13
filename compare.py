
import json

# Load predictions from both experiments
with open("results/narrative-baseline_dev.json") as f:
    baseline = json.load(f)

with open("results/narrative-structured_dev.json") as f:
    structured = json.load(f)

fixed = []
regressed = []
both_wrong = []
both_correct = []

for b, s in zip(baseline, structured):
    assert b["index"] == s["index"]
    assert b["actual"] == s["actual"]

    if not b["correct"] and s["correct"]:
        fixed.append(b["index"])
    elif b["correct"] and not s["correct"]:
        regressed.append(b["index"])
    elif not b["correct"] and not s["correct"]:
        both_wrong.append(b["index"])
    else:
        both_correct.append(b["index"])

print("Fixed by structured prompting:", len(fixed))
print("Made worse by structured prompting:", len(regressed))
print("Both wrong:", len(both_wrong))
print("Both correct:", len(both_correct))

print("\nExamples fixed:", fixed[:10])
print("Examples regressed:", regressed[:10])

with open("data/dev/dev_track_a.jsonl", encoding="utf-8") as f:
    examples = [json.loads(line) for line in f]

# Display examples where the two prompts disagreed
for index in fixed + regressed:
    example = examples[index]

    print(f"\n{'=' * 60}")
    print(f"EXAMPLE {index}")
    print(f"{'=' * 60}")

    print("\nANCHOR:")
    print(example["anchor_text"])

    print("\nCANDIDATE A:")
    print(example["text_a"])

    print("\nCANDIDATE B:")
    print(example["text_b"])

    print("\nCORRECT ANSWER:",
          "A" if example["text_a_is_closer"] else "B")

    print("BASELINE:",
          "A" if baseline[index]["prediction"] else "B")

    print("STRUCTURED:",
          "A" if structured[index]["prediction"] else "B")

