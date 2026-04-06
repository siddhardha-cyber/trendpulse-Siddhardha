import json
import csv

# ✅ Your actual file (from screenshot)
INPUT_FILE = "data/trends_20260406.json"

# Output file
OUTPUT_FILE = "data/trends_cleaned.csv"


def clean_data():
    print("🚀 Starting cleaning...")

    # Load JSON
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    cleaned_data = []

    for item in data:

        # Skip if no title
        if "title" not in item or item["title"] == "":
            continue

        # Clean each record
        cleaned_item = {
            "post_id": item.get("post_id", ""),
            "title": item.get("title", "").strip(),
            "category": item.get("category", "other"),
            "score": item.get("score", 0),
            "num_comments": item.get("num_comments", 0),
            "author": item.get("author", "unknown"),
            "collected_at": item.get("collected_at", "")
        }

        cleaned_data.append(cleaned_item)

    print(f"✅ Cleaned {len(cleaned_data)} records")

    # Save CSV
    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "post_id",
                "title",
                "category",
                "score",
                "num_comments",
                "author",
                "collected_at"
            ]
        )
        writer.writeheader()
        writer.writerows(cleaned_data)

    print(f"📁 Saved CSV to {OUTPUT_FILE}")
    print("🎉 Done!")


# Run program
if __name__ == "__main__":
    clean_data()