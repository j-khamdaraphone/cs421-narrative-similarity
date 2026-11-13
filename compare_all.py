
import json


def load_results(filename):
    with open(f"results/{filename}", encoding="utf-8") as f:
        return json.load(f)


baseline = load_results("narrative-baseline_dev.json")
structured = load_results("narrative-structured_dev.json")
embeddings = load_results("nomic-embed-text_dev.json")

# Compare predictions for the same dataset examples
assert len(baseline) == len(structured) == len(embeddings)

fixed_by_embeddings = []
embedding_regressions = []
all_wrong = []

for b, s, e in zip(baseline, structured, embeddings):
    assert b["index"] == s["index"] == e["index"]
    assert b["actual"] == s["actual"] == e["actual"]

    if not b["correct"] and not s["correct"] and e["correct"]:
        fixed_by_embeddings.append(b["index"])

    if b["correct"] and not e["correct"]:
        embedding_regressions.append(b["index"])

    if not b["correct"] and not s["correct"] and not e["correct"]:
        all_wrong.append(b["index"])

print("Gemma shared errors fixed by embeddings:",
      len(fixed_by_embeddings))

print("Baseline correct, embeddings incorrect:",
      len(embedding_regressions))

print("All three methods incorrect:", len(all_wrong))

print("\nExamples fixed by embeddings:",
      fixed_by_embeddings[:10])

print("Examples all methods missed:",
      all_wrong[:10])
