import streamlit as st
from src.recommender import load_data, train_model
import pandas as pd

st.title("Anime Recommender Engine")

df = load_data()
model = train_model(df)
#load anime title
anime = pd.read_csv("data/anime.csv")
anime_titles = dict(zip(anime['anime_id'], anime['name']))

user_id = 1
st.subheader(f"Top Anime Recommendations for User ID: {user_id}")


predictions = [model.predict(user_id, i) for i in range(1, 100)]
top_predictions = sorted(predictions, key=lambda x: x.est, reverse=True)[:5]

for pred in top_predictions:
    title = anime_titles.get(pred.iid, "Unknown Anime")
    st.write(f"**{title}**  → Predicted Rating: **{pred.est:.2f}**")
