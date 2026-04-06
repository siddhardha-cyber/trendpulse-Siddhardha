import json
import csv


INPUT_FILE = "data/trends_20260406.json"


OUTPUT_FILE = "data/trends_cleaned.csv"


def clean_data():
    print("cleaning data")


    with open(INPUT_FILE, "r") as f:
        data = json.load(f)

    cleaned_data = []

    for item in data:


        if "title" not in item or item["title"] == "":
            continue


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

    print(f"Cleaned {len(cleaned_data)} data")

    with open(OUTPUT_FILE, "w", newline="") as f:
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

    print(f"Saved CSV to {OUTPUT_FILE}")



if __name__ == "__main__":
    clean_data()