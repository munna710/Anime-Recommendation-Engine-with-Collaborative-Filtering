import shutil
import datetime

def ingest_data():
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copy("data/anime.csv", f"data_raw/anime_{timestamp}.csv")
    shutil.copy("data/rating.csv", f"data_raw/rating_{timestamp}.csv")
    print("Data ingested to data_raw folder")

if __name__ == "__main__":
    ingest_data()
