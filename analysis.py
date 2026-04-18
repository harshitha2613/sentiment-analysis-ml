import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from wordcloud import WordCloud
import plotly.express as px

print("Election Sentiment Analysis Started")

df = pd.read_csv("data.csv")

# Convert date column
df['date'] = pd.to_datetime(df['date'])

print("\nDataset Loaded:")
print(df.head())

def get_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "Positive", 1
    elif analysis.sentiment.polarity < 0:
        return "Negative", -1
    else:
        return "Neutral", 0

df[['sentiment', 'score']] = df['text'].apply(
    lambda x: pd.Series(get_sentiment(x))
)

plt.figure()
sns.heatmap(pd.crosstab(df['state'], df['sentiment']), annot=True)
plt.title("State vs Sentiment Heatmap")
plt.show()

text = " ".join(df['text'])
wc = WordCloud(width=800, height=400).generate(text)

plt.figure()
plt.imshow(wc)
plt.axis("off")
plt.title("Word Cloud")
plt.show()

state_score = df.groupby('state')['score'].sum()
state_score.plot(kind='bar')
plt.title("State-wise Sentiment Score")
plt.xlabel("State")
plt.ylabel("Score")
plt.show()

district_party = df.groupby(['district', 'party'])['score'].sum().unstack()

print("\nDistrict-wise Party Performance:")
print(district_party)

district_party.plot(kind='bar')
plt.title("District-wise Party Sentiment")
plt.ylabel("Score")
plt.show()

state_map = df.groupby('state')['score'].sum().reset_index()

fig = px.choropleth(
    state_map,
    locations="state",
    locationmode="geojson-id",
    color="score",
    title="India State-wise Sentiment Map"
)

fig.show()

trend = df.groupby('date').size()

trend.plot()
plt.title("Tweet Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Number of Tweets")
plt.show()

party_trend = df.groupby(['date', 'party']).size().unstack()

party_trend.plot()
plt.title("Party-wise Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Tweet Count")
plt.show()

print("\nReal-time Prediction")

user_text = input("Enter tweet: ")
party = input("Enter party: ")

sentiment, score = get_sentiment(user_text)

print("Predicted Sentiment:", sentiment)
print(f"Impact for {party}:", score)

print("\nProject Completed")
