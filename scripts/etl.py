import os
import pandas as pd

def etl():
    # Find latest rating CSV in data_raw
    rating_files = sorted([f for f in os.listdir("data_raw") if "rating" in f])
    latest_rating = rating_files[-1]
    
    ratings = pd.read_csv(f"data_raw/{latest_rating}")
    # Remove unrated or zero ratings
    ratings = ratings[ratings['rating'] > 0]
    
    # Save as Parquet in data_processed folder (efficient format)
    ratings.to_parquet("data_processed/ratings.parquet", index=False)
    print("Data transformed and saved as Parquet")

if __name__ == "__main__":
    etl()
