import requests
import time
import json
import os
from datetime import datetime


TOP_URL = "https://hacker-news.firebaseio.com/v0/topstories.json"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"

HEADERS = {"User-Agent": "TrendPulse/1.0"}


CATEGORIES = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}


def get_category(title):
    title = title.lower()
    for cat, keywords in CATEGORIES.items():
        for word in keywords:
            if word in title:
                return cat
    return "other"


def get_story_ids():
    try:
        res = requests.get(TOP_URL, headers=HEADERS)
        return res.json()[:500]   
    except:
        print("Failed to fetch story IDs")
        return []


def get_story(story_id):
    try:
        url = ITEM_URL.format(story_id)
        res = requests.get(url, headers=HEADERS)
        return res.json()
    except:
        return None


def main():
    print("🚀 Starting Data Collection...")

    story_ids = get_story_ids()
    results = []

    for sid in story_ids:
        story = get_story(sid)

        if not story or "title" not in story:
            print("⚠️ Failed story:", sid)
            continue

        title = story["title"]
        category = get_category(title)

        data = {
            "post_id": story.get("id"),
            "title": title,
            "category": category,
            "score": story.get("score", 0),
            "num_comments": story.get("descendants", 0),
            "author": story.get("by", "unknown"),
            "collected_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        results.append(data)


        if len(results) >= 125:
            break


    if not os.path.exists("data"):
        os.makedirs("data")


    filename = f"data/trends_{datetime.now().strftime('%Y%m%d')}.json"
    with open(filename, "w") as f:
        json.dump(results, f, indent=4)

    print(f"✅ Collected {len(results)} stories")
    print(f"📁 Saved to {filename}")
    print("🎉 Done!")


if __name__ == "__main__":
    main()