
from surprise import Dataset, Reader, SVD
import pandas as pd

def load_data():
    df = pd.read_csv("data/rating.csv")
    df = df[df['rating'] > 0]
    return df

def train_model(df):
    reader = Reader(rating_scale=(1, 10))
    data = Dataset.load_from_df(df[['user_id', 'anime_id', 'rating']], reader)
    trainset = data.build_full_trainset()

    model = SVD()
    model.fit(trainset)
    return model
