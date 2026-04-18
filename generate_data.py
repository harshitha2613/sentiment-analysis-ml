import pandas as pd
import random

states = ["Karnataka", "Tamil Nadu", "Delhi", "Maharashtra", "Kerala"]
districts = ["Bangalore", "Chennai", "New Delhi", "Mumbai", "Kochi"]
parties = ["Party A", "Party B", "Party C"]

positive_texts = [
    "good government policies",
    "excellent development work",
    "great leadership",
    "happy with services",
    "positive growth"
]

negative_texts = [
    "bad leadership",
    "poor infrastructure",
    "not satisfied",
    "corruption issues",
    "bad policies"
]

neutral_texts = [
    "average performance",
    "okay services",
    "no strong opinion",
    "moderate growth",
    "neutral response"
]

data = []

for i in range(1000):
    state = random.choice(states)
    district = random.choice(districts)
    party = random.choice(parties)

    sentiment_type = random.choice(["positive", "negative", "neutral"])

    if sentiment_type == "positive":
        text = random.choice(positive_texts)
    elif sentiment_type == "negative":
        text = random.choice(negative_texts)
    else:
        text = random.choice(neutral_texts)

    data.append([state, district, party, text])

df = pd.DataFrame(data, columns=["state", "district", "party", "text"])

df.to_csv("data.csv", index=False)

print("Dataset with 1000 rows created successfully!")
