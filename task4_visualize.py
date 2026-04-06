import pandas as pd
import matplotlib.pyplot as plt
import os

FILE = "data/trends_cleaned.csv"

def visualize():
    print("🚀 Starting Visualization...")

    df = pd.read_csv(FILE)

    # Create folder for charts
    if not os.path.exists("data/charts"):
        os.makedirs("data/charts")

    # 1️⃣ Category Count Chart
    category_counts = df["category"].value_counts()
    plt.figure()
    category_counts.plot(kind="bar")
    plt.title("Stories per Category")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("data/charts/category_counts.png")
    plt.close()

    # 2️⃣ Top 10 Scores Chart
    top_scores = df.sort_values(by="score", ascending=False).head(10)
    plt.figure()
    plt.barh(top_scores["title"], top_scores["score"])
    plt.title("Top 10 Stories by Score")
    plt.xlabel("Score")
    plt.tight_layout()
    plt.savefig("data/charts/top_scores.png")
    plt.close()

    # 3️⃣ Comments Distribution
    plt.figure()
    df["num_comments"].plot(kind="hist")
    plt.title("Comments Distribution")
    plt.xlabel("Number of Comments")
    plt.tight_layout()
    plt.savefig("data/charts/comments_hist.png")
    plt.close()

    print("📊 Charts saved in data/charts/")
    print("🎉 Task 4 Completed!")

if __name__ == "__main__":
    visualize()