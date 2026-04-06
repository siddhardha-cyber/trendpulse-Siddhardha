# Import required libraries
import pandas as pd
import numpy as np

print("🚀 Starting Analysis...")

# -------------------------------
# 1. Load the CSV file
# -------------------------------
file_path = "data/trends_clean.csv"

df = pd.read_csv(file_path)

# Print basic info
print(f"Loaded data: {df.shape}")
print("\nFirst 5 rows:")
print(df.head())

# -------------------------------
# 2. Basic statistics
# -------------------------------
avg_score = df["score"].mean()
avg_comments = df["num_comments"].mean()

print("\nAverage score:", round(avg_score, 2))
print("Average comments:", round(avg_comments, 2))

# -------------------------------
# 3. NumPy analysis
# -------------------------------
scores = df["score"].values

print("\n--- NumPy Stats ---")
print("Mean score:", round(np.mean(scores), 2))
print("Median score:", round(np.median(scores), 2))
print("Std deviation:", round(np.std(scores), 2))
print("Max score:", np.max(scores))
print("Min score:", np.min(scores))

# -------------------------------
# 4. Category with most stories
# -------------------------------
category_counts = df["category"].value_counts()

top_category = category_counts.idxmax()
top_count = category_counts.max()

print(f"\nMost stories in: {top_category} ({top_count} stories)")

# -------------------------------
# 5. Most commented story
# -------------------------------
max_comments_row = df.loc[df["num_comments"].idxmax()]

print("\nMost commented story:")
print(f"\"{max_comments_row['title']}\" - {max_comments_row['num_comments']} comments")

# -------------------------------
# 6. Add new columns
# -------------------------------

# engagement = num_comments / (score + 1)
df["engagement"] = df["num_comments"] / (df["score"] + 1)

# is_popular = True if score > average score
df["is_popular"] = df["score"] > avg_score

# -------------------------------
# 7. Save result
# -------------------------------
output_path = "data/trends_analysed.csv"

df.to_csv(output_path, index=False)

print(f"\nSaved to {output_path}")
print("🎉 Done!")