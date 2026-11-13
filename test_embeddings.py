
import json
from embeddings import predict

with open("data/dev/dev_track_a.jsonl", encoding="utf-8") as f:
    example = json.loads(next(f))

prediction = predict(
    example["anchor_text"],
    example["text_a"],
    example["text_b"]
)

print("Predicted:", prediction)
print("Actual:", example["text_a_is_closer"])
print("Correct:", prediction == example["text_a_is_closer"])
