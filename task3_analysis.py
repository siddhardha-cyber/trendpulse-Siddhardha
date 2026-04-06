import pandas as pd


FILE = "data/trends_cleaned.csv"

def analyze():
    print("Analyzing data...")

    df = pd.read_csv(FILE)


    print(f"\nTotal Stories: {len(df)}")


    print("\nStories per Category:")
    print(df["category"].value_counts())


    print("\nTop 5 Stories by Score:")
    print(df.sort_values(by="score", ascending=False)[["title", "score"]].head(5))

    print("\nAverage Score:", df["score"].mean())


    print("\nTop Authors:")
    print(df["author"].value_counts().head(5))


if __name__ == "__main__":
    analyze()