import pandas as pd
import os

# -------------------------------
# Step 1: Load JSON file
# -------------------------------

file_path = "data/trends_20260406.json"   # change if your file name is different

if not os.path.exists(file_path):
    print("File not found:", file_path)
    exit()

df = pd.read_json(file_path)

print(f"Loaded {len(df)} stories from {file_path}")


# -------------------------------
# Step 2: Clean the data
# -------------------------------

# 1. Remove duplicates (same post_id)
df = df.drop_duplicates(subset="post_id")
print(f"After removing duplicates: {len(df)}")

# 2. Remove missing important fields
df = df.dropna(subset=["post_id", "title", "score"])
print(f"After removing nulls: {len(df)}")

# 3. Fix data types (ensure numeric)
df["score"] = pd.to_numeric(df["score"], errors="coerce")
df["num_comments"] = pd.to_numeric(df["num_comments"], errors="coerce")

# 4. Remove low quality (score < 5)
df = df[df["score"] >= 5]
print(f"After removing low scores: {len(df)}")

# 5. Clean title (remove extra spaces)
df["title"] = df["title"].str.strip()


# -------------------------------
# Step 3: Save as CSV
# -------------------------------

output_path = "data/trends_clean.csv"
df.to_csv(output_path, index=False)

print(f"Saved {len(df)} rows to {output_path}")


# -------------------------------
# Step 4: Summary (stories per category)
# -------------------------------

print("\nStories per category:")
print(df["category"].value_counts())