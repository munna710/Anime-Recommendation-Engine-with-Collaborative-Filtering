from surprise import Dataset, Reader, SVD
import pandas as pd
import joblib

def train_model():
    df = pd.read_parquet("data_processed/ratings.parquet")
    reader = Reader(rating_scale=(1, 10))
    data = Dataset.load_from_df(df[['user_id', 'anime_id', 'rating']], reader)
    
    trainset = data.build_full_trainset()
    
    model = SVD()
    model.fit(trainset)
    
    joblib.dump(model, "models/svd_model.pkl")
    print("Model trained and saved to models/svd_model.pkl")

if __name__ == "__main__":
    train_model()
