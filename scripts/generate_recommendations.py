import pandas as pd
from surprise import Dataset, Reader, SVD
from src import recommender  # Import from src folder
import joblib

def main():
    print("Loading data...")
    df = recommender.load_data()
    
    print("Training model...")
    model = recommender.train_model(df)
    
    # Save model
    joblib.dump(model, "models/svd_model.pkl")
    print("Model saved at models/svd_model.pkl")

if __name__ == "__main__":
    main()
