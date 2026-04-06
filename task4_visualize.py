import pandas as pd
import matplotlib.pyplot as plt
import os

FILE = "data/trends_cleaned.csv"

def visualize():
    print("creating charts...")

    df = pd.read_csv(FILE)


    if not os.path.exists("data/charts"):
        os.makedirs("data/charts")

 # Category chart
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

# Score chart
    top_scores = df.sort_values(by="score", ascending=False).head(10)
    plt.figure()
    plt.barh(top_scores["title"], top_scores["score"])
    plt.title("Top 10 Stories by Score")
    plt.xlabel("Score")
    plt.tight_layout()
    plt.savefig("data/charts/top_scores.png")
    plt.close()


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