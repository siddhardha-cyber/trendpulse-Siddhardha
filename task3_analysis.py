import pandas as pd


FILE = "data/trends_cleaned.csv"

def analyze():
    print("🚀 Starting Analysis...")

    df = pd.read_csv(FILE)


    print(f"\n📊 Total Stories: {len(df)}")


    print("\n📂 Stories per Category:")
    print(df["category"].value_counts())


    print("\n🔥 Top 5 Stories by Score:")
    print(df.sort_values(by="score", ascending=False)[["title", "score"]].head(5))

    print("\n📈 Average Score:", df["score"].mean())


    print("\n👤 Top Authors:")
    print(df["author"].value_counts().head(5))

    print("\n🎉 Analysis Done!")

if __name__ == "__main__":
    analyze()