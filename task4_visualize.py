# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import os

print("🚀 Starting Visualization...")

# -------------------------------
# 1. Load data
# -------------------------------
file_path = "data/trends_analysed.csv"
df = pd.read_csv(file_path)

# -------------------------------
# 2. Create outputs folder
# -------------------------------
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# -------------------------------
# 3. Chart 1 — Top 10 stories
# -------------------------------
top10 = df.sort_values(by="score", ascending=False).head(10)

# Shorten long titles
top10["short_title"] = top10["title"].apply(lambda x: x[:50] + "..." if len(x) > 50 else x)

plt.figure(figsize=(8,6))
plt.barh(top10["short_title"], top10["score"])
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()

plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# -------------------------------
# 4. Chart 2 — Stories per category
# -------------------------------
category_counts = df["category"].value_counts()

plt.figure(figsize=(6,5))
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")

plt.savefig("outputs/chart2_categories.png")
plt.close()

# -------------------------------
# 5. Chart 3 — Scatter plot
# -------------------------------
popular = df[df["is_popular"] == True]
not_popular = df[df["is_popular"] == False]

plt.figure(figsize=(7,5))

plt.scatter(popular["score"], popular["num_comments"], label="Popular")
plt.scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")

plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()

plt.savefig("outputs/chart3_scatter.png")
plt.close()

# -------------------------------
# 6. Bonus — Dashboard
# -------------------------------
fig, axes = plt.subplots(1, 3, figsize=(15,5))

# Chart 1
axes[0].barh(top10["short_title"], top10["score"])
axes[0].set_title("Top Stories")
axes[0].invert_yaxis()

# Chart 2
axes[1].bar(category_counts.index, category_counts.values)
axes[1].set_title("Categories")

# Chart 3
axes[2].scatter(popular["score"], popular["num_comments"], label="Popular")
axes[2].scatter(not_popular["score"], not_popular["num_comments"], label="Not Popular")
axes[2].set_title("Score vs Comments")

fig.suptitle("TrendPulse Dashboard")

plt.savefig("outputs/dashboard.png")
plt.close()

print("✅ All charts saved in outputs/")
print("🎉 Done!")